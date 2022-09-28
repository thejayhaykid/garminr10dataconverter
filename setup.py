# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

setup(
    name="Garmin Approach R10 Data Converter",
    version="1.0.0",
    description="Convert your Garmin Approach R10 Data into CSV files.",
    long_description=readme,
    url="https://github.com/earl553/garminr10dataconverter",
    packages=find_packages(exclude="test"),
    entry_points={"console_scripts": ["gar10 = gar10.cli:main"]},
    install_requires=["click", "pandas"],
)
