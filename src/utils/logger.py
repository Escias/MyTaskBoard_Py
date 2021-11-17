import logging


def logs(disable_logs, file):
    if disable_logs:
        logging.getLogger().disabled = disable_logs
    else:
        logging.basicConfig(
            level=logging.INFO,  # type of log
            format="%(asctime)s [%(levelname)s] %(message)s",  # format of message
            handlers=[
                logging.FileHandler(file, mode='w'),
                logging.StreamHandler()
            ]
        )