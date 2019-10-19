import sys
sys.path.append('E:\\pythontest\\tt\\autest') 

import uiautomator2 as u2

import time
from db.myrethinkdb import mydb
import mytime.mytime as timeutil

from appbase.appbase import app 
import random

class dy(app):
	def __init__(self, d, name, device):
		super(dy, self).__init__(d, name, device)

	def run(self):
		d = self.d
		#self.start_app()
		up = True
		while (True):
			time.sleep(1.0)
			per = random.randint(1,10)
			sw = 'down'
			#if per < 7:
			if up:
				sw = 'up'
			if d(resourceId="com.ss.android.ugc.aweme.lite:id/ajf").wait(2.0):
				sec_str = time.asctime(time.localtime(time.time()))
				print(sec_str, "success")
				time.sleep(per+2.0)
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
	pk = "com.ss.android.ugc.aweme.lite"
	tab = 'dy'
	jd = dy(d, pk, serl)
	jd.set_tab_name(tab)
	#jd.load()
	jd.run()
