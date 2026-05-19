from db_connect import get_connection

# Dùng để reset DB
# MonHoc.trangThaiMon là enum ['enable','disable']
print("Cảnh báo! Thao tác này sẽ xóa toàn bộ dữ liệu trong database của bạn và khôi phục về dữ liệu gốc.")
choice = input("Bạn chắc là muốn tiếp tục chứ? (y/n): ")
while choice!='y':
	choice = input("Bạn chắc là muốn tiếp tục chứ? (y/n): ")


conn = get_connection()
cursor = conn.cursor()

# Tao bảng ----------------------------------------------
conn.executescript("""
CREATE TABLE IF NOT EXISTS MonHoc(
	maMon INTEGER PRIMARY KEY AUTOINCREMENT,
	tenMon TEXT NOT NULL,
	tgTaoMon TEXT DEFAULT (DATETIME('now','localtime')),
	truyCapGanNhat TEXT DEFAULT (DATETIME('now','localtime')),
	trangThaiMon TEXT DEFAULT 'enable',
	isUaThich TEXT DEFAULT 'disable'
);
CREATE TABLE IF NOT EXISTS Chuong(
	maChuong INTEGER PRIMARY KEY AUTOINCREMENT,
	tenChuong TEXT NOT NULL,
	tgTaoChuong TEXT DEFAULT (DATETIME('now','localtime')),
	maMon INTEGER NOT NULL,
	thuTuChuong REAL,
	FOREIGN KEY(maMon) REFERENCES MonHoc(maMon)
		ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS GhiChu(
	maNote INTEGER PRIMARY KEY AUTOINCREMENT,
	noiDung TEXT NOT NULL,
	tgTaoNote TEXT DEFAULT (DATETIME('now','localtime')),
	maChuong INTEGER NOT NULL,
	thuTuNote REAL,
	trangThaiThongBao TEXT DEFAULT 'enable',
	soLanOn REAL DEFAULT 0,
	heSoDeNho REAL DEFAULT 0,
	khoangCach REAL DEFAULT 0,
	ngayOnTiep REAL DEFAULT (DATETIME('now','localtime')),
	FOREIGN KEY(maChuong) REFERENCES Chuong(maChuong)
		ON DELETE CASCADE
);
""")
conn.execute("PRAGMA foreign_keys = ON;")
conn.commit()
# --------------------------------------------------------

# Tạo dữ liệu mẫu ----------------------------------------
conn.executescript("""
DELETE FROM GhiChu;
DELETE FROM Chuong;
DELETE FROM MonHoc;

DELETE FROM sqlite_sequence WHERE name='MonHoc';
DELETE FROM sqlite_sequence WHERE name='Chuong';
DELETE FROM sqlite_sequence WHERE name='GhiChu';
""")
conn.commit()

conn.executescript("""
INSERT INTO MonHoc(tenMon) VALUES
	(
		"Detroit Become Human"
	),
	(
		"Giải tích"
	);

INSERT INTO Chuong(tenChuong,maMon,thuTuChuong) VALUES
	(
		"Khái quát về game",
		1,
		100
	),
	(
		"Chương 1",
		2,
		100
	),
	(
		"Ý nghĩa",
		1,
		200
	),
	(
		"Chương 2",
		2,
		200
	);

INSERT INTO GhiChu(noiDung, maChuong,thuTuNote) VALUES
	(
		"Đây là con game lựa chọn, một lựa chọn sẽ rẽ ra một nhánh. Sẽ có nhiều nhánh và dẫn đến nhiều ending khác nhau",
		1,
		100
	),
	(
		"Đạo hàm là một phép tính để chỉ tốc độ biến thiên của hàm theo biến số",
		2,
		100
	),
	(
		"Ngược lại của đạo hàm là nguyên hàm",
		2,
		200
	),
	(
		"Sau khi chơi game này, tôi thấy thật thú vị, đây là minh chứng cho việc game là một loại hình nghệ thuật không thua kém gì âm nhạc và phim",
		3,
		100
	),
	(
		"Vi phân được gọi là một phép tính của đạo hàm",
		4,
		100
	);
""")
# --------------------------------------------------------

print("Dữ liệu khôi phục thành công")

conn.close()
