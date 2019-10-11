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

#签到
def sign():
	if (d(resourceId="com.xiangkan.android:id/tv_box_hint").wait(2.0)):
		text = d(resourceId="com.xiangkan.android:id/tv_box_hint").get_text()
		if (text == "已签"):
			print(text)
			return
	sign_btn = d(resourceId="com.xiangkan.android:id/custom_sign_box")
	sign_btn.click()

def time_award():
	if (d(resourceId="com.xiangkan.android:id/tv_box_time_new").wait(2.0)):
		text = d(resourceId="com.xiangkan.android:id/tv_box_time_new").get_text()
		print(text)
		if (text != "领金币"):
			return

	d(resourceId="com.xiangkan.android:id/custom_integer_coin_box").click()



#我的	
def wode():
	x,y = d(resourceId="com.xiangkan.android:id/tv_tab_title", text="我的").sibling(resourceId="com.xiangkan.android:id/tab_icon").center()
	print(x)
	print(y)
	d.click(x,y)

#阅读文章0.5分钟(圆圈转1圈
def wenzhang():
	ret = False

	tv_text = "阅读文章 30 秒"
	#tv_text = "阅读文章0.5分钟(圆圈转1圈)"
	for x in range(1,3):
		title_tv_res_id = "com.xiangkan.android:id/title_tv"
		if (d(resourceId=title_tv_res_id, text=tv_text).wait(1.0)):
			print("找到了")
			stats_res_id = "com.xiangkan.android:id/status_fl"
			stats_btn_res_id = "com.xiangkan.android:id/status_btn"
			status = d(resourceId = title_tv_res_id, text=tv_text).sibling(resourceId=stats_res_id)

			ret = True
			for item in status:
				status_btn = item.child(resourceId="stats_btn_res_id")

				for tt in status_btn:
					text = tt.get_text()
					if text == "已完成":
						print(text)
						ret = False

			break

		print("%s %u" %(tv_text, x))
		d.swipe_ext("up",0.3)
	if not ret:
		return

	time.sleep(2.0)
	x, y = d(resourceId="com.xiangkan.android:id/title_tv", text=tv_text).center()
	d.click(x,y)

	for i in range(1,20):
		each_wenzhang();
		time.sleep(1.0)

		d.swipe_ext("up",0.5)
		time.sleep(4.0)

def each_wenzhang():
	infos = d(resourceId="com.xiangkan.android:id/common_recycler_view").child(resourceId="com.xiangkan.android:id/tvInfo")
	#print(infos.info)
	for item in infos:
		print("tt")
		text = item.get_text()
		
		print(text)
		if (text.find("广告") != -1):
			print("sssst")
			continue
		#elif (text.find("")):
		#	continue
		time.sleep(1.0)
		tvtitle = item.sibling(resourceId="com.xiangkan.android:id/tvTitle")
		x,y = tvtitle.center()
		print("x,y %u %u" %(x,y))
		d.click(x, y)
		onewenzhang()

def onewenzhang():
	#if d(resourceId="com.xiangkan.android:id/bubble_text").wait(1.0):
	#	text = d(resourceId="com.xiangkan.android:id/bubble_text").get_text()
	#	print(text)
	#	if text == "本篇奖励已达上限":
	#		print("back")
	#		d.press("back")
	#		return

	print("onewenzhang2")
	if not (d(resourceId="com.xiangkan.android:id/ringProgressBar").wait(2.0)):
		print("meiyoujiangli")
		#d.press("back")
		toshouye()
		return
	
	if check_no_award():
		toshouye()
		return
	cur = time.time()
	print("onewenzhang3")
	for x in range(1,20):
		d.swipe_ext("down",0.2)
		d.swipe_ext("up",0.2)
		time.sleep(5.0)
		dur = time.time()-cur
		if dur > 95.0:
			print("dur is %f"%(dur))	
			break
		
		#if check_no_award():
		#	break
		#print(d(resourceId="com.xiangkan.android:id/ringProgressBar").info)

	fudai()	
	#if d.watcher("AUTO_FC_WHEN_ANR").triggered:
	#	print("treed")
	
	#d.press("back")
	toshouye()
def check_no_award():
	cion = d(resourceId="com.xiangkan.android:id/coin_bubble_layout").child(className="android.widget.TextView")
	for item in cion:
		if item.get_text() == "本篇奖励已达上限":
			return True
			print("no award")
	
	return False

def toshouye():
	#d.watcher("AUTO_FC_WHEN_ANR").remove()
	for i in range(1,3):
		d.press("back");
		if d(resourceId="com.xiangkan.android:id/tv_tab_title", text="首页").wait(1.0):
			print("shouye")
			break
	
