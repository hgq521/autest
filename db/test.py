from rethinkdb import RethinkDB
r = RethinkDB()
con = r.connect("192.168.14.111",28015,db="autest")
con.repl()
#r.db_create("test1").run()
db_test1 = r.db("autest")
#db_test1.table_create("test_table").run()
tb_test = db_test1.table("hs")
#cur = tb_test.get('66J5T19603005713').run(con)
cur = tb_test.run()
con.close()

print(cur)
for h in cur:
	print(h['id'])
