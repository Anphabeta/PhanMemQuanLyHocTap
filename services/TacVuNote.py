from database.db_connect import get_connection

def layDanhSachNote(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		select * from GhiChu
		where maChuong = (?);
	""", (maChuong,))
	rows = cur.fetchall()

	ds = [dict(row) for row in rows]

	conn.close()

	return ds

def layNote(maNote):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		select * from GhiChu
		where maNote = (?);
	""",(maNote,))

	rows = cur.fetchall()
	thongTinNote = dict(rows[0])

	conn.close()

	return thongTinNote

def themNote(maChuong, noiDung, thuTuNote):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		insert into GhiChu(noiDung, maChuong, thuTuNote)
		values (?,?,?);
	""",(noiDung, maChuong, thuTuNote))

	conn.commit()
	conn.close()

def layThuTuLonNhat(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		select max(thuTu) from GhiChu
		where maChuong = (?)
	""", (maChuong,))

	row = cur.fetchone()

	conn.close()

	if row[0] is None:
		return 0
	else:
		return row[0]


def suaNote(maNote, noiDung):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		update GhiChu
		set noiDung = (?)
		where maNote = (?);
	""",(noiDung,maNote))

	conn.commit()
	conn.close()

def xoaNote(maNote):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		delete from GhiChu
		where maNote = (?)
	""",(maNote,))

	conn.commit()
	conn.close()


