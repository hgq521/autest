import uiautomator2 as u2
from uiautomator2.exceptions import (UiObjectNotFoundError,
									 UiautomatorQuitError)
import time
from db.myrethinkdb import mydb

def hailianshipin():
	ret = False
	#d.xpath('//*[@resource-id="app"]/android.view.View[8]').click()
	count = 0
	#d.watcher("quit_con").when(resourceId="com.ss.android.ugc.livelite:id/rl").click()
	for item in d(resourceId="app").child(className="android.view.View",clickable=True):
		count = count+1
		if (count >10):
			return False
		if item.child(className="android.view.View").count > 0:
			if item.child(className="android.view.View")[0].get_text() == "看视频赚海量金币":
				item.click()
				break

	if (d(text="关闭广告").wait(20.0)):
		print("guanbiguangg")
		d(text="关闭广告").click()
		time.sleep(1.0)
	else:
		print("超时")
		d.press("back")

	#if (d(className="android.widget.RelativeLayout",resourceId="com.ss.android.ugc.livelite:id/rl").wait(1.0)):
	#	d(className="android.widget.RelativeLayout",resourceId="com.ss.android.ugc.livelite:id/rl").click()
	#d(resourceId="com.ss.android.ugc.livelite:id/r_")
	if d.watchers.triggered:
		print("triggered")

	#d.watchers.remove("quit_con")
	#d.watchers.reset()
	
	return True

#开宝箱
def lb(d):
	d(resourceId="com.ss.android.ugc.livelite:id/lb").click()
	d(text="开宝箱得金币").click()
	coin_100 = "看视频 领100金币"
	coin_double = '看视频 领双倍金币'
	
	time.sleep(1.0)
	if not d(className="android.app.Dialog").wait(3.0):
		print("dialog not exists ")

		return
		
	ret = False
	for item in d(className="android.app.Dialog").child(text=coin_100):
		print("100 %s" %(item.get_text()))
		item.click()
		ret = True
		pass
	if not ret:
		for item in d(className="android.app.Dialog").child(text=coin_double):
			print("double %s" %(item.get_text()))
			item.click()
			ret = True



	#if (d(text="看视频 领100金币").wait(3.0)):
	#	d(text="看视频 领100金币").click()
	#elif (d(text='看视频 领双倍金币').wait(3.0)):
	#	d(text='看视频 领双倍金币').click()		
	#else:
	if not ret:
		print("开宝箱,未处理的情况")
		return


	if (d(text="关闭广告").wait(30.0)):
		print("guanbiguangg")
		d(text="关闭广告").click()
	else:
		print("开宝箱看视频 超时")
		d.press("back")


def start_app(pk_name):
	d.app_stop(pk_name)
	d.app_start(pk_name)



#click hongbao
#hongbao_btn = d(resourceId="com.ss.android.ugc.livelite:id/vr").child(className="android.widget.RelativeLayout")[1].info
def hongbao():
	d(text="红包", resourceId="com.ss.android.ugc.livelite:id/title").click()

	time.sleep(1.0)
	if (d(resourceId="com.ss.android.ugc.livelite:id/lb").wait(10.0)):
		lb_str = d(resourceId="com.ss.android.ugc.livelite:id/lb").get_text()
	else:
		print("未找到红包ui")
		return
	
	if (lb_str=="宝箱"):
		print("kaibaox")
		lb(d)

#签到
def sign():
	ret = False
	count = 0
	for item in d(resourceId="app").child(className="android.view.View",clickable=True):
		count = count+1
		if (count >5):
			return False
		if item.child(className="android.view.View").count > 0:
			text = item.child(className="android.view.View")[0].get_text()
			print(text)
			if text == "签到":
				item.click()
				ret = True
				break

	if not ret:
		return
	time.sleep(1.0)
	d(text="javascript:;").click()


#kanshipin
#time.sleep(1.0)
#if (d(text="看视频赚海量金币").wait(20.0)): 
	#shipin_str = d(text="看视频赚海量金币").down(className="android.view.View").get_text()
#	pass

def kan_hlsp():
	count = 0
	d.watcher("quit_con").when(resourceId="com.ss.android.ugc.livelite:id/rl").click()
	while True:
		if not hailianshipin():
			break
		time.sleep(1.0)
		count = count + 1
		print("count: ")
		print(count)
		if (count >= 18):
			break;

	d.watchers.remove("quit_con")

