import pytest
import requests
from pathlib import Path
import os
import shutil


def pytest_configure(config):
    # Determine base reports directory:
    # Priority: REPORTS_DIR env -> PROJECT_ROOT/REPO_ROOT env -> repository root
    repo_root = Path(__file__).resolve().parent

    reports_dir_env = os.environ.get("REPORTS_DIR")
    project_root_env = os.environ.get("PROJECT_ROOT") or os.environ.get("REPO_ROOT")

    if reports_dir_env:
        reports_dir = Path(reports_dir_env)
    elif project_root_env:
        reports_dir = Path(project_root_env) / "reports"
    else:
        reports_dir = repo_root / "reports"

    reports_dir.mkdir(parents=True, exist_ok=True)

    # If pytest was invoked from a different cwd that already has a 'reports' folder,
    # remove it so outputs go only into the chosen reports folder.
    cwd_reports = Path.cwd() / "reports"
    try:
        if cwd_reports.exists() and cwd_reports.resolve() != reports_dir.resolve():
            shutil.rmtree(cwd_reports)
    except Exception:
        # best-effort: ignore cleanup failures
        pass

    # Override html and allure output paths so they always point to the chosen reports folder
    try:
        config.option.htmlpath = str(reports_dir / "report.html")
    except Exception:
        pass

    try:
        config.option.alluredir = str(reports_dir / "allure-results")
    except Exception:
        pass


@pytest.fixture(scope="function")
def browser_context(playwright, browser_context_args):
    # browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    browser = playwright.chromium.launch(headless=True, args=["--start-maximized"])
    context = browser.new_context()  # isolated browser context
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def page(browser_context, base_url):
    page = browser_context.new_page()
    page.goto(base_url)
    yield page
    page.close()

# --- n8n Webhook Hook ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Extract metadata about the failure
        payload = {
            "project_name": "Playwright-Framework-Ecom",  # <-- ADD THIS LINE HERE!
            "test_name": item.name,
            "file_path": item.fspath.strpath,
            "error_message": str(report.longreprtext)[:1000]
        }

        # Your permanent production URL (can be overridden with N8N_WEBHOOK_URL)
        n8n_webhook_url = os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook/0c48f4a1-6f55-4aa4-812a-540f754ad4d1")

        try:
            requests.post(n8n_webhook_url, json=payload, timeout=5)
            print(f"\n[n8n Alert] Successfully sent failure details for {item.name}")
        except requests.RequestException as e:
            print(f"\n[n8n Alert] Failed to send data to n8n: {e}")
