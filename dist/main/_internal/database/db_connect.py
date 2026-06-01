import os
import sqlite3

# Dùng để tạo kết nối với DB

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR,"data","quan_ly_hoc_tap.db")

def get_connection():
	conn = sqlite3.connect(DB_PATH)
	conn.row_factory = sqlite3.Row
	conn.execute("PRAGMA foreign_keys = ON;")  # Bắt buộc bật mỗi lần kết nối để ON DELETE CASCADE hoạt động
	return conn