def fudai():
	if not d(resourceId="com.xiangkan.android:id/fudai_icon").exists():
		return

	print("开福袋")
	x, y = d(resourceId="com.xiangkan.android:id/fudai_icon").center()
	d.click(x, y)
		
#观看视频1分钟
def shipin():
	ret = False
	d.swipe_ext("down",0.9)
	tv_text = "观看视频 1 分钟"
	#tv_text = "观看视频1分钟(圆圈转1圈)"
	for x in range(1,3):
		if d(resourceId="com.xiangkan.android:id/title_tv", text=tv_text).wait(1.0):
			print("shipin")
			ret = True
			break

		print("找不到 %s"%(tv_text))
		d.swipe_ext("up",0.3)

	if not ret:
		return
	time.sleep(1.0)
	x, y = d(resourceId="com.xiangkan.android:id/title_tv", text=tv_text).center()
	d.click(x,y)

	for i in range(1,5):
		each_shipin();
		time.sleep(1.0)
		d.swipe_ext("up",0.5)
		time.sleep(4.0)

def each_shipin():
	infos = d(resourceId="com.xiangkan.android:id/common_recycler_view").child(resourceId="com.xiangkan.android:id/video_layout")

	for item in infos:
		print("xx")
		x, y = item.center()
		d.click(x, y)

		oneshipin()

def oneshipin():
	if not (d(resourceId="com.xiangkan.android:id/ringProgressBar").wait(2.0)):
		print("wujiangli")
		toshiping()
		return
	dur_sec = t2s(d(resourceId="com.xiangkan.android:id/video_item_duration").get_text())
	last_sec = 0
	for x in range(1,20):
		play_sec = t2s(d(resourceId="com.xiangkan.android:id/player_time").get_text())

		if last_sec == play_sec:
			d(resourceId="com.xiangkan.android:id/video_item_play_btn").click()
		last_sec = play_sec
		if (dur_sec < 185):
			if dur_sec - play_sec < 10:
				print("a dur %u, play %u 退出" % (dur_sec, play_sec))	
				break
		else:
			if play_sec >= 182:
				print("b dur %u, play %u 退出" % (dur_sec, play_sec))	
				break
		print("dur %u, play %u" % (dur_sec, play_sec))	
		time.sleep(10.0)
	
	toshiping()

def toshiping():
	toshouye()
		
