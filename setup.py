#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "watchdog",
]

setup_requirements = []

test_requirements = []

setup(
    author="Paul J. Gierz",
    author_email="pgierz@awi.de",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="A watchdog package that automatically fixes and resubmits pism jobs after common crashes",
    entry_points={"console_scripts": ["watchdog_pism=watchdog_pism.cli:main",],},
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="watchdog_pism",
    name="watchdog_pism",
    packages=find_packages(include=["watchdog_pism", "watchdog_pism.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/pgierz/watchdog_pism",
    version="0.1.0",
    zip_safe=False,
)
