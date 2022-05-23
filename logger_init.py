import logging

logging.basicConfig(level=logging.DEBUG, filemode="w", encoding="utf-8", style="{")

logger_mine = logging.getLogger("logger")
handler = logging.FileHandler("main_logging.log")
formatter = logging.Formatter("->>> [%(levelname)s] : [%(asctime)s] : %(message)s")
handler.setFormatter(formatter)
logger_mine.addHandler(handler)
