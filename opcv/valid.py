
import sys
sys.path.append('E:\\pythontest\\tt\\autest') 
import numpy as np
import argparse
import time
import copy
from logger.logger import Logger

import cv2
from matplotlib import pyplot
import os

'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
help="path to input image")

args = vars(ap.parse_args())

print(args['image'])
'''

def get_loc(img_gray, from_y, from_x, huidu):
	rows = img_gray.shape[0]
	cols = img_gray.shape[1]
	begin_x = rows//2
	begin_y = cols//2

	start_x = 0
	end_x = 0
	tmp = 0
	max_count = 0

	for y in range(rows):

		if y != from_y:
			continue
		count = 0
		for x in range(cols):
			if x < from_x:
				continue

			if (img_gray[y][x] < huidu):
				img_gray[y][x] = 0
				if (count == 0):
					tmp = x
				count += 1
			else:
				if (count > max_count):
					max_count = count
					start_x = tmp
					end_x = x-1
					
				'''
				if (count > 0):
					print("conttt count:")
					print(count)
				'''

				count = 0
				continue;
			
	#test
	'''
	print("startx endx %u %u, count %u" %(start_x, end_x, max_count))
	for y in range(20):
		tmp_y = from_y - 10 + y
		if img_gray[tmp_y,start_x]< huidu:
			img_gray[tmp_y,start_x] = 0

		if img_gray[tmp_y, end_x] < huidu:
			img_gray[tmp_y, end_x] = 0

		loc = (start_x + end_x) // 2
		if (img_gray[tmp_y, loc] < huidu):
			img_gray[tmp_y, loc] = 0
	#print(img_gray)
	cv2.imshow('img3',img_gray)
	cv2.waitKey(0)
	print("xxxxxxxxxxxxxxxxx %u"% (from_y))
	'''
	return start_x, end_x, max_count

def try_get_loc(img_gray, huidu):
	start_x = 0
	end_x = 0
	max_count = 0
	from_y = 500
	ret = False
	big_count = 0
	small_count = 0
	for i in range(10):
		start_x, end_x, max_count = get_loc(img_gray, from_y, 140, huidu)
		#print("got x( %u, %u, %u, %u, %u)" %(start_x, end_x, max_count, i, huidu))
		#cv2.waitKey(0)
		if (max_count > 127 and max_count < 133):
			ret = True
			break
		if (max_count > 133):
			big_count += 1
		else:
			small_count += 1
		from_y+=10
	if ret:	
		return ret, start_x, end_x

	return ret, big_count, small_count
		
def find_slot(file_name):
	imgobj1 = cv2.imread(file_name)
	huidu=150
	step = 50
	ret = False
	start_x, end_x = 0, 0
	for i in range(3):
		img_gray = cv2.cvtColor(imgobj1,cv2.COLOR_BGR2GRAY)
		ret,start_x, end_x = try_get_loc(img_gray, huidu) # True start_x,end_x; False big_count, small_count
		if (ret):
			break
		
		if start_x > end_x:
			huidu -= step
		else:
			huidu += step
	

	cv2.destroyAllWindows()
	return ret,start_x, end_x

if __name__ == '__main__':
	
	tt = Logger().get_log
	#dpath = 'sshot/data/'
	dpath = '../'

	#files = os.listdir(dpath)
	files = []
	files.append('p20191113_173904.png')

	for file_name in files:
		print("xxxxxxxx:"+file_name)
		ret, start_x, end_x = find_slot(dpath+file_name)
		if (ret):
			tt.error("%s final got start_x %u, end_x %u " %(file_name,start_x, end_x))
		else:
			tt.error("%s not found", file_name)
		break
