# Dành cho dev để kiểm tra, không liên quan đến phần mềm
# Dùng để hiển thị thông tin của 1 bảng
# Nhập tables để hiển thị thông tin thuộc tính tất cả bảng
# Nhập tên bảng để hiển thị nội dung của bảng
from tabulate import tabulate
from db_connect import get_connection
import textwrap

conn = get_connection()
cur = conn.cursor()

MAX_WIDTH = 20

def wrap_cell(cell, width=MAX_WIDTH):
    if cell is None:
        return ""
    return "\n".join(textwrap.wrap(str(cell), width=width))

command = input()

if command.lower() == 'tables':
    cur.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name
    """)
else:
    cur.execute(f"SELECT * FROM {command}")

rows = cur.fetchall()

headers = [d[0] for d in cur.description]

# Wrap toàn bộ dữ liệu
wrapped_rows = [
    [wrap_cell(cell) for cell in row]
    for row in rows
]

print(tabulate(
    wrapped_rows,
    headers=headers,
    tablefmt="grid"
))

conn.close()