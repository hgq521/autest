import sys
sys.path.append('E:\\pythontest\\tt\\autest') 

import uiautomator2 as u2

import time
from db.myrethinkdb import mydb
import mytime.mytime as timeutil


from appbase.appbase import app 

class jdmall(app):
	
	def __init__(self, d, name, device):
		super(jdmall, self).__init__(d, name,device)

	
	def run(self):
		pass
		



if __name__ == '__main__':

	serl = '66J5T19603005713'
	d = u2.connect(serl)
	pk = "com.jingdong.app.mall"
	tab = 'jdsc'
	jd = jdmall(d, pk, serl)
	jd.set_tab_name(tab)
	jd.load()
	jd.run()

