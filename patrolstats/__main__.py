# -*- coding: utf-8 -*-

from __future__ import absolute_import
import argparse
import datetime
import io
import logging
import os.path

import appdirs

from . import config
from . import db
from . import log
from .genpage import genpage


def one_week_ago():
    today = datetime.date.today()
    one_week = datetime.timedelta(days=7)
    return "{:%Y%m%d%H%M%S}".format(today-one_week)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", action="store", help="config file path")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        log.set_level(logging.DEBUG)
    logger = log.get_logger(__name__)

    cfg_dir = appdirs.user_config_dir("patrolstats")
    cfg_path = args.config or os.path.join(cfg_dir, "patrolstats.json")

    cfg = config.load_config_from_file(cfg_path)
    logger.debug("Loaded config from {}".format(cfg_path))

    for wiki in cfg["wikis"]:
        logger.debug("Getting stats for {}".format(wiki))
        stats = db.get_patrol_stats(wiki, one_week_ago())
        logger.debug("Generating stats page for {}".format(wiki))
        page = genpage(stats, wiki, cfg["wikis"][wiki])

        file_path = os.path.join(cfg["output_dir"], "{}.html".format(wiki))
        with io.open(file_path, mode="w", encoding="utf8") as f:
            f.write(page)
        logger.info("Wrote stats for {} to {}".format(wiki, file_path))


if __name__ == "__main__":
    main()
