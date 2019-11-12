from logger.logger import Logger
import time

if __name__ == '__main__':
	tt = Logger().get_log
	tt.error("sdaaada3")
	tt.debug("sdetsdebugtest1")
	for i in range(1,20):
		tt.debug("asda %u" %(i))
		time.sleep(5.0)
