# -*- coding: utf-8 -*-

import logging
import sys
import time

_level = logging.INFO
_loggers = []


def get_logger(name):
    l = logging.getLogger(name)
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.formatter = logging.Formatter("%(asctime)s UTC %(name)-12s %(levelname)-8s %(message)s")
    handler.formatter.converter = time.gmtime
    l.addHandler(handler)
    l.setLevel(_level)
    _loggers.append(l)
    return l


def set_level(level):
    global _level
    _level = level
    for l in _loggers:
        l.setLevel(_level)
