import logging

# create logger
logger = logging.getLogger(__name__)
print (__name__)
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create console handler and set level to info
streamhandler = logging.StreamHandler()
streamhandler.setLevel(logging.DEBUG)

# add formatter to streamhandler
streamhandler.setFormatter(formatter)

# add streamhandler to logger
logger.addHandler(streamhandler)

#  # create file handler and set level to debug
#  filehandler = logging.FileHandler("sample.log")
#  filehandler.setLevel(logging.DEBUG)

#  # add formatter to filehandler
#  filehandler.setFormatter(formatter)

#  # add filehandler to logger
#  logger.addHandler(filehandler)

def get_logger(*args, **kwargs):
    return logging.getLogger(*args, **kwargs)
