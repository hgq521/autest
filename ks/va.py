import sys
sys.path.append('E:\\pythontest\\tt\\autest') 

from opcv.valid import find_slot
import time
import random
import uiautomator2 as u2


class va:
	def __init__(self, d, pk, serl):
		self.d = d
		self.pk = pk
		self.serl = serl
		self.count = 0
		self.file_name = ""
		pass

	def take_sshot(self):
		d = self.d
		sec = time.time() // 1
		self.file_name = "p"+time.strftime("%Y%m%d_%H%M%S", time.localtime())+".png"
		d.screenshot(self.file_name)

	
	def swip(self, target_x):
		target_x = target_x//1
		d = self.d
		x,y = 65,985
		for slib in d(text="向右拖动滑块填充拼图").sibling(className="android.view.View"):
			x1,y = slib.center()
			x, y1 = slib.center(offset=(0, 0))
			print("slib x1,y %u %u " %(x1, y ))
			print("slib x,y1 %u %u " %(x, y1 ))
			if x1 >400:
				continue
			x = x1
			break
		print("xxxxxxx %u %u, %u" % (x,y, target_x))

		time.sleep(0.01)
		rand_y = 0
		rand_x = 0
		point_list = []
		dis = target_x - x
		total = 0
		for i in range(5):
			total += 2**i

		cur = 0
		
		rand_max = 10
		rand = random.randint(1,rand_max)
		rand_y = y + (rand-rand_max/2)
		point_list.append((x, rand_y))
		for i in range(5):
			cur += 2**(4-i)
			rand = random.randint(1,rand_max)
			rand_x = x + dis * cur /total + rand - rand_max/2

			rand = random.randint(1,rand_max)
			rand_y = y + (rand-rand_max/2)
			point_list.append((rand_x, rand_y))

		rand = random.randint(1,rand_max)
		rand_y = y + (rand-rand_max/2)
		point_list.append((target_x, rand_y))


		for i in range(int(x), int(target_x), 100):
			rand = random.randint(1,6)
			rand_y = y + (rand-3)
			rand = random.randint(1,6)
			rand_x = i + (rand-3)
			#point_list.append((rand_x, rand_y))


		rand_y = point_list[len(point_list) - 1][1]
		point_list[len(point_list)-1] = (target_x, rand_y)
		for aa,bb in point_list:
			print("ssssssssssss %u %u"%(aa,bb))
		d.swipe_points(point_list, .5)


	def fresh(self):
		d = self.d
		__, min_y = d(text="向右拖动滑块填充拼图").center(offset(0,0))

		for ci in d(text="captcha").child(className="android.view.View", clickable=True):
			
			x, y = ci.center(offset(0,0))

			print("fresh x, y (%u, %u); min_y %u" %u (x, y, min_y))
			if y >= min_y:
				continue
			x, y = ci.center()
			d.click(x, y)
			print("fresh click x, y (%u, %u)" % (x, y))

		pass

	def run(self):
		d = self.d
		while (True):
			if (d(text="向右拖动滑块填充拼图").wait(20.0)):
				
				time.sleep(1.0)
				self.take_sshot()
				time.sleep(2.0)
				ret, start_x, end_x = find_slot(self.file_name)
				print("find ret start end (%u, %u, %u)"%(ret, start_x, end_x))
				if (ret):
					self.swip((start_x + end_x)//2)
					self.count += 1
					
				else:
					self.fresh()
					continue

				time.sleep(300.0)

				pass
				
		pass


if __name__ == "__main__":
	serl = '66J5T19603005713'
	d = u2.connect(serl)
	pk = "com.kuaishou.nebula"
	tt = va(d, pk, serl)
	tt.run()
	#tt.swip(736)
