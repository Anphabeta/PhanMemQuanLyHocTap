import repositories.RepoChuong as RepoChuong

def layDanhSachChuong(maMon):
	return RepoChuong.layDanhSachChuong(maMon)

def layChuong(maChuong):
	return RepoChuong.layChuong(maChuong)

def layThuTuLonNhat(maMon):
	return RepoChuong.layChuongThuTuLonNhat(maMon)

def themChuong(tenChuong, maMon, thuTuChuong):
	RepoChuong.themChuong(tenChuong, maMon, thuTuChuong)

def suaTenChuong(maChuong, newName):
	RepoChuong.capNhatTenChuong(maChuong, newName)

def xoaChuong(maChuong):
	RepoChuong.xoaChuong(maChuong)