#围观
def weiguan():
	x, y = d(resourceId="com.xiangkan.android:id/title_tv", text="在围观内观看小视频5分钟").center()
	d.click(x,y)



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
		self.next_refresh_time = 0

		self.tab_name = 'xk'
		self.db = mydb()
		self.db.connect()
		self.db.get_db("autest")
		self.device = device
		self.is_friday = False

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
		self.next_refresh_time = timeutil.today_hour(24)
		self.save()
		if (timeutil.wday(time.time()) == 5:
			self.is_friday = True
		else:
			self.is_friday = False

	def load(self):
		print(self.tab_name,"load")

		if (timeutil.wday(time.time()) == 5:
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

	def gen(self):
		data = {}

		data['last_time'] = self.last_time
		data['last_coin'] = self.last_coin
		data['signed'] = self.signed
		data['wenzhang_over'] = self.wenzhang_over
		data['shipin_over'] = self.shipin_over
		data['fudai_time'] = self.fudai_time
		data['fudai_count'] = self.fudai_count
		data['next_refresh_time'] = self.next_refresh_time
		
		

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
		self.refresh()

		if not self.has_task():
			print("xk no task")
			return True

		self.set_time()

		if not self.start_app():
			return False

		ret = False
		self.d.watcher("readmore").when(resourceId="com.xiangkan.android:id/more_minute_btn").click()
		while True:
			
			if not self.sign():
				break
			if not self.time_award():
				break

			if not self.wenzhang():
				break	
			if not self.shipin():
				break

			ret = True

		self.d.watchers.remove("readmore")
		self.d.app_stop(self.name)
	
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

		if sec - self.last_coin < timeutil.hour_sec():
			return False

		return True

	def time_award(self):
		sec = time.time()
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
		self.last_coin = timeutil.hour(sec) #取到小时
		#self.last_coin = sec
		self.save()
		return True


	def wenzhang(self):

		d = self.d

		x,y = d(resourceId="com.xiangkan.android:id/tv_tab_title",
		text="我的").sibling(resourceId="com.xiangkan.android:id/tab_icon").center()

		d.click(x,y)

		if (self.wenzhang_over):
			return True

		#wenzhang
		ret = False
		#tv_text = "阅读文章 30 秒"
		tv_text = "阅读文章0.5分钟(圆圈转1圈)"

		for x in range(1,3):
			title_tv_res_id = "com.xiangkan.android:id/title_tv"
			if (d(resourceId=title_tv_res_id, text=tv_text).wait(1.0)):
				stats_res_id = "com.xiangkan.android:id/status_fl"
				stats_btn_res_id = "com.xiangkan.android:id/status_btn"
				if d(resourceId = title_tv_res_id, text=tv_text).sibling(resourceId=stats_res_id)[0].wait(1.0):
					if d(resourceId = title_tv_res_id, text=tv_text).sibling(resourceId=stats_res_id)\
					[0].child(resourceId="stats_btn_res_id")[0].wait(2.0):
						print("ttt")
					else:
						print("hhh")
				else:
					print("xxxasdfa")
				ret = True
				#for item in status:
				#	status_btn = item.child(resourceId="stats_btn_res_id")

				#	for tt in status_btn:
				#		text = tt.get_text()
				#		print("txxxx:",text)
				#		if text == "已完成":
				#			print("已完成")
				#			ret = False

				break
			print("not found")

			d.swipe_ext("up",0.3)


		if not ret:
			self.wenzhang_over = True
			self.save()
			return True

		time.sleep(2.0)
		x, y = d(resourceId="com.xiangkan.android:id/title_tv", text=tv_text).center()
		d.click(x,y)

		for i in range(1,20):
			self.each_wenzhang();
			time.sleep(1.0)

			d.swipe_ext("up",0.5)
			time.sleep(4.0)
			if (self.check_time()):
				return False

	def each_wenzhang(self):
		d = self.d
		try:
			infos = d(resourceId="com.xiangkan.android:id/common_recycler_view").child(resourceId="com.xiangkan.android:id/tvInfo")
		except UiObjectNotFoundError:
			self.toshouye()
			print("tiaoquguangaole")
			return
			pass

		for item in infos:
			text = item.get_text()
		
			print(text)
			if (text.find("广告") != -1):
				continue
			time.sleep(1.0)
			tvtitle = item.sibling(resourceId="com.xiangkan.android:id/tvTitle")
			try:
				x,y = tvtitle.center()
			except UiObjectNotFoundError:
				print("tvTitle not found")
				continue

			d.click(x, y)
			self.onewenzhang()

	def onewenzhang(self):
		d = self.d
		if not (d(resourceId="com.xiangkan.android:id/ringProgressBar").wait(2.0)):
			self.toshouye()
			return

		if self.check_no_award():
			self.toshouye()
			return

		cur = time.time()
		for x in range(1,20):
			d.swipe_ext("down",0.2)
			d.swipe_ext("up",0.2)
			time.sleep(5.0)
			dur = time.time()-cur
			if dur > 70.0:
				print("dur is %f"%(dur))	
				break
		
		self.fudai()	
		self.toshouye()

	def toshouye(self):
		d = self.d
		for i in range(1,3):
			d.press("back");
			if d(resourceId="com.xiangkan.android:id/tv_tab_title", text="首页").wait(1.0):
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
		d = self.d
		d.swipe_ext("down",0.9)
		#tv_text = "观看视频 1 分钟"
		tv_text = "观看视频1分钟(圆圈转1圈)"
		for x in range(1,3):
			if d(resourceId="com.xiangkan.android:id/title_tv", text=tv_text).wait(1.0):
				print("shipin")
				ret = True
				break

			print("找不到 %s"%(tv_text))
			d.swipe_ext("up",0.3)

		if not ret:
			self.shipin_over = True
			self.save()
			return True
		time.sleep(1.0)
		x, y = d(resourceId="com.xiangkan.android:id/title_tv", text=tv_text).center()
		d.click(x,y)

		for i in range(1,5):
			self.each_shipin();
			time.sleep(1.0)
			d.swipe_ext("up",0.5)
			time.sleep(4.0)
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
		d.watcher("restart").when(resourceId="com.xiangkan.android:id/player_compete_restart").click()
		for x in range(1,20):
			if time.time() - now_sec > 180:	
				break
			time.sleep(10.0)
	
		d.watchers.remove("restart")
		self.toshiping()
	
	def toshiping(self):
		self.toshouye()


if __name__ == '__main__':
	d = u2.connect('66J5T19603005713')
	start_app("com.xiangkan.android")
	sign()
	time_award()
	wode()
	wenzhang()
	#shipin()
