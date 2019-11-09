import sys
sys.path.append('E:\\pythontest\\tt\\autest') 

import uiautomator2 as u2

import time
from db.myrethinkdb import mydb
import mytime.mytime as timeutil

from appbase.appbase import app 
import random

class ks(app):
	def __init__(self, d, name, device):
		super(ks, self).__init__(d, name, device)

	def run(self):
		d = self.d
		#self.start_app()
		up = True
		d.screenshot(".\p2.png");

if __name__ == '__main__':
	serl = '66J5T19603005713'
	d = u2.connect(serl)
	pk = "com.kuaishou.nebula"
	tab = 'ks'
	jd = ks(d, pk, serl)
	jd.set_tab_name(tab)
	#jd.load()
	jd.run()
