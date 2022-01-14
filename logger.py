import logging
import os.path
import os
import sys
from logging.handlers import RotatingFileHandler

def create_dir_if_not_exist(dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

def setup(app_name, logdir="./log", level=logging.INFO, rotation=10, size=20_000_000):
    create_dir_if_not_exist(logdir)
    formatter = logging.Formatter("[%(asctime)s %(levelname)s]: %(message)s")
    rootLogger = get_root_logger(level)

    setup_activity(app_name, rotation, size, logdir, formatter, rootLogger)
    setup_error(app_name, logdir, formatter, rootLogger)
    setup_console(formatter, rootLogger)

def get_root_logger(level):
    rootLogger = logging.getLogger()
    # clean up all the handlers
    rootLogger.handlers = []
    rootLogger.setLevel(level)
    return rootLogger

def config_log_dir():
    basedir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    runtime = os.path.join(os.path.dirname(os.path.dirname(basedir)), 'runtime')
    log_dir = os.path.join(runtime, "log")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return log_dir


def setup_console(formatter, rootLogger):
    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(formatter)
    consoleHandler.setLevel(logging.INFO)
    rootLogger.addHandler(consoleHandler)

def setup_error(app_name, log_dir, formatter, rootLogger):
    err_fileHandler = RotatingFileHandler(f"{log_dir}/{app_name}_error.log", maxBytes=20_000_000, backupCount=10)
    err_fileHandler.setFormatter(formatter)
    err_fileHandler.setLevel(logging.ERROR)
    rootLogger.addHandler(err_fileHandler)

def setup_activity(app_name, rotation, size, log_dir, formatter, rootLogger):
    activity_fileHandler = RotatingFileHandler(f"{log_dir}/{app_name}_activity.log", maxBytes=size,
                                               backupCount=rotation)
    activity_fileHandler.setFormatter(formatter)
    activity_fileHandler.setLevel(logging.INFO)
    rootLogger.addHandler(activity_fileHandler)