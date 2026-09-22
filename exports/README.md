n8n exported workflows
======================

This folder contains exported n8n workflows (JSON) that can be safely committed to GitHub. Each file represents a single workflow and does NOT include sensitive credentials.

How to import
-------------
1. Open your local n8n instance (http://localhost:5678).
2. In the top-left workflow menu, choose Import -> Upload file and select the JSON file from this folder.
3. Recreate any credentials (API keys, OAuth) in your local n8n instance as needed.

Files in this folder
--------------------
- (If exports were found in your n8n database, the JSON files will appear here.)

If no JSON files are present, export workflows from the n8n UI: open the workflow -> three-dot menu -> Export -> Export (or Export as JSON) and save into this folder.
