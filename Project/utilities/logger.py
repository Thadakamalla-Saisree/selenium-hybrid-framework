import logging
import os
import datetime
from utilities.config_reader import ConfigReader


def configure_logger():
    """
    Method name: configure_logger
    Author name: Anushka
    Short description of method:
        Configures and returns a logger with both console and file handlers.
        Log files are created with timestamp-based names.
    Return type: logging.Logger
    Parameter list: None
    """

    try:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            logger.handlers.clear()

        config = ConfigReader()

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        log_directory = config.get_value("PATH", "logger_path")

        os.makedirs(log_directory, exist_ok=True)

        log_file_path = os.path.join(log_directory, f"log_{timestamp}.log")
        file_handler = logging.FileHandler(log_file_path, mode="a")
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger

    except Exception as error:
        raise Exception(f"Error while configuring logger: {error}")