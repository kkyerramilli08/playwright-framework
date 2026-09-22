import logging

# logging.basicConfig(filename="../logs/logfile1.log", format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m-%d-%y %I:%M:%S %p',level=logging.INFO)
#
# log = logging.getLogger()
# log.error(" I am at error block")
# log.info(" This is kamal kiran")

def log():
    logging.basicConfig(filename="../logs/logfile1.log", format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%m-%d-%y %I:%M:%S %p', level=logging.INFO)
    logger = logging.getLogger()
    return logger
logger = log()
logger.info("this is from a function or a utility")
