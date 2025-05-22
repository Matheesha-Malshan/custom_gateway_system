import logging


class Log:

    def __init__(self, log_file: str = "file_events.log"):
        self.logger = logging.getLogger("EventLogger")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)