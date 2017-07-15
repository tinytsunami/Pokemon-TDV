import sqlite3

db = sqlite3.connect('./data/database.db')

def rhp(base, individual, effort):
	return int((2*base + individual + int(effort/4))/2) + 60
	pass

def rd(base, individual, effort, nature):
	return int((int((2*base + individual + int(effort/4))/2)+5)*nature)
	pass

def erd(base, individual, effort, nature):
	return int((int((2*base + individual + int(effort/4))/2)+5)*nature*1.5)
	pass

def getTop(value):
	if value >= 252:
		return 253
	return value
	pass

def tdv(hp, de, sd):
	save = [0, 0, 0, 0, 0.0]
	buff = [1, 1]
	if de > sd:
		save[3] = 1
		buff[1] = 1.1
	else:
		save[3] = 0
		buff[0] = 1.1
	pass
	for ehp in range(0, 253, 4):
		rede = getTop(510 - ehp)
		for ede in range(0, rede, 4):
			resd = getTop(510 - ehp - ede)
			for esd in range(0, resd, 4):
				chp = rhp(hp, 31, ehp)
				cde = rd(de, 31, ede, buff[0])
				csd = rd(sd, 31, esd, buff[1])
				tdv = (chp*cde*csd)/(cde+csd)
				if tdv >= save[4]:
					save[0] = ehp
					save[1] = ede
					save[2] = esd
					save[4] = tdv
					pass
	return save
	pass

def eviolite_tdv(hp, de, sd):
	save = [0, 0, 0, 0, 0.0]
	buff = [1, 1]
	if de > sd:
		save[3] = 1
		buff[1] = 1.1
	else:
		save[3] = 0
		buff[0] = 1.1
	pass
	for ehp in range(0, 253, 4):
		rede = getTop(510 - ehp)
		for ede in range(0, rede, 4):
			resd = getTop(510 - ehp - ede)
			for esd in range(0, resd, 4):
				chp = rhp(hp, 31, ehp)
				cde = erd(de, 31, ede, buff[0])
				csd = erd(sd, 31, esd, buff[1])
				tdv = (chp*cde*csd)/(cde+csd)
				if tdv >= save[4]:
					save[0] = ehp
					save[1] = ede
					save[2] = esd
					save[4] = tdv
					pass
	return save
	pass

for data in db.execute("SELECT * FROM `pokemon`"):
	pid = data[0]
	name = data[1]
	tmp = tdv(data[2], data[4], data[6])
	evtdv = eviolite_tdv(data[2], data[4], data[6])
	if tmp[3] == 0:
		nature = "+de"
	else:
		nature = "+sd"
		pass
	save = (pid, name, nature, tmp[0], tmp[1], tmp[2], tmp[4], evtdv[0], evtdv[1], evtdv[2], evtdv[4])
	#print(save)
	db.execute("INSERT INTO `tdv_data` VALUES (?,?,?,?,?,?,?,?,?,?,?)", save)
	db.commit()
	pass
