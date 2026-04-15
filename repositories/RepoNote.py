from database.db_connect import get_connection

def layDanhSachNote(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		select * from GhiChu
		where maChuong = (?)
		order by thuTuNote;
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

def layDanhSachNoteWithThuTu(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		select maNote, thuTuNote from GhiChu
		where maChuong = (?)
		order by thuTuNote;
	""", (maChuong,))

	rows = cur.fetchall()

	ds = [dict(row) for row in rows]

	conn.close()

	return ds

def themNote(maChuong, noiDung, thuTuNote):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		insert into GhiChu(noiDung, maChuong, thuTuNote)
		values (?,?,?);
	""",(noiDung, maChuong, thuTuNote))

	conn.commit()
	conn.close()

def layNoteThuTuLonNhat(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		select max(thuTuNote) from GhiChu
		where maChuong = (?)
	""", (maChuong,))

	row = cur.fetchone()

	conn.close()

	if row[0] is None:
		return 0
	else:
		return row[0]

def capNhatThuTu(maNote, thuTuMoi):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		update GhiChu
		set thuTuNote = (?)
		where maNote = (?);
	""",(thuTuMoi,maNote))

	conn.commit()
	conn.close()

def capNhatNote(maNote, noiDung):
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


