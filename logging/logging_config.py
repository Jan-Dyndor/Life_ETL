import sys

from loguru import logger


def congigure_logger():
    logger.remove()
    logger.add(sys.stderr, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
    logger.info("Logger configurated")
