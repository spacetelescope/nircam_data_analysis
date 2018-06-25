#! /usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(
    name='nircam_data_analysis',
    version = '1.0',
    description = 'NIRCam data analysis tools',
    long_description = ('A collection of tools for analyzing NIRCam'
                        'imaging and WFSS data after pipeline processing.'),
    author = 'STScI NIRCam Team',
    author_email = 'acanipe@stsci.edu',
    keywords = ['astronomy'],
    classifiers = ['Programming Language :: Python'],
    packages = find_packages(exclude=["examples"]),
    install_requires = [],
    include_package_data = True
    )
