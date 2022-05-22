import logging

logging.basicConfig(filemode="w", encoding="utf-8")

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('->>> [%(levelname)s] : %(asctime)s : %(message)s')
formatter_console = logging.Formatter('[%(levelname)s] : %(asctime)s : %(message)s')

file_handler = logging.FileHandler("main_logging.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter_console)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
