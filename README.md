# OpenCV_datamatrix
Some test with data matrix recognize

# Mission: 
Recognizing datamatrix codes from bottles moving along the conveyor
The camera stands statically. The lens is aimed at the conveyor. Bottles with a code glued to them move along the conveyor at different speeds at different times. The task is to recognize the bottle, first check whether there is a sticker with a code at all, and then check the code itself. If everything is in order, the bottle moves on. If not, the bottle must be removed from the tape.

# Useful links:

* https://github.com/NaturalHistoryMuseum/pylibdmtx - to decode datamatrix code
* https://en.wikipedia.org/wiki/Data_Matrix - more about datamatrix code
* https://docs.opencv.org/4.8.0/ - openCV docs

# Development plans:

* pylibdmtx - how it works, some test with real image
* openCV_part1 - image code recognition
* openCV_part2 - video code recognition

