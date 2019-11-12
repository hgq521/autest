import numpy as np
import argparse
import time
import copy

import cv2
from matplotlib import pyplot

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
help="path to input image")

args = vars(ap.parse_args())

print(args['image'])

if __name__ == '__main__':
	imgobj1 = cv2.imread('../sshot/p2.png')
	imgobj2 = cv2.imread('../sshot/2.png')
	gray1 = cv2.cvtColor(imgobj1,cv2.COLOR_BGR2GRAY)
	ret, im_fixed = cv2.threshold(gray1, 70, 255, cv2.THRESH_BINARY)

	for item in gray1:	
		print(item)

	#cv2.imshow('img1', im_fixed)

	rows = imgobj1.shape[0]
	cols = imgobj1.shape[1]
	cover = copy.deepcopy(gray1)

	for i in range(rows):
		for j in range(cols):
			cover[i][j] = 255-cover[i][j]

	#cv2.imshow('img3',cover)
	cv2.waitKey(0)


