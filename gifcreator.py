#	GifCreator
#	Simple script that takes a number of pictures in a file and puts them together into an animated GIF
#	Restriction: Make sure the pictures are all roughly the same resolution otherwise the results will be wonky
#	Yahya Ismail
#	11/9/2017

import imageio
import os, os.path

imageURI = raw_input("Where are your pictures located?")

staticImages = []

for filename in os.listdir(imageURI):
	staticImages.append(imageio.imread(imageURI+'\\'+filename))
	print('reading:' + filename)

print(staticImages[0])
	
writerKwargs = {'duration': '0.5'}
imageWriter = imageio.get_writer(imageURI+'\\'+'AnimatedGif.gif', 'GIF', 'I', **writerKwargs)

for image in staticImages:
	imageWriter.append_data(image)

imageWriter.close()