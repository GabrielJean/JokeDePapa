#!/bin/python3.6
import os
from random import *

while True:
	audio = os.listdir("Audio")
	nb_len = len(audio)
	print(nb_len)
	audiofile = randint(0, nb_len - 1)
	print(audiofile)
	print(audio[audiofile])
