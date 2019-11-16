import sys
sys.path.append('E:\\pythontest\\tt\\autest') 

import uiautomator2 as u2

import threading
import time
from db.myrethinkdb import mydb
import mytime.mytime as timeutil

from appbase.appbase import app 
import random
from thread.mythread import MyThread

import va as Va

class ks(app):
	def __init__(self, d, name, device):
		super(ks, self).__init__(d, name, device)

	def run(self, lock):
		d = self.d
		#self.start_app()
		up = True
		while (True):
			toast_msg = d.toast.get_message(1.0, 10.0, "no toast message")
			print(toast_msg)
			per = random.randint(2,4)
			sw = 'down'
			#if per < 7:
			if up:
				sw = 'up'
			if True: #d(resourceId="com.kuaishou.nebula:id/red_packet").wait(2.0):
				sec_str = time.asctime(time.localtime(time.time()))
				print(sec_str, "success")
				time.sleep(per)
			else:
				sec_str = time.asctime(time.localtime(time.time()))
				print(sec_str, 'no red_packet')

			print(sw)

			lock.acquire()
			print("ks lock")
			d.swipe_ext(sw, 0.5)
			lock.release()
			print("ks unlock")
			up = not up
			
		pass


if __name__ == '__main__':
	serl = '66J5T19603005713'
	d = u2.connect(serl)
	pk = "com.kuaishou.nebula"
	tab = 'ks'
	jd = ks(d, pk, serl)
	jd.set_tab_name(tab)
	#jd.load()
	#jd.run()

	'''
	test
	'''

	tt = Va.va(d, pk, serl) 
	
	threadLock = threading.Lock()
	threads = []

	thread1 = MyThread(1, "t1", 5, jd.run, threadLock)
	thread2 = MyThread(2, "t2", 5, tt.run, threadLock)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

