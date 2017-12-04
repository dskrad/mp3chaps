from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(
    name='mp3chaps',
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.1',
    description='tool for inserting chapter marks in mp3 files',
    long_description=open("README.rst", encoding="utf8").read(),

    url='https://github.com/dskrad/mp3chaps',

    author='David Karimeddini',
    author_email='dskcl1@gmail.com',
    license='MIT',

    keywords='mp3 chapters',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["mp3chaps"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
      'docopt>=0.6.2',
      'eyeD3>=0.8.4'
      ],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'mp3chaps=mp3chaps:main',
        ],
    },
)
