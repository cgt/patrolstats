# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import datetime
import io
import os.path

import appdirs

from . import config
from . import db
from .genpage import genpage


def one_week_ago():
    today = datetime.date.today()
    one_week = datetime.timedelta(days=7)
    return "{:%Y%m%d%H%M%S}".format(today-one_week)


def main():
    cfg_dir = appdirs.user_config_dir("patrolstats")
    cfg_path = os.path.join(cfg_dir, "patrolstats.json")
    cfg = config.load_config_from_file(cfg_path)

    for wiki in cfg["wikis"]:
        stats = db.get_patrol_stats(wiki, one_week_ago())
        page = genpage(stats)

        file_path = os.path.join(cfg["output_dir"], "{}.html".format(wiki))
        with io.open(file_path, mode="w", encoding="utf8") as f:
            f.write(page)


if __name__ == "__main__":
    main()
