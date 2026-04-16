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
create table if not exists MonHoc(
	maMon integer primary key autoincrement,
	tenMon text not null,
	tgTaoMon text default (datetime('now','localtime')),
	truyCapGanNhat text default (datetime('now','localtime')),
	trangThaiMon text default 'enable'
);
create table if not exists Chuong(
	maChuong integer primary key autoincrement,
	tenChuong text not null,
	tgTaoChuong text default (datetime('now','localtime')),
	maMon integer not null,
	thuTuChuong real,
	foreign key(maMon) references MonHoc(maMon)
		ON DELETE CASCADE
);
create table if not exists GhiChu(
	maNote integer primary key autoincrement,
	noiDung text not null,
	tgTaoNote text default (datetime('now','localtime')),
	maChuong integer not null,
	thuTuNote real,
	foreign key(maChuong) references Chuong(maChuong)
		ON DELETE CASCADE
);
""")
conn.execute("PRAGMA foreign_keys = ON;")
conn.commit()
# --------------------------------------------------------

# Tạo dữ liệu mẫu ----------------------------------------
conn.executescript("""
delete from GhiChu;
delete from Chuong;
delete from MonHoc;

delete from sqlite_sequence where name='MonHoc';
delete from sqlite_sequence where name='Chuong';
delete from sqlite_sequence where name='GhiChu';
""")
conn.commit()

conn.executescript("""
insert into MonHoc(tenMon) values
(
	"Detroit Become Human"
),
(
	"Giải tích"
);

insert into Chuong(tenChuong,maMon,thuTuChuong) values
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

insert into GhiChu(noiDung, maChuong,thuTuNote) values
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
