# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import datetime

from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader("patrolstats", "templates"))


def genpage(stats):
    tmpl = env.get_template("statstable.html")
    now = datetime.datetime.utcnow()
    return tmpl.render(stats=stats, timestamp=now)
