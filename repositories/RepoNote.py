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

def themNote(maChuong, noiDung, cauHoi, thuTuNote, trangThaiThongBao):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		INSERT INTO GhiChu(noiDung, cauHoi, maChuong, thuTuNote, trangThaiThongBao)
		VALUES (?,?,?,?,?);
	""",(noiDung, cauHoi, maChuong, thuTuNote, trangThaiThongBao))

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

	if row is None:
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

def layThongSo(maNote):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT soLanOn, heSoDeNho, khoangCach FROM GhiChu
		WHERE maNote = (?)
	""", (maNote,))

	row = cur.fetchone()

	conn.close()

	if row is None:
		return None
	else:
		return dict(row)

def capNhatThongSo(maNote, soLanOn, heSoDeNho, khoangCach, ngayOnTiep):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		UPDATE GhiChu
		SET soLanOn = (?),
			heSoDeNho = (?),
			khoangCach = (?),
			ngayOnTiep = (?)
		WHERE maNote = (?);
	""",(soLanOn, heSoDeNho, khoangCach, ngayOnTiep, maNote))

	conn.commit()
	conn.close()

def layDanhSachNoteCanOn():
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

def layDanhSachReviewTag():
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT g.maNote, m.tenMon, c.tenChuong, g.cauHoi, g.noiDung 
		FROM GhiChu as g
		JOIN Chuong as c ON g.maChuong = c.maChuong
		JOIN MonHoc as m ON m.maMon = c.maMon
		WHERE g.ngayOnTiep <= datetime('now', 'localtime');
	""")
	rows = cur.fetchall()

	ds = [dict(row) for row in rows]

	conn.close()

	return ds	

def suaCauHoi(maNote, cauHoiMoi):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		UPDATE GhiChu
		SET cauHoi = (?)
		WHERE maNote = (?);
	""",(cauHoiMoi, maNote))

	conn.commit()
	conn.close()

