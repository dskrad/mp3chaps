mp3chaps
========

commandline utility for adding chapter marks to mp3 files similar to ``mp4chaps`` utility

many pocast apps on Android and iOS support chapter markers in both mp4 (aac) and mp3 files

this utilizes the excellent `eyeD3 <https://github.com/nicfit/eyeD3>`_ tagging module to read and write chapter frames and title subframes

installation
------------

``pip install mp3chaps``

usage
-----

assuming you have a file named ``episode_42.mp3``, ``mp3chaps.py`` looks for a chapter marks file called ``episode_42.chapters.txt`` in the same directory:

``00:00:00.000 Introduction
00:02:00.000 Chapter Title
00:42:24.123 Chapter Title``

add chapter marks
-----------------

``mp3chaps.py -i episode_42.mp3``

list chapters
-------------

``mp3chaps.py -l episode_42.mp3``

remove chapters
---------------

``mp3chaps.py -r episode_42.mp3``
