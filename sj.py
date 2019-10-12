'''mobile'''
import uiautomator2 as u2
import time
import xk.xk as xiankan
import hs.hs as huoshan

class sj:
	
	def __init__(self, ip='', serl=''):
		self.ip = ip
		self.serl = serl
		self.pks = {} 
		self.apps = []
		self.d = {}
		pass

	def connect(self):
		if not (self.ip == ""):
			self.d = u2.connect(self.ip)
		else:
			self.d = u2.connect(self.serl)

	def add_app(self, pk_name, tab_name):
		self.pks[tab_name] = pk_name
		#self.pks.append(pk_name)

	def run(self):
		self.connect()
		self.init_app()
		self.loop()
		pass 


	def loop(self):
		while True:
			for app in self.apps:
				if (app.run()):
					self.apps.remove(app)
					print("shanc")
				time.sleep(2.0)
	
	def init_app(self):
		for tab, pk in self.pks.items():
			if (pk == "com.xiangkan.android"):
				app = xiankan.xk(self.d, pk, self.serl)
				app.set_tab_name(tab)
				app.load()
				self.apps.append(app)
				continue

			if (pk == "com.ss.android.ugc.livelite"):
				app = huoshan.hs(self.d, pk, self.serl)
				app.set_tab_name(tab)
				app.load()
				self.apps.append(app)
				continue

if __name__ == '__main__':
	mo = sj(serl='66J5T19603005713')
	mo.add_app("com.xiangkan.android")
	mo.add_app("com.ss.android.ugc.livelite")
	mo.run()
