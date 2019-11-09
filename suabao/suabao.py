import sys
sys.path.append('E:\\pythontest\\tt\\autest') 

import uiautomator2 as u2

import time
from db.myrethinkdb import mydb
import mytime.mytime as timeutil

from appbase.appbase import app 
import random

class suabao(app):
	def __init__(self, d, name, device):
		super(suabao, self).__init__(d, name, device)

	def run(self):
		d = self.d
		#self.start_app()
		up = True
		while (True):
			toast_msg = d.toast.get_message(1.0, 10.0, "no toast message")
			print(toast_msg)
			per = random.randint(1,10)
			sw = 'down'
			#if per < 7:
			if up:
				sw = 'up'
			if True:#d(resourceId="com.kuaishou.nebula:id/red_packet").wait(2.0):
				sec_str = time.asctime(time.localtime(time.time()))
				print(sec_str, "success")
				#time.sleep(per+5.0)
				time.sleep(18.0)
			else:
				sec_str = time.asctime(time.localtime(time.time()))
				print(sec_str, 'no red_packet')

			print(sw)

			d.swipe_ext(sw, 0.5)
			#up = not up
			
		pass


if __name__ == '__main__':
	serl = '66J5T19603005713'
	d = u2.connect(serl)
	pk = "com.kuaishou.nebula"
	tab = 'ks'
	jd = suabao(d, pk, serl)
	jd.set_tab_name(tab)
	#jd.load()
	jd.run()
