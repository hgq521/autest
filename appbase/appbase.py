import sys
sys.path.append('E:\\pythontest\\tt\\autest') 

import uiautomator2 as u2

import time
from db.myrethinkdb import mydb
import mytime.mytime as timeutil

class app:
	
	def __init__(self, d, name, device):
		self.name = name
		self.d = d
		self.device = device
		self.tab_name = 'jdsc'

		self.next_refresh_time = 0
		self.last_time = 0



		self.db = mydb()
		self.db.connect()
		self.db.get_db('autest')

		pass

	def __del__(self):
		self.db.close()	

	
	def set_tab_name(self, tab_name):
		self.tab_name = tab_name

	
	def do_init(self):

		self.next_refresh_time = timeutil.today_hour(24)
		self.save()
		pass

	def has_task(self):
		print(self.name, "没有实现has_task")

		return True

	def load(self):
		tab = self.db.tab(self.tab_name)

		cur = tab.get(self.device).run()

		if cur == None:
			data = self.gen()
			data['id'] = self.device
			tab.insert(data).run()
			return

		print('load', self.name)
		
		return

	def	gen(self):
		data = {}
		print(self.name, "gen 未实现")
		return data

	def save(self):
		data = self.gen()
		tab = self.db.tab(self.tab_name)	
		cur = tab.get(self.device).update(data).run()
	
	def check_time(self, sec=600):
		if time.time() - self.last_time > sec:
			return True
		return False

	def set_time(self):
		self.last_time = time.time()

	
	def refresh(self):
		sec = time.time()
		if sec < self.next_refresh_time:
			return

		self.do_init()

	def run(self):
		print(self.name, '没有实现run方法')
		self.start_app()
		return True

	
	def start_app(self):
		print(self.name, "start_app")
		self.d.app_stop(self.name)
		self.d.app_start(self.name)
		return True


if __name__ == '__main__':
	serl = '66J5T19603005713'
	d = u2.connect(serl)
	pk = "com.jingdong.app.mall"
	tab = 'jdsc'
	tt = app(d, pk, serl)
	tt.set_tab_name(tab)
	tt.load()
	tt.run()
