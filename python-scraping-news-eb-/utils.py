import logging
import os


class Log:
    def __init__(self, name):
        os.makedirs('log', exist_ok=True)

        logging.basicConfig(
            format="{asctime} - {levelname} - {message}",
            filemode='a+',
            filename='log/service.log',
            style="{",
            datefmt="%Y-%m-%d %H:%M",
            level=logging.NOTSET,
        )
        logging.debug(f"Log de {name=}")

    def warning(self, msg):
        logging.warning(msg)

    def error(self, msg):
        logging.error(msg)

    def critical(self, msg):
        logging.critical(msg)

    def info(self, msg):
        logging.info(msg)

    def debug(self, msg):
        logging.debug(msg)

    def exception(self, msg):
        logging.exception(msg)
