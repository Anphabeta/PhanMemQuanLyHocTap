import repositories.RepoMonHoc as RepoMonHoc

def layDanhSachMon():
	return RepoMonHoc.layDanhSachMon()

def layMon(maMon):
	return RepoMonHoc.layMon(maMon)

def layDanhSachMonTrash():
	return RepoMonHoc.layDanhSachMonTrash()

def layDanhSachMonUaThich():
	return RepoMonHoc.layDanhSachMonFav()

def themMon(tenMon):
	RepoMonHoc.themMon(tenMon)

def capNhatTruyCapGanNhat(maMon):
	RepoMonHoc.capNhatTruyCapGanNhat(maMon)

def suaTenMon(maMon, newName):
	RepoMonHoc.capNhatTenMon(maMon, newName)

def moveMonToTrash(maMon):
	RepoMonHoc.capNhatTrangThaiMonDisable(maMon)

def khoiPhucMon(maMon):
	RepoMonHoc.capNhatTrangThaiMonEnable(maMon)

def xoaMon(maMon):
	RepoMonHoc.xoaMon(maMon)

def xoaTatCaMon():
	RepoMonHoc.xoaMonKhiTrangThaiMonDisable()

def layMaMonMoiNhat():
	return RepoMonHoc.layMaMonMoiNhat()

def themUaThich(maMon):
	RepoMonHoc.capNhatIsUaThich(maMon, 'enable')

def boUaThich(maMon):
	RepoMonHoc.capNhatIsUaThich(maMon, 'disable')