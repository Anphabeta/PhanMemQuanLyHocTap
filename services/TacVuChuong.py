from database.db_connect import get_connection

def layDanhSachChuong(maMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		select * from Chuong
		where maMon = (?);
	""", (maMon,))
	rows = cur.fetchall()

	ds = [dict(row) for row in rows]

	conn.close()

	return ds

def layChuong(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		select * from Chuong
		where maChuong = (?);
	""", (maChuong,))
	rows = cur.fetchall()

	thongTinChuong = dict(rows[0])

	conn.close()

	return thongTinChuong

def layThuTuLonNhat(maMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		select max(thuTuChuong) from Chuong
		where maMon = (?)
	""",(maMon,))

	row = cur.fetchone()

	conn.close()

	if row[0] is None:
		return 0
	else:
		return row[0]

def themChuong(tenChuong, maMon, thuTuChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		insert into Chuong(tenChuong, maMon, thuTuChuong) values
		(?,?,?);
	""",(tenChuong,maMon,thuTuChuong))

	conn.commit()
	conn.close()

def suaTenChuong(maChuong, newName):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		update Chuong
		set tenChuong = (?)
		where maChuong = (?);
	""",(newName,maChuong))

	conn.commit()
	conn.close()

def xoaChuong(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		delete from Chuong
		where maChuong = (?);
	""",(maChuong,))

	conn.commit()
	conn.close()

