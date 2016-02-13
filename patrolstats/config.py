# -*- coding: utf-8 -*-

import json


required_cfg_settings = frozenset(["wikis", "output_dir"])


class ConfigError(Exception):
    pass


def check_config(cfg):
    missing = []
    for setting in required_cfg_settings:
        if setting not in cfg:
            missing.append(setting)

    if len(missing) != 0:
        raise ConfigError("Missing required settings: {}", missing)


def load_config_from_file(filename):
    with open(filename, "r") as f:
        cfg = json.load(f)
        check_config(cfg)
        return cfg
