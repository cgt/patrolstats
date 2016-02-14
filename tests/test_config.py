# -*- coding: utf-8 -*-

import pytest

from patrolstats import config


def test_check_config_missing_required():
    invalid_cfg = {"notwikis": [], "thisshouldfail": True}
    with pytest.raises(config.ConfigError):
        config.check_config(invalid_cfg)


def test_check_config():
    valid_cfg = {
        "wikis": ["doesn't matter", "fakewiki"],
        "output_dir": "/dev/null",
    }
    config.check_config(valid_cfg)
