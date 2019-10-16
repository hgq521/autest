import logging
import os


class Logger:
	
	def __init__(self, name=__name__):
		self.name = name
		self.logger = logging.getLogger(self.name)
		self.logger.setLevel(logging.DEBUG)

		log_path = os.path.dirname(os.path.abspath(__file__))
		log_name = log_path + '/out.log'
		
		fh = logging.FileHandler(log_name, mode='a', encoding='utf-8')
		fh.setLevel(logging.DEBUG)

		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)

		formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
		'-%(levelname)s-[日志信息]:%(message)s', datefmt='%a, %d %b %Y %H:%M:%S')

		fh.setFormatter(formatter)
		ch.setFormatter(formatter)

		self.logger.addHandler(fh)
		self.logger.addHandler(ch)

	@property
	def get_log(self):
		return self.logger

if __name__ == '__main__':
	log = Logger(__name__).get_log
	log.error('xxxxxxxxxxxxxxxxxxxtest')

