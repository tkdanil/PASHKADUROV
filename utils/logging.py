import logging


def setup_logger(level: int = logging.INFO, fname: str = __name__) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)s | %(name)s: %(message)s",
        datefmt="[%d-%m-%Y %H:%M:%S]",
        level=level,
        handlers=[logging.FileHandler(f"logs/{fname}.log", mode='w'), ],
    )
