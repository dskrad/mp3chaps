mp3chaps
========

commandline utility for adding chapter marks to mp3 files similar to ``mp4chaps`` utility

many pocast apps on Android and iOS support chapter markers in both mp4 (aac) and mp3 files

this utilizes the excellent `eyeD3 <https://github.com/nicfit/eyeD3>`_ tagging module to read and write chapter frames and title subframes

requirements
------------
Python 3 (Python 2 is no longer supported)

installation
------------

``pip3 install mp3chaps``

usage
-----

assuming you have a file named ``episode_42.mp3``, ``mp3chaps`` looks for a chapter marks file called ``episode_42.chapters.txt`` in the same directory.

**Important**: File must be encoded in your system default file format, e.g. ANSI for Windows and UTF-8 for Unix

either::

    00:00:00.000 Introduction
    00:02:00.000 Chapter Title
    00:42:24.123 Chapter Title

or (Audacity export format, separated by tab, contains 2x start time in seconds of the chapter)::

    0.000000	0.000000	Chapter 1
    85.180378	85.180378	Chapter 2
    543.822379	543.822379	Chapter 3 - spaces are allowed as you like

add chapter marks
-----------------
add (import) chapter marks from text file (unexpected results may occur if chapters already exist, for best results remove chapters first with -r)

``mp3chaps -i episode_42.mp3``

If you run into errors, try using ASCII. There have been some issue with Unicode.

list chapters
-------------

``mp3chaps -l episode_42.mp3``

remove chapters
---------------

``mp3chaps -r episode_42.mp3``
