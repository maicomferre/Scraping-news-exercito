import logging
import os

class Log:
    name = None
    def __init__(self, name):
        self.name = name
        os.makedirs('log', exist_ok=True)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Criar manipulador de arquivo
        file_handler = logging.FileHandler('log/service.log', mode='a+')
        file_handler.setLevel(logging.DEBUG)

        # Configurar formato do log
        formatter = logging.Formatter(
            fmt="{asctime} - {levelname} - {message}",
            style="{",
            datefmt="%Y-%m-%d %H:%M"
        )
        file_handler.setFormatter(formatter)

        # Evitar múltiplos manipuladores duplicados
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)

    def warning(self, msg):
        print(f"warning[{self.name}]: {msg}")
        self.logger.warning(msg)

    def error(self, msg):
        print(f"error[{self.name}]: {msg}")
        self.logger.error(msg)

    def critical(self, msg):
        print(f"critical[{self.name}]: {msg}")
        self.logger.critical(msg)

    def info(self, msg):
        print(f"info[{self.name}]: {msg}")
        self.logger.info(msg)

    def debug(self, msg):
        print(f"debug[{self.name}]: {msg}")
        self.logger.debug(msg)

    def exception(self, msg):
        print(f"exception[{self.name}]: {msg}")
        self.logger.exception(msg)