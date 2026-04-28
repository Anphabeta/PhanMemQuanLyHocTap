from database.db_connect import get_connection

# Đây là vùng đệm giao tiếp giữa logic nghiệp vụ và DB
# Quy tắc chung:
# - Tạo kết nối (gọi hàm get_connection())
# - Giao tiếp với DB (nhúng lệnh SQL vào python)
# - Đóng kết nối (conn.close())

def layDanhSachMon():
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT * FROM MonHoc
		WHERE trangThaiMon = 'enable'
		ORDER BY truyCapGanNhat DESC
	""")
	rows = cur.fetchall()
	
	ds = [dict(row) for row in rows]

	conn.close()

	return ds

def layMon(maMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT * FROM MonHoc
		WHERE maMon = (?)
	""",(maMon,))
	rows = cur.fetchall()
	
	thongTinMon = dict(rows[0])

	conn.close()

	return thongTinMon

def layDanhSachMonTrash():
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT * FROM MonHoc
		WHERE trangThaiMon = 'disable'
		ORDER BY truyCapGanNhat DESC
	""")
	rows = cur.fetchall()

	ds = [dict(row) for row in rows]

	conn.close()

	return ds

def layMaMonMoiNhat():
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		SELECT maMon FROM MonHoc
		ORDER BY maMon DESC
		LIMIT 1;
	""")

	rows = cur.fetchall()

	ds = [dict(row) for row in rows]

	conn.close()

	return ds[0]

def themMon(tenMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		INSERT INTO MonHoc(tenMon,truyCapGanNhat) 
		VALUES (?,datetime('now','localtime'))
	""",(tenMon,))

	conn.commit()
	conn.close()


def capNhatTruyCapGanNhat(maMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		UPDATE MonHoc
		SET truyCapGanNhat = datetime('now','localtime')
		WHERE maMon = (?)
	""",(maMon,))

	conn.commit()
	conn.close()

def capNhatTenMon(maMon, newName):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		UPDATE MonHoc SET 
		tenMon = (?),
		truyCapGanNhat = datetime('now','localtime')
		WHERE maMon = (?)
	""",(newName,maMon))

	conn.commit()
	conn.close()

def capNhatTrangThaiMonDisable(maMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		UPDATE MonHoc SET 
		trangThaiMon = 'disable'
		WHERE maMon = (?)
	""",(maMon,))

	conn.commit()
	conn.close()

def capNhatTrangThaiMonEnable(maMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		UPDATE MonHoc SET 
		trangThaiMon = 'enable',
		truyCapGanNhat = datetime('now','localtime')
		WHERE maMon = (?)
	""",(maMon,))

	conn.commit()
	conn.close()

def xoaMon(maMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		DELETE FROM MonHoc 
		WHERE maMon = (?);
	""",(maMon,))

	conn.commit()
	conn.close()

def xoaMonKhiTrangThaiMonDisable():
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		DELETE FROM MonHoc 
		WHERE trangThaiMon = 'disable';
	""")

	conn.commit()
	conn.close()

