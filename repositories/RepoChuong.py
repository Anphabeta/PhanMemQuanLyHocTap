from database.db_connect import get_connection

def layDanhSachChuong(maMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT * FROM Chuong
		WHERE maMon = (?);
	""", (maMon,))
	rows = cur.fetchall()

	ds = [dict(row) for row in rows]

	conn.close()

	return ds

def layChuong(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT * FROM Chuong
		WHERE maChuong = (?);
	""", (maChuong,))
	rows = cur.fetchall()

	thongTinChuong = dict(rows[0])

	conn.close()

	return thongTinChuong

def layMaChuongMoiNhat():
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT maChuong FROM Chuong
		ORDER BY maChuong DESC
		LIMIT 1;
	""")

	rows = cur.fetchall()

	ds = [dict(row) for row in rows]

	conn.close()

	return ds[0]	

def layChuongThuTuLonNhat(maMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT max(thuTuChuong) FROM Chuong
		WHERE maMon = (?)
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
		INSERT INTO Chuong(tenChuong, maMon, thuTuChuong) values
		(?,?,?);
	""",(tenChuong,maMon,thuTuChuong))

	conn.commit()
	conn.close()

def capNhatTenChuong(maChuong, newName):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		UPDATE Chuong
		SET tenChuong = (?)
		WHERE maChuong = (?);
	""",(newName,maChuong))

	conn.commit()
	conn.close()

def xoaChuong(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		DELETE FROM Chuong
		WHERE maChuong = (?);
	""",(maChuong,))

	conn.commit()
	conn.close()

