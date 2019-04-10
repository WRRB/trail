#!/usr/bin/env python

from setuptools import setup, find_packages

dependencies = ['requests']

test_dependencies = []

setup(
    name='trail',
    version='0.1.0',
    description='A Belgian rail notification system',
    long_description='',
    author='Wim Berchmans',
    author_email="wimberchmans@gmail.com",
    license='',
    url='https://github.com/WRRB/trail',
    include_package_data=True,
    package_data={},
    packages=find_packages(),
    install_requires=dependencies,
    tests_require=test_dependencies,
    scripts=['trail/cli/trail', 'trail/cli/trail.bat'],
    zip_safe=False
)
