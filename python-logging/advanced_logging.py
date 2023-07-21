import logging

# create logger
logger = logging.getLogger('advanced_example')
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create console handler and set level to info
streamhandler = logging.StreamHandler()
streamhandler.setLevel(logging.INFO)

# add formatter to streamhandler
streamhandler.setFormatter(formatter)

# add streamhandler to logger
logger.addHandler(streamhandler)

# create file handler and set level to debug
filehandler = logging.FileHandler("sample.log")
filehandler.setLevel(logging.DEBUG)

# add formatter to filehandler
filehandler.setFormatter(formatter)

# add filehandler to logger
logger.addHandler(filehandler)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
