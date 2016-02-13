from setuptools import setup, find_packages


setup(
    name="patrolstats",
    author="Christoffer G. Thomsen",
    author_email="chris@cgt.name",
    license="Boost Software License 1.0",
    packages=find_packages(),
    install_requires=["appdirs", "Jinja2", "phpserialize", "wmflabs"],
    package_data={
        "patrolstats": ["templates/*"],
    },
    entry_points={
        "console_scripts": [
            "patrolstats=patrolstats:main",
        ],
    },
)
