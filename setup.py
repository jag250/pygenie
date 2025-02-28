"""
  Copyright 2025 Netflix, Inc.

     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nflx-genie-client',
    versioning='devcommit',
    author='Netflix Inc.',
    author_email='genieoss@googlegroups.com',
    keywords='genie hadoop cloud netflix client bigdata presto',
    packages=['pygenie',
              'pygenie.adapter',
              'pygenie.jobs'],
    package_data={
        'pygenie': ['genie.ini']
    },
    scripts=[],
    url='http://netflix.github.io/genie/',
    license='Apache 2.0',
    description='Genie Python Client.',
    long_description=long_description,
    install_requires=[
        "decorator",
        "multipledispatch",
        "pyconfigurator",
        "python-dateutil >= 2.4",
        "requests",
        "six",
        "importlib-metadata",
    ],
    setup_requires=['setupmeta'],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',


        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. 
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',        
    ],
)