#shipin
def kan_sp():
	d(text="视频", resourceId="com.ss.android.ugc.livelite:id/title").click()
	count=0
	x, y = d(resourceId="com.ss.android.ugc.livelite:id/y9")[0].center()
	d.click(x,y)
	while True:
		count=count+1
		print("视频 %u 次"%(count))

		#抽奖
		if d.xpath('//*[@resource-id="com.ss.android.ugc.livelite:id/a2"]/android.widget.RelativeLayout[1]').wait(2.0):
			#todo	
			item = d.xpath('//*[@resource-id="com.ss.android.ugc.livelite:id/a2"]/android.widget.RelativeLayout[1]')
			x,y = item.center()
			d.click(x, y)
			
			time.sleep(6.0)
			d.swipe_ext("up", 0.5)
			print("抽奖")
			continue

		#免费领取
		if d.xpath('//*[@resource-id="com.ss.android.ugc.livelite:id/a2"]/android.widget.FrameLayout[1]').wait(2.0):
			
			child = d(resourceId="com.ss.android.ugc.livelite:id/a0k").child(resourceId="com.ss.android.ugc.livelite:id/l8")
			for item in child:
					time.sleep(10.0)
					d.swipe_ext("up",0.3)
					d.swipe_ext("down",0.3)
					time.sleep(5.0)
					item.click()
					time.sleep(1.0)

					tt.click()
					d.swipe_ext("up",0.3)
					print("免费领取")
					continue
					
				 

		#if (d.exists(resourceId="com.ss.android.ugc.livelite:id/a0r")):
		#	print("tt")
		#	time.sleep(10.0)
		#	d.swipe_ext("up",0.3)
		#	d.swipe_ext("down",0.3)
		#	time.sleep(5.0)
		#	d(resourceId="com.ss.android.ugc.livelite:id/l8").click()
		#	time.sleep(1.0)
		#d.swipe_ext("up",0.3)

		time.sleep(15.0)
		d.swipe_ext("up", 0.3)
		print("普通视频")

		#com.ss.android.ugc.livelite:id/a1s  zhuan

