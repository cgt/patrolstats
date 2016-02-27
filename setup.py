#!/usr/bin/env python2

from setuptools import setup, find_packages

setup(
    name="patrolstats",
    author="Christoffer G. Thomsen",
    author_email="chris@cgt.name",
    license="Boost Software License 1.0",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    tests_require=["pytest"],
    install_requires=["appdirs", "Jinja2", "phpserialize", "wmflabs"],
    entry_points={
        "console_scripts": [
            "patrolstats=patrolstats:main",
        ],
    },
)
