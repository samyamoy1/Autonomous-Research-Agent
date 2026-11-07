
import logging
from pathlib import Path


def setup_logger():
    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    logger = logging.getLogger("research_agent")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(
            log_directory / "agent.log",
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
