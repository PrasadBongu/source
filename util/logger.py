import logging


def get_logger():
    # create logger
    logger = logging.getLogger("simple_example")
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    fh = logging.FileHandler("python_training.log")
    ch.setLevel(logging.DEBUG)
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter("%(asctime)s-%(levelname)s - %(filename)s-%(lineno)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger