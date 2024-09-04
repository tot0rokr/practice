import custom_logging_module

logger = custom_logging_module.get_logger(__name__)
print (__name__)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
