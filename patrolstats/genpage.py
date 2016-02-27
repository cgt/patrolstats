# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import datetime

from jinja2 import Environment, PackageLoader

from .messages import messages


env = Environment(loader=PackageLoader("patrolstats", "templates"))


def genpage(stats, wiki, options):
    tmpl = env.get_template("statstable.html")
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    msgs = messages[options["language"]]
    return tmpl.render(stats=stats, timestamp=now, msg=msgs, wiki=wiki)
