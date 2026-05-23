import repositories.RepoNote as RepoNote
from datetime import datetime, timedelta
from debug.log_writer import plainLog, log_model

def layDanhSachNote(maChuong):
	return RepoNote.layDanhSachNote(maChuong)

def layNote(maNote):
	return RepoNote.layNote(maNote)

def layThuTuLonNhat(maChuong):
	return RepoNote.layNoteThuTuLonNhat(maChuong)

def themNote(maChuong, noiDung, cauHoi, trangThaiThongBao):
	maxOrder = RepoNote.layNoteThuTuLonNhat(maChuong)
	if maxOrder is None:
		maxOrder = 0

	RepoNote.themNote(maChuong, noiDung, cauHoi, maxOrder+100, trangThaiThongBao)

def suaNote(maNote, noiDung):
	RepoNote.capNhatNote(maNote, noiDung)

def xoaNote(maNote):
	RepoNote.xoaNote(maNote)

def diChuyenNoteLen(maNote, maChuong):
	ds = RepoNote.layDanhSachNoteWithThuTu(maChuong)

	for i in range(len(ds)):
		if ds[i]["maNote"] == maNote:
			curIdx = i
			break

	if curIdx == 0:
		log_model("Di chuyển thất bại")
		return

	if curIdx-2 <0:
		tb = ds[curIdx-1]["thuTuNote"]/2
	else:
		tb = (ds[curIdx-2]["thuTuNote"] + ds[curIdx-1]["thuTuNote"])/2
	RepoNote.capNhatThuTu(maNote, tb)

def diChuyenNoteXuong(maNote, maChuong):
	ds = RepoNote.layDanhSachNoteWithThuTu(maChuong)
	print(ds)

	for i in range(len(ds)):
		if ds[i]["maNote"] == maNote:
			curIdx = i
			break

	if curIdx == len(ds)-1:
		log_model("Di chuyển thất bại")
		return

	if curIdx+2 >len(ds)-1:
		tb =  ds[curIdx+1]["thuTuNote"] + 100
	else:
		tb = (ds[curIdx+2]["thuTuNote"] + ds[curIdx+1]["thuTuNote"])/2
	RepoNote.capNhatThuTu(maNote, tb)

def tatThongBao(maNote):
	RepoNote.capNhatTrangThaiThongBao(maNote, "disable")

def batThongBao(maNote):
	RepoNote.capNhatTrangThaiThongBao(maNote, "enable")

def lapLaiNgatQuang(diem, thongSo):
	(soLanLap, doDe, khoangCachOn) = thongSo
	if diem >= 3:
		if soLanLap == 0:
			khoangCachOn = 0.5
		elif soLanLap == 1:
			khoangCachOn = 2
		else:
			khoangCachOn =  round(khoangCachOn * doDe)
		soLanLap += 1
	else:
		soLanLap = 0
		khoangCachOn = 1

	doDe += (0.1 - (5-diem)*(0.08 + (5-diem)*0.02))
	doDe = max(doDe, 1.3)
	doDe = min(doDe, 2.3)

	return (soLanLap, doDe, khoangCachOn)


def capNhatThongSo(maNote, diem):
	data = RepoNote.layThongSo(maNote)
	thongSo = (data["soLanOn"], data["heSoDeNho"], data["khoangCach"])
	thongSo = lapLaiNgatQuang(diem, thongSo)

	ngayOnTiep = datetime.now() + timedelta(days=thongSo[2])
	RepoNote.capNhatThongSo(maNote, thongSo[0], thongSo[1], thongSo[2], ngayOnTiep.strftime("%Y-%m-%d %H:%M:%S"))

def resetThongSo(maNote):
	RepoNote.capNhatThongSo(maNote, 0, 1.7, 0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def layDanhSachReviewTag():
	return RepoNote.layDanhSachReviewTag()

def suaCauHoi(maNote, cauHoiMoi):
	RepoNote.suaCauHoi(maNote, cauHoiMoi)