from database.db_connect import get_connection

# Đây là vùng đệm giao tiếp giữa logic nghiệp vụ và DB
# Quy tắc chung:
# - Tạo kết nối (gọi hàm get_connection())
# - Giao tiếp với DB (nhúng lệnh SQL vào python)
# - Đóng kết nối (conn.close())

def layDanhSachMon():
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("select * from MonHoc order by truyCapGanNhat desc")
	rows = cur.fetchall()
	
	ds = [dict(row) for row in rows]

	conn.close()

	return ds

def themMon(tenMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("insert into MonHoc(tenMon,truyCapGanNhat) values (?,datetime('now','localtime'))",(tenMon,))

	conn.commit()
	conn.close()


def capNhatTruyCapGanNhat(maMon):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		update MonHoc
		set truyCapGanNhat = datetime('now','localtime')
		where maMon = (?)
	""",(maMon,))

	conn.commit()
	conn.close()

def suaTenMon(maMon, newName):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
		update MonHoc
		set tenMon = (?)
		where maMon = (?)
	""",(newName,maMon))

	conn.commit()
	conn.close()
