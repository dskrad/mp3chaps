#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'mp3chaps'
VERSION = '0.3'
KEYWORDS = 'mp3 chapters'
DESCRIPTION = 'tool for inserting chapter marks in mp3 files'
URL = 'https://github.com/dskrad/mp3chaps'
EMAIL = 'dskcl1@gmail.com'
AUTHOR = 'David Karimeddini'

# What packages are required for this module to be executed?
REQUIRED = [
    'docopt>=0.6.2', 'eyeD3>=0.9.5'
    ]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
  long_description = '\n' + f.read()


class UploadCommand(Command):
  """Support setup.py upload."""

  description = 'Build and publish the package.'
  user_options = []

  @staticmethod
  def status(s):
    """Prints things in bold."""
    print('\033[1m{0}\033[0m'.format(s))

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def run(self):
    try:
      self.status('Removing previous builds…')
      rmtree(os.path.join(here, 'dist'))
    except OSError:
      pass

    self.status('Building Source and Wheel (universal) distribution…')
    os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

    self.status('Uploading the package to PyPi via Twine…')
    os.system('twine upload dist/*')

    sys.exit()


setup(
  name=NAME,
  version=VERSION,
  description=DESCRIPTION,
  long_description=long_description,
  author=AUTHOR,
  author_email=EMAIL,
  url=URL,
  #packages=find_packages(exclude=('tests',)),
  # If your package is a single module, use this instead of 'packages':
  py_modules=["mp3chaps"],

  entry_points={
    'console_scripts': [ 'mp3chaps=mp3chaps:main' ],
    },
  install_requires=REQUIRED,
  include_package_data=True,
  license='MIT',
  keywords=KEYWORDS,

  classifiers=[
    # Trove classifiers
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy'
    ],
  # $ setup.py publish support.
  cmdclass={
    'upload': UploadCommand
    },
)
