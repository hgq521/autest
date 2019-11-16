
import threading
import time

class MyThread(threading.Thread):

	def __init__(self, threadID, name, counter, func, lock):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter =counter
		self.func = func
		self.threadLock = lock

	def run(self):
		print("开启线程:" + self.name)
		#self.threadLock.acquire()
		self.func(self.threadLock)
		#self.threadLock.release()



		
def print_time(threadName, delay, counter, lock):
	while counter:
		time.sleep(delay)
		lock.acquire()
		print("%s:%s" % (threadName, time.ctime(time.time())))
		counter -= 1
		lock.release()



if __name__ == "__main__":
	threadLock = threading.Lock()
	threads = []

	thread1 = MyThread(1, "Thread-1", 5, print_time, threadLock)
	thread2 = MyThread(2, "Thread-2", 5, print_time, threadLock)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()
	print("退出主线程")
