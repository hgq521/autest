from .config import cfg
from rethinkdb import RethinkDB
r = RethinkDB()

class mydb:
	def __init__(self):
		self.cfg = cfg()
		self.conn = {}
		self.db = {}
		
		pass
	
	def __del__(self):
		self.close()


	def close(self):
		self.conn.close()
		pass

	def connect(self):
		self.conn = r.connect(self.cfg.ip, self.cfg.port)
		self.conn.repl()
		pass

	def create_db(self, db_name):
		if db_name not in r.db_list().run():
			r.db_create(db_name).run()
		pass

	def create_tab(self, tab_name):
		db = self.db
		if tab_name not in db.table_list().run():
			db.table_create(tab_name).run()
		pass

	def get_db(self, db_name):
		self.create_db(db_name)
		self.db = r.db(db_name)
		return self.db
		pass

	def tab(self, tab_name):
		self.create_tab(tab_name)
		return self.db.table(tab_name)
		pass


