import sqlite3
db = sqlite3.connect('./data/database.db')

for data in db.execute("SELECT * FROM `pokemon`"):
	evio = data[0]
	name = data[1]
	fin = data[8]
	if fin == 0:
		db.execute("UPDATE `tdv_data` SET `eviolite_tdv` = `tdv` WHERE `name` = ?", (name,))
		db.commit()
		pass
	pass
