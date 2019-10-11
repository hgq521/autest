import time

def day_hours():
	return 24*60*60

def hour_sec():
	return 3600

def today_hour(hour): #24小时制
	sec = time.time() 
	return (sec - sec % day_hours() + hour * hour_sec() - 8 * hour_sec())

def wday(sec):
	tt = time.localtime(sec)
	return (tt.tm_wday+1)

if __name__ == '__main__':
	sec = today_hour(5)
	print(sec)
	print(time.localtime(sec))
	print(wday(sec))

