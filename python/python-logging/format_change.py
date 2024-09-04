# -*- coding: utf-8 -*-
"""To use logging bluemesh.

It is very simple to make log inside bluemesh module. You can get logs from through two
functions.

Example:
    In order to turn on the log recording function inside bluemesh, a handler must be
    registered. Handler could be added through two ways: ``add_stream_handler`` makes
    handler when you get logs from stream like stdout, and ``add_file_handler`` is used
    to make log file::

        import bluemesh.bluemesh_logging as logging
        logging.add_stream_handler("bluemesh", loglevel = "INFO")
        logging.add_file_handler("bluemesh", "bluemesh.log", loglevel = "DEBUG",
            logformat = "%(asctime)s - %(name)s - %(funcName)s - %(processName)s"
                      + "(%(process)d) - %(threadName)s(%(thread)d) - %(levelname)s"
                      + "- %(message)s")

    First argument is the module name. Each module hierarchy may looks like this::

        bluemesh
        |   .application
        |   .element
        |   .interface
        |   .models
        |   |   .base
        |   |   .config
        |   |   .general_level
        |   |   ...
        |   .access

    User-defined(vendor) model might need to write logs. Add logging for
    user-defined models::

        import bluemesh.bluemesh_logging as logging
        logger = logging.get_logger("bluemesh.models.user_custom_model")
        logger.info("You can write log this way: opcode({})", 0xC005F1)

"""

import logging

_logger = logging.getLogger("bluemesh")
_logger.setLevel(logging.DEBUG)

_logger.addHandler(logging.NullHandler())
DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
"""str: logging format if ``logformat`` is not specify when adding logger handler.

You can make formats and find the attributes from `here`_.

.. _here: https://docs.python.org/3/library/logging.html#logrecord-attributes

"""

class __Message:
    def __init__(self, fmt, args):
        self.fmt = fmt
        self.args = args

    def __str__(self):
        return self.fmt.format(*self.args)

class __StyleAdapter(logging.LoggerAdapter):
    def __init__(self, logger, extra=None):
        super().__init__(logger, extra or {})

    def log(self, level, msg, /, *args, **kwargs):
        if self.isEnabledFor(level):
            self.logger._log(level, Message(msg, args), (), **kwargs)


def get_logger(name=None):
    """To use when getting logger instance. You can find more information by
    `logging.getLogger`_.

    Return:
        An instance of ``logging.LoggerAdapter``. You can find more information by
        `logging.LoggerAdapter`_ and `logging.Logger`_.

    .. _logging.getLogger:
       https://docs.python.org/3/library/logging.html#logging.getLogger
    .. _logging.LoggerAdapter:
       https://docs.python.org/3/library/logging.html#logging.LoggerAdapter
    .. _logging.Logger: https://docs.python.org/3/library/logging.html#logging.Logger

    """
    return StyleAdapter(logging.getLogger(name))


def add_stream_handler(name: str, stream=None, loglevel: str = "WARN", logformat=None):
    """To use to get logs into stream like console.

    Args:
        name: A module name for printing logs.
        stream: An output stream. When stream is None, it shall print by standard
            output.
        loglevel: logging level after severity; DEBUG, INFO, WARN, ERROR, CRITICAL.
        logformat: Logging format to write. If None, this is set
            ``DEFAULT_LOG_FORMAT``.

    """
    handler = logging.StreamHandler(stream)
    handler.setLevel(getattr(logging, loglevel))
    handler.setFormatter(
        logging.Formatter(logformat if logformat is not None else DEFAULT_LOG_FORMAT)
    )
    logging.getLogger(name).addHandler(handler)


def add_file_handler(name: str, file_name: str, loglevel: str = "INFO", logformat=None):
    """To use to get logs into a file.

    Args:
        name: A module name for printing logs.
        file_name: A logfile path.
        loglevel: logging level after severity; DEBUG, INFO, WARN, ERROR, CRITICAL.
        logformat: Logging format to write. If None, this is set
            ``DEFAULT_LOG_FORMAT``.

    """
    handler = logging.FileHandler(file_name)
    handler.setLevel(getattr(logging, loglevel))
    handler.setFormatter(
        logging.Formatter(logformat if logformat is not None else DEFAULT_LOG_FORMAT)
    )
    logging.getLogger(name).addHandler(handler)

