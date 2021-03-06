#!/usr/bin/env python

from setuptools import setup, find_packages


install_requires = [
    "cassiopeia",
    "datapipelines>=1.0.3",
    "simplekv"
]

setup(
    name="cassiopeia-diskstore",
    version="1.0.1",
    author="Jason Maldonis; Rob Rua",
    author_email="team@merakianalytics.com",
    url="https://github.com/meraki-analytics/cassiopeia-datastores/tree/master/cassiopeia-diskstore",
    description="A disk data store for the Cassiopeia League of Legends wrapper.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
    license="MIT",
    packages=find_packages(),
    zip_safe=True,
    install_requires=install_requires,
    include_package_data=True
)
