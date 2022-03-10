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

The chapter markers could be in either timecode or millisecond format

assuming you have a file named ``episode_42.mp3``, ``mp3chaps`` looks for a chapter marks file called ``episode_42.chapters.txt`` in the same directory::

``    00:00:00.000 Introduction``
``    00:02:00.000 Chapter Title``
``    00:42:24.123 Chapter Title``

``    00000000 Introduction``
``    00060000 Chapter Title``
``    00276123 Chapter Title``

add chapter marks
-----------------
add (import) chapter marks from text file (unexpected results may occur if chapters already exist, for best results remove chapters first with -r)

``mp3chaps -i episode_42.mp3``

list chapters
-------------

``mp3chaps -l episode_42.mp3``

remove chapters
---------------

``mp3chaps -r episode_42.mp3``

list chapters details
-------------

``mp3chaps -p episode_42.mp3``

Export chapters with timecode markers to <filename>.chaps.txt
---------------

``mp3chaps -e=tc episode_42.mp3``

Export chapters with milliseconds markers to <filename>.chaps.txt
---------------

``mp3chaps -e=mi episode_42.mp3``

Add test chapters marks
-------------

``mp3chaps -p episode_42.mp3``

---------------
