from database.db_connect import get_connection

def layDanhSachNote(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT * FROM GhiChu
		WHERE maChuong = (?)
		ORDER BY thuTuNote;
	""", (maChuong,))
	rows = cur.fetchall()

	ds = [dict(row) for row in rows]

	conn.close()

	return ds

def layNote(maNote):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT * FROM GhiChu
		WHERE maNote = (?);
	""",(maNote,))

	rows = cur.fetchall()
	thongTinNote = dict(rows[0])

	conn.close()

	return thongTinNote

def layDanhSachNoteWithThuTu(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT maNote, thuTuNote FROM GhiChu
		WHERE maChuong = (?)
		ORDER BY thuTuNote;
	""", (maChuong,))

	rows = cur.fetchall()

	ds = [dict(row) for row in rows]

	conn.close()

	return ds

def themNote(maChuong, noiDung, thuTuNote, trangThaiThongBao):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		INSERT INTO GhiChu(noiDung, maChuong, thuTuNote, trangThaiThongBao)
		VALUES (?,?,?,?);
	""",(noiDung, maChuong, thuTuNote, trangThaiThongBao))

	conn.commit()
	conn.close()

def layNoteThuTuLonNhat(maChuong):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT max(thuTuNote) FROM GhiChu
		WHERE maChuong = (?)
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
		UPDATE GhiChu
		SET thuTuNote = (?)
		WHERE maNote = (?);
	""",(thuTuMoi,maNote))

	conn.commit()
	conn.close()

def capNhatNote(maNote, noiDung):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		UPDATE GhiChu
		SET noiDung = (?)
		WHERE maNote = (?);
	""",(noiDung,maNote))

	conn.commit()
	conn.close()

def xoaNote(maNote):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		DELETE FROM GhiChu
		WHERE maNote = (?)
	""",(maNote,))

	conn.commit()
	conn.close()

def capNhatTrangThaiThongBao(maNote, trangThaiMoi):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		UPDATE GhiChu
		SET trangThaiThongBao = (?)
		WHERE maNote = (?);
	""", (trangThaiMoi, maNote))

	conn.commit()
	conn.close()