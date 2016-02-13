# -*- coding: utf-8 -*-

from __future__ import print_function
import collections
from operator import itemgetter

import wmflabs
import phpserialize as php


def is_autopatrol(log_params):
    p = php.loads(log_params)
    return p["6::auto"] == 1


def get_patrol_stats(db_name, oldest_ts):
    db = wmflabs.db.connect(db_name)
    with db.cursor() as c:
        c.execute("""select log_user_text, log_params from logging
                  where log_action = 'patrol' and log_timestamp > ?
                  order by log_timestamp
                  desc""",
                  params=[oldest_ts])
        patrols = collections.Counter()
        for log_user_text, log_params in c:
            if not is_autopatrol(log_params):
                patrols[log_user_text.decode("utf-8")] += 1

        return collections.OrderedDict(reversed(sorted(patrols.items(), key=itemgetter(1))))
    db.close()