class hs:
	
	def __init__(self, d, name, device):
		self.name = name
		self.d = d

		self.signed = False
		self.last_time = 0
		self.last_lb_time = 0
		self.hlsp_over = False
		self.kan_sp_over = False
		self.next_refresh_time = 0

		self.db = mydb()
		self.db.connect()
		self.db.get_db("autest")
		self.tab_name = "hs"
		self.device = device

	def do_init(self):
		self.signed = False
		#self.last_time = 0
		#self.last_lb_time = 0
		self.hlsp_over = False
		self.kan_sp_over = False
		self.next_refresh_time = mytime.mytime.today_hour(24)
		self.save()


	def has_task(self):
		if not self.hlsp_over:
			return True
		if not self.kan_sp_over:
			return True

		sec = time.time()
		if (sec - self.last_lb_time) > 1800:
			return True

		return False

	def load(self):
		tab = self.db.tab(self.tab_name)
		
		cur = tab.get(self.device).run()
		if cur == None:
			data = self.gen()
			data['id'] = self.device
			tab.insert(data).run()
			return

		for item in cur:
			print("load")
			print(item)	
			self.signed = item['signed']
			self.last_time = item['last_time']
			self.last_lb_time = item['last_lb_time']
			self.hlsp_over = item['hlsp_over']
			self.kan_sp_over = item['kan_sp_over']
			self.next_refresh_time = item['next_refresh_time']
			return
		data = self.gen()
		data['id'] = self.device
		tab.insert(data).run()
	
	def gen(self):
		data = {}
		data['signed'] = self.signed
		data['last_time'] = self.last_time
		data['last_lb_time'] = self.last_lb_time
		data['hlsp_over'] = self.hlsp_over
		data['kan_sp_over'] = self.kan_sp_over
		data['next_refresh_time'] = self.next_refresh_time
		return data
		
	def save(self):
		data = self.gen()
		tab = self.db.tab(self.tab_name)	
		cur = tab.get(self.device).update(data).run()
			
		pass

	def check_time(self):
		if time.time() - self.last_time > 600:
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
		
		self.refresh()

		if not self.has_task():
			print("hs no task")
			return True
		self.set_time()
		print("set_time")
		if not self.start_app():
			return False


		#if not self.sign():
		#	print("sign return false")
		#	return False
		
		ret = False
		while True:
			if not self.hongbao():
				break

			print("hlsp")
			if not self.kan_hlsp():
				print("hlsp return false")
				break

			if not self.kan_sp():
				break

			ret = True
		self.d.app_stop(self.name)
		return ret

	def start_app(self):
		print("start_app")
		self.d.app_stop(self.name)
		self.d.app_start(self.name)
		return True

	def hongbao(self):
		d = self.d
		d(text="红包", resourceId="com.ss.android.ugc.livelite:id/title").click()

		time.sleep(1.0)
		#时间检测
		now_time = time.time()
		if (now_time - self.last_lb_time < 1800):
			return True
		
		if d(text="开宝箱得金币").wait(2.0):
			d(text="开宝箱得金币").click()
			self.lb()

		#if (d(resourceId="com.ss.android.ugc.livelite:id/lb").wait(10.0)):
		#	lb_str = d(resourceId="com.ss.android.ugc.livelite:id/lb").get_text()
		else:
			print("未找到红包ui")
			return True
	
		#if (lb_str=="宝箱"):
		#	print("kaibaox")
		#	self.lb()

		return True

	def lb(self):
		d = self.d

		#d(resourceId="com.ss.android.ugc.livelite:id/lb").click()
		#d(text="开宝箱得金币").click()
		coin_100 = "看视频 领100金币"
		coin_double = '看视频 领双倍金币'
	
		time.sleep(1.0)
		if not d(className="android.app.Dialog").wait(3.0):
			print("dialog not exists ")

			return
		
		ret = False
		for item in d(className="android.app.Dialog").child(text=coin_100):
			print("100 %s" %(item.get_text()))
			x,y = item.center()
			d.click(x, y)
			#item.click()
			ret = True
			pass
		if not ret:
			for item in d(className="android.app.Dialog").child(text=coin_double):
				print("double %s" %(item.get_text()))
				item.click()
				ret = True


		if not ret:
			print("开宝箱,未处理的情况")
			return


		self.last_lb_time = time.time()
		self.save()

		if (d(text="关闭广告").wait(60.0)):
			print("guanbiguangg")
			d(text="关闭广告").click()
		else:
			print("开宝箱看视频 超时")
			d.press("back")
			pass

	def sign(self):
		print("sign")
		if self.signed:
			return True
		
		d = self.d
		ret = False
		count = 0
		for item in d(resourceId="app").child(className="android.view.View",clickable=True):
			count = count+1
			if (count >5):
				return False
			if item.child(className="android.view.View").count > 0:
				text = item.child(className="android.view.View")[0].get_text()
				print(text)
				if text == "签到":
					item.click()
					ret = True
					break

		if not ret:
			return True
		time.sleep(1.0)
		d(text="javascript:;").click()
		self.signed = True
		self.save()

		return True

	def kan_hlsp(self):
		print("kan_hlsp 0")
		if self.hlsp_over:
			return True
		if self.check_time():
			print("kan_hlsp 1")
			return False

		print("kan_hlsp 2")
		d = self.d
		ret = False
		d.watcher("quit_con").when(resourceId="com.ss.android.ugc.livelite:id/rl").click()
		while True:
			if not self.hailianshipin():
				self.hlsp_over = True
				self.save()
				ret = True
				break
			time.sleep(1.0)
			if self.check_time():
				print("kan_hlsp 3")
				break

		d.watchers.remove("quit_con")

		return ret

	def hailianshipin(self):
		
		d = self.d
		ret = False
		count = 0
		for item in d(resourceId="app").child(className="android.view.View",clickable=True):
			count = count+1
			if (count >10):
				return False
			if item.child(className="android.view.View").count > 0:
				if item.child(className="android.view.View")[0].get_text() == "看视频赚海量金币":
					item.click()
					break

		if (d(text="关闭广告").wait(60.0)):
			print("guanbiguangg")
			d(text="关闭广告").click()
			time.sleep(1.0)
		else:
			print("超时")
			d.press("back")

		if d(resourceId="com.ss.android.ugc.livelite:id/r_").wait(1.0):
			d(resourceId="com.ss.android.ugc.livelite:id/r_").click()

		if d.watchers.triggered:
			print("triggered")

	
		return True
		
	def kan_sp(self):
		print("kan_sp")
		if self.kan_sp_over:
			return True
		
		d = self.d
		#d(text="视频", resourceId="com.ss.android.ugc.livelite:id/title").click()
		#x, y = d(resourceId="com.ss.android.ugc.livelite:id/y9")[0].center()
		#d.click(x,y)

		#tt = d.xpath('//*[@resource-id="app"]/android.view.View[6]')
		#text = ""
		#if tt.child(className="android.view.View")[0].wait(1.0):
		#	text = tt.child(className="android.view.View")[0].get_text()
		#else:
		#	self.kan_sp_over = True
		#	self.save()
		#	return True

		#if text.find("累积观看视频") == -1 :
		#	return True
		#tt.click()		
		
		ret = False
		for item in d(resourceId="app").child(className="android.widget.Image"):
			sli_tmp = {}
			count = 0
			for sli in item.sibling(className="android.view.View"):
				text = sli.get_text()
				print("search 累计观看",text)
				print(count)
				if count == 0:
					if (text.find("累积观看视频") != -1):
						ret = True
						count += 1
						sli_tmp = sli
						continue
					else:
						break
				elif count == 1:
					count += 1
					continue
				elif count == 2:
					print("tttt")
					if (text == "已完成"):
						ret = False
					break

			if ret:
				print("click")
				x, y = sli_tmp.center()
				d.click(x, y)
				break

		
		if not ret:
			self.kan_sp_over = True
			self.save()
			return True
		last_sec = time.time()
		while not self.check_time():

			#if self.check_sp_over():
			#	self.kan_sp_over = True
			#	self.save()
			#	break
			#抽奖
			if d.xpath('//*[@resource-id="com.ss.android.ugc.livelite:id/a2"]/android.widget.RelativeLayout[1]').wait(2.0):
				#todo	
				item = d.xpath('//*[@resource-id="com.ss.android.ugc.livelite:id/a2"]/android.widget.RelativeLayout[1]')
				x,y = item.center()
				d.click(x, y)
			
				time.sleep(6.0)
				d.swipe_ext("up", 0.5)
				print("抽奖")
				continue

			#免费领取
			if d(resourceId="com.ss.android.ugc.livelite:id/a0c").wait(2.0):
				get_btn = d(resourceId="com.ss.android.ugc.livelite:id/a0d")
				if "点击领取" == get_btn.get_text():
					d.swipe_ext('up', 0.3)
					d.swipe_ext('down', 0.3)
					time.sleep(1.0)
					get_btn = d(resourceId="com.ss.android.ugc.livelite:id/a0d")
					x, y = get_btn.center()
					d.click(x, y)
					d.swipe_ext('up', 0.3)
					last_sec = time.time()
					print("免费领取")
					continue
				else:
					if (time.time() - last_sec > 50):
						print("免费领取超时")
						last_sec = time.time()
						d.swipe_ext('up', 0.3)
						continue

					print("免费领取等待...")
					time.sleep(10.0)
					continue

			'''
			if d.xpath('//*[@resource-id="com.ss.android.ugc.livelite:id/a2"]/android.widget.FrameLayout[1]').wait(2.0):
			
				child = d(resourceId="com.ss.android.ugc.livelite:id/a0k").child(resourceId="com.ss.android.ugc.livelite:id/l8")
				for item in child:
					time.sleep(10.0)
					d.swipe_ext("up",0.3)
					d.swipe_ext("down",0.3)
					time.sleep(5.0)
					item.click()
					time.sleep(1.0)

					tt.click()
					d.swipe_ext("up",0.3)
					print("免费领取")
					continue
			'''		
				 

			now_sec = time.time()
			diff_sec = now_sec - last_sec
			if diff_sec > 15:
				last_sec = now_sec
			else:
				time.sleep(diff_sec - 15)
			d.swipe_ext("up", 0.3)
			print("普通视频")

		return self.kan_sp_over



if __name__ == '__main__':
	d = u2.connect('66J5T19603005713')
	#start_app("com.ss.android.ugc.livelite")
	#hongbao()
	#sign()
	#kan_hlsp()
	#kan_sp()
	tt = hs(d, "com.ss.android.ugc.livelite")
	print("xxx")
	tt.run()

		
