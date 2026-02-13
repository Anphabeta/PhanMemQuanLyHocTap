# Dành cho dev để kiểm tra, không liên quan đến phần mềm
# Dùng để hiển thị thông tin của 1 bảng
# Nhập tables để hiển thị thông tin thuộc tính tất cả bảng
# Nhập tên bảng để hiển thị nội dung của bảng
from tabulate import tabulate
from db_connect import get_connection

conn = get_connection()
cur = conn.cursor()

command = input()

if(command.lower()=='tables'):
	cur.execute("""
		SELECT name
		FROM sqlite_master
		WHERE type = 'table'
		ORDER BY name
	""")
	rows = cur.fetchall()

	headers = [d[0] for d in cur.description]

	print(tabulate(rows, headers=headers, tablefmt="grid"))
else:
	cur.execute(f"select * from {command}")
	rows = cur.fetchall()

	headers = [d[0] for d in cur.description]

	print(tabulate(rows, headers=headers, tablefmt="grid"))

conn.close()