import sys
sys.path.append('E:\\pythontest\\tt\\autest') 
import uiautomator2 as u2
from uiautomator2.exceptions import (UiObjectNotFoundError,
									 UiautomatorQuitError)

import time
from db.myrethinkdb import mydb
import mytime.mytime as timeutil

def start_app(pk_name):
	d.app_stop(pk_name)
	d.app_start(pk_name)



#click hongbao
#hongbao_btn = d(resourceId="com.ss.android.ugc.livelite:id/vr").child(className="android.widget.RelativeLayout")[1].info


def t2s(t):
	m="0"
	s="0"
	m,s = t.strip().split(":")
	if m=="":
		m="0"
	if s=="":
		s="0"
	return int(m)*60 + int(s)

class xk:
	
	fudai_interval = 0,5,10,30,60,90
	def __init__(self,d, name, device):
		self.name = name
		self.d = d

		self.last_time = 0
		self.last_coin = 0
		self.signed = False
		self.wenzhang_over = False
		self.shipin_over = False
		self.fudai_time = 0
		self.fudai_count = 0
		self.weiguan_over = False
		self.next_refresh_time = 0

		self.tab_name = 'xk'
		self.db = mydb()
		self.db.connect()
		self.db.get_db("autest")
		self.device = device
		self.is_friday = False

	def set_tab_name(self, tab_name):
		self.tab_name = tab_name

	def __del__(self):
		self.db.close()
		pass

	def do_init(self):
		#self.last_time = 0
		#self.last_coin = 0
		self.signed = False
		self.wenzhang_over = False
		self.shipin_over = False
		self.fudai_time = 0
		self.fudai_count = 0
		self.weiguan_over = False
		self.next_refresh_time = timeutil.today_hour(24)
		self.save()
		if timeutil.wday(time.time()) == 5:
			self.is_friday = True
		else:
			self.is_friday = False

		#self.is_friday = False

	def load(self):
		print(self.tab_name,"load")

		if timeutil.wday(time.time()) == 5:
			self.is_friday = True
		else:
			self.is_friday = False

		tab = self.db.tab(self.tab_name)

		cur = tab.get(self.device).run()
		if cur == None:
			data = self.gen()
			data['id'] = self.device
			tab.insert(data).run()
			return

		print(cur)

		self.last_time = cur['last_time']
		self.last_coin = cur['last_coin']
		self.signed = cur['signed']
		self.wenzhang_over = cur['wenzhang_over']
		self.shipin_over = cur['shipin_over']
		self.fudai_time = cur['fudai_time']
		self.fudai_count = cur['fudai_count']
		self.next_refresh_time = cur['next_refresh_time']
		if ('weiguan_over' in cur):
			self.weiguan_over = cur['weiguan_over']

	def gen(self):
		data = {}

		data['last_time'] = self.last_time
		data['last_coin'] = self.last_coin
		data['signed'] = self.signed
		data['wenzhang_over'] = self.wenzhang_over
		data['shipin_over'] = self.shipin_over
		data['fudai_time'] = self.fudai_time
		data['fudai_count'] = self.fudai_count
		data['weiguan_over'] = self.weiguan_over
		data['next_refresh_time'] = self.next_refresh_time
		return data
		
		

	@classmethod
	def get_fudai_interval(xk, count):
		if count < len(xk.fudai_interval):
			return xk.fudai_interval[count]
		return 10000

	@classmethod
	def get_fudai_max(xk):
		return len(xk.fudai_interval)	

	def save(self):
		data = self.gen()
		tab = self.db.tab(self.tab_name)	
		cur = tab.get(self.device).update(data).run()
		pass

	def check_time(self):
		'''
		if time.time() - self.last_time > 600:
			return True
		return False
		'''
		return False
	
	def set_time(self):
		self.last_time = time.time()
	
	def refresh(self):
		sec = time.time()
		if sec < self.next_refresh_time:
			return

		self.do_init()
		pass
	
	def has_task(self):
		if self.check_time_award():
			return True

		if not self.wenzhang_over:
			return True

		if not self.shipin_over:
			return True
			
		return False

	def run(self):
		'''
		self.refresh()

		if not self.has_task():
			print("xk no task")
			return True

		self.set_time()

		if not self.start_app():
			return False

		ret = False
		self.d.watcher("readmore").when(resourceId="com.xiangkan.android:id/more_minute_btn").click()
		'''
		while True:
			
			'''
			if not self.sign():
				break
			if not self.time_award():
				break
			'''
			
			if not self.wenzhang():
				break	
			'''
			if not self.shipin():
				break

			if not self.weiguan():
				break

			'''
			ret = True
			break

		self.d.watchers.remove("readmore")
		#self.d.app_stop(self.name)
	
	def start_app(self):
		self.d.app_stop(self.name)
		self.d.app_start(self.name)
		return True

	def sign(self):
		if self.signed:
			return True

		d = self.d
		if (d(resourceId="com.xiangkan.android:id/tv_box_hint").wait(2.0)):
			text = d(resourceId="com.xiangkan.android:id/tv_box_hint").get_text()
			if (text == "已签"):
				print(text)
				return True
		sign_btn = d(resourceId="com.xiangkan.android:id/custom_sign_box")
		sign_btn.click()
		self.signed = True
		self.save()
		return True
	def check_time_award(self):
		sec = time.time()

		if sec - self.last_coin < timeutil.hour_sec():
			return False

		return True

	def time_award(self):
		d = self.d
		if not self.check_time_award():
			return True
		
		if (d(resourceId="com.xiangkan.android:id/tv_box_time_new").wait(2.0)):
			try:
				text = d(resourceId="com.xiangkan.android:id/tv_box_time_new").get_text()
			except UiObjectNotFoundError:
				print("time_award: UiObjectNotFoundError")
				return True

			print("time_award:",text)
			if (text != "领金币"):
				return True

		d(resourceId="com.xiangkan.android:id/custom_integer_coin_box").click()
		sec = time.time()
		self.last_coin = timeutil.hour(sec) #取到小时
		#self.last_coin = sec
		self.save()
		return True

	def find_wenzhang(self):
		tv_text = "阅读文章 30 秒"
		if (self.is_friday):
			#tv_text = "阅读文章0.5分钟(圆圈转1圈)"
			tv_text = "阅读文章30秒"

		return self.find_text(tv_text)

	def find_weiguan(self):
		tv_text = "在围观内观看小视频5分钟"
		return self.find_text(tv_text)

	def find_text(self, tv_text):
		d = self.d
		time.sleep(1.0)
		d.swipe_ext('down', 0.5)
		for x in range(1,3):
			for title_tv in d(resourceId="com.xiangkan.android:id/title_tv"):
				text = title_tv.get_text()
				print(text)
				if not (text == tv_text):
					continue
				if title_tv.sibling(resourceId="com.xiangkan.android:id/status_fl")[0].wait(1.0):
					pass
				else:
					continue

				if title_tv.sibling(resourceId="com.xiangkan.android:id/status_fl")[0].child(className="android.widget.TextView")[0].wait(1.0):
					pass
				else:
					continue

				tt = title_tv.sibling(resourceId="com.xiangkan.android:id/status_fl")[0].child(className="android.widget.TextView")[0].get_text()
				if tt == "已完成":
					return False, {}
				else:
					return True, title_tv
			
			print("not found", tv_text)
			d.swipe_ext('up', 0.3)
			time.sleep(0.5)
			
		return False, {}
	def find_shipin(self):
		tv_text = "观看视频 1 分钟"
		if (self.is_friday):
			#tv_text = "观看视频1分钟(圆圈转1圈)"
			tv_text = "观看视频1分钟"
		
		return self.find_text(tv_text)
	
	def towode(self):
		d = self.d
		print("towode")
		for i in range(1, 3):
			if d(resourceId="com.xiangkan.android:id/tv_tab_title", text="我的").wait(1.0):
				#x, y = d(resourceId="com.xiangkan.android:id/tv_tab_title", text="我的").center()
				x, y = d(resourceId="com.xiangkan.android:id/tv_tab_title", text="我的").\
				sibling(resourceId="com.xiangkan.android:id/tab_icon").center()
				d.click(x, y)
				print("towode ok")
				return True
			else:
				d.press('back')

			time.sleep(0.5)

		print("towode failed")
		return False

		pass

	def wenzhang(self):

		d = self.d

		'''
		if (self.wenzhang_over):
			return True

		if not self.towode():
			return True

		ret, title_tv = self.find_wenzhang()


		if not ret:
			self.wenzhang_over = True
			self.save()
			return True

		time.sleep(2.0)


		#x, y = d(resourceId="com.xiangkan.android:id/title_tv", text=tv_text).center()
		x, y = title_tv.center()
		d.click(x,y)

		'''
		for i in range(1,1000):
			print("wenzhang 0")
			self.each_wenzhang();
			time.sleep(1.0)

			print("wenzhang 1")
			d.swipe_ext("up",0.5)
			time.sleep(4.0)
			if (self.check_time()):
				return False

	def each_wenzhang(self):
		d = self.d
		try:
			infos = d(resourceId="com.yuncheapp.android.pearl:id/root").child(resourceId="com.yuncheapp.android.pearl:id/title")
		except UiObjectNotFoundError:
			self.toshouye()
			print("tiaoquguangaole")
			return
			pass
		print("each_wenzhang")
		for item in infos:
			'''
			text = item.get_text()
		
			print(text)
			if (text.find("广告") != -1):
				continue
			time.sleep(1.0)
			tvtitle = item.sibling(resourceId="com.xiangkan.android:id/tvTitle")
			'''
			try:
				x,y = item.center()
			except UiObjectNotFoundError:
				print("tvTitle not found")
				continue

			d.click(x, y)
			self.onewenzhang()

	def onewenzhang(self):
		d = self.d
		cur = time.time()

		d.swipe_ext("down",0.2)
		d.swipe_ext("up",0.2)
		print('onewenzhang duration')
		#if d(resourceId="com.xiangkan.android:id/video_item_duration").wait(2.0):
		#	self.toshouye()
		#	print('is video return')
		#	return

		for x in range(1,20):
			print("onewenzhang");
			d.swipe_ext("down",0.2)
			d.swipe_ext("up",0.2)
			time.sleep(5.0)
			dur = time.time()-cur
			if dur > 40.0:
				print("dur is %f"%(dur))	
				break
		
		#self.fudai()	
		self.toshouye()

	def toshouye(self):
		d = self.d
		for i in range(1,3):
			d.press("back");
			if d(resourceId="com.yuncheapp.android.pearl:id/tab_tv", text="首页").wait(1.0):
				print("shouye")
				break

	def fudai(self):
		if self.fudai_count >= xk.get_fudai_max():
			return
		interval = xk.get_fudai_interval(self.fudai_count)
		if interval == 10000:
			return
			
		if not (time.time() - self.fudai_time > interval*60):
			return
		#时间检测	
		d = self.d
		if not d(resourceId="com.xiangkan.android:id/fudai_icon").exists():
			return

		x, y = d(resourceId="com.xiangkan.android:id/fudai_icon").center()
		d.click(x, y)
		if self.fudai_count == 0:
			self.fudai_time = time.time()
		self.fudai_count += 1
		self.save()

	def check_no_award(self):
		d = self.d
		cion = d(resourceId="com.xiangkan.android:id/coin_bubble_layout").child(className="android.widget.TextView")
		for item in cion:
			if item.get_text() == "本篇奖励已达上限":
				return True
	
		return False

	def shipin(self):
		ret = False
		if self.shipin_over:
			return True

		if not self.towode():
			return False

		d = self.d
		#d.swipe_ext("down",0.9)
		'''
		#tv_text = "观看视频 1 分钟"
		tv_text = "观看视频1分钟(圆圈转1圈)"
		for x in range(1,3):
			if d(resourceId="com.xiangkan.android:id/title_tv", text=tv_text).wait(1.0):
				print("shipin")
				ret = True
				break

			print("找不到 %s"%(tv_text))
			d.swipe_ext("up",0.3)
		'''
		
		ret, title_tv = self.find_shipin()

		if not ret:
			self.shipin_over = True
			self.save()
			return True
		time.sleep(1.0)
		#x, y = d(resourceId="com.xiangkan.android:id/title_tv", text=tv_text).center()

		x, y = title_tv.center()
		d.click(x,y)

		time.sleep(1.0)
		d.swipe_ext('up',0.5)
		d.swipe_ext('up',0.5)
		d.swipe_ext('up',0.5)
		time.sleep(2.0)
		for i in range(1,1000):
			self.each_shipin();
			time.sleep(1.0)
			d.swipe_ext("up",0.5)
			time.sleep(1.0)
			if self.check_time():
				return False
	
	def each_shipin(self):
		d = self.d	
		infos = d(resourceId="com.xiangkan.android:id/common_recycler_view").child(resourceId="com.xiangkan.android:id/video_layout")

		for item in infos:
			print("xx")
			try:
				x, y = item.center()
				d.click(x, y)
			except UiObjectNotFoundError:
				print("uiautomator2.exceptions.UiObjectNotFoundError")
				continue

			self.oneshipin()

	def oneshipin(self):
		now_sec = time.time()
		d = self.d
		if not (d(resourceId="com.xiangkan.android:id/ringProgressBar").wait(2.0)):
			self.toshiping()
			return
		dur_sec = t2s(d(resourceId="com.xiangkan.android:id/video_item_duration").get_text())
		#totest
		d.watcher("restart").when(resourceId="com.xiangkan.android:id/player_compete_restart").click()
		for x in range(1,20):
			if time.time() - now_sec > 160:	
				break
			time.sleep(5.0)
	
		d.watchers.remove("restart")
		self.toshiping()
	
	def toshiping(self):
		self.toshouye()


	def weiguan(self):
		if self.weiguan_over:
			return True

		#我的

		if not self.towode():
			return False
			
		time.sleep(1.0)

		d = self.d
		d.swipe_ext('down', 0.9)

		ret, title_tv = self.find_weiguan()

		if not ret:
			self.weiguan_over = True
			self.save()
			return True

		time.sleep(1.0)
		x, y = title_tv.center()
		d.click(x, y)
		for i in range(1, 60):
			time.sleep(10.0)
			d.swipe_ext('up', 0.3)
			if self.check_time():
				ret = False
				break
		
		d.press("back")
		return ret
	
	def qunhongbao(self):
		d = self.d
		if not d(resourceId="com.xiangkan.android:id/iv_redpacket").wait(2.0):
			return True

		
		if not d(resourceId="com.xiangkan.android:id/iv_msg_count").wait(2.0):
			return True

		if d(resourceId="com.xiangkan.android:id/iv_msg_count").get_text() == "":
			return True

		x, y =  d(resourceId="com.xiangkan.android:id/iv_redpacket").center()
		d.click(x, y)

		'''
		if d(resourceId='com.xiangkan.android:id/tab_icon')[2].wait(1.0):
			x, y = d(resourceId='com.xiangkan.android:id/tab_icon')[2].center()
			d.click(x, y)
			pass
		'''
		
		ret = False
		for tv_name in d(resourceId='com.xiangkan.android:id/tv_name'):
			text = tv_name.get_text()
			if text.find('小分队'):
				x, y = tv_name.center()
				d.click(x, y)
				ret = True
				break

		if not ret:
			print('没有找到小分队')
			return True
		print('进入领取群红包')
		for i in range(1,5):
			ret = False
			for item in d(resourceId='com.xiangkan.android:id/layout_packet'):
				ret = False
				for text in item.child(className='android.widget.TextView'):
					if text.get_text() == '点击领取':
						print('领取群红包 ')
						ret = True
						break
			
				if ret:
					item.click()

					d(resourceId="com.xiangkan.android:id/iv_open_result").wait(2.0).click()
					time.sleep(3.0)
					#d.press('back')
					print('返回上一层')

			if not ret:
				break

			d.swipe_ext('up', 0.3)
			time.sleep(0.5)
			

		d.press('back')
		print('领取完毕，返回')


		return True


if __name__ == '__main__':
	serl = '66J5T19603005713'
	d = u2.connect('66J5T19603005713')
	#start_app("com.xiangkan.android")
	#sign()
	#time_award()
	#wode()
	#wenzhang()
	#shipin()
	tt = xk(d, "com.yuncheapp.android.pearl", serl)
	print("xxx")
	#tt.set_tab_name(tab)
	tt.load()
	while True:
		tt.run()
		time.sleep(1.0)
