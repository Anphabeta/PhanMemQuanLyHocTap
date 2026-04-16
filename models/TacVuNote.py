import repositories.RepoNote as RepoNote
from debug.log_writer import plainLog, log_model

def layDanhSachNote(maChuong):
	return RepoNote.layDanhSachNote(maChuong)

def layNote(maNote):
	return RepoNote.layNote(maNote)

def themNote(maChuong, noiDung, thuTuNote, trangThaiThongBao):
	RepoNote.themNote(maChuong, noiDung, thuTuNote, trangThaiThongBao)

def layThuTuLonNhat(maChuong):
	return RepoNote.layNoteThuTuLonNhat(maChuong)

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