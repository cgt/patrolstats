# -*- coding: utf-8 -*-

import pytest

from patrolstats import db


def test_is_autopatrol():
    log_params_auto = """a:3:{s:8:"4::curid";i:8450575;s:9:"5::previd";i:8450569;s:7:"6::auto";i:1;}"""
    log_params_not_auto = """a:3:{s:8:"4::curid";s:7:"8450569";s:9:"5::previd";s:7:"8406023";s:7:"6::auto";i:0;}"""

    assert db.is_autopatrol(log_params_auto)
    assert not db.is_autopatrol(log_params_not_auto)
