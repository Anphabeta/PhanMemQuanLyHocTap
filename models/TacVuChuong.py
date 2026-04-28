import repositories.RepoChuong as RepoChuong

def layDanhSachChuong(maMon):
	return RepoChuong.layDanhSachChuong(maMon)

def layChuong(maChuong):
	return RepoChuong.layChuong(maChuong)

def layThuTuLonNhat(maMon):
	return RepoChuong.layChuongThuTuLonNhat(maMon)

def layMaChuongMoiNhat():
	return RepoChuong.layMaChuongMoiNhat()

def themChuong(tenChuong, maMon):
	maxOrder = layThuTuLonNhat(maMon)
	RepoChuong.themChuong(tenChuong, maMon, maxOrder+100)

def suaTenChuong(maChuong, newName):
	RepoChuong.capNhatTenChuong(maChuong, newName)

def xoaChuong(maChuong):
	RepoChuong.xoaChuong(maChuong)

