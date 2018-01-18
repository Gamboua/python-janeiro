import logging

logging.basicConfig(
    filename="app.log",
    level=logging.CRITICAL,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="[ %d/%m/%Y - %H:%M:%s ]"
)

logging.critical("Novo log")