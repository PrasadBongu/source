import logging

# create logger
logger = logging.getLogger("prasad.logger")

# set level to logger
logger.setLevel(logging.DEBUG)

# print to console handler
ch = logging.StreamHandler()

# print to file handler
fh = logging.FileHandler("prasd_file")

# set level to ch and fh
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

#formate creation
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(lavelname)s - %(lineno)s - %(message)s")

#add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

#logger to fh and ch
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug(dir(dict))
logger.debug(help(dict.copy))
logger.debug(dir(dict))
logger.debug(help(dict.copy))
logger.debug(dir(str.replace))

logger.debug(help(str.replace))



