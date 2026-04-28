from PyQt6.QtCore import QObject, pyqtSignal

import models.TacVuNote as TacVuNote
import models.TacVuMonHoc as TacVuMonHoc
import models.TacVuChuong as TacVuChuong
from debug.log_writer import log_controller, plainLog

class ControllerCreateNoteDialog(QObject):

	def __init__(self, view):
		super().__init__()

		self.createNoteDialog = view

		self.createNoteDialog.subjList_get_request.connect(self.handleGetSubjList)

		self.createNoteDialog.chapterList_get_request.connect(self.handleGetChapterList)

		self.handleGetSubjList()

	# Phụ trách xử lý signal ---------------------------------------------
	def handleGetSubjList(self):
		log_controller("Lấy danh sách môn từ model")
		subjList = TacVuMonHoc.layDanhSachMon()
		self.createNoteDialog.handleGetSubjList(subjList)

	def handleGetChapterList(self, maMon):
		log_controller("Lấy danh sách chương từ model")
		chapterList = TacVuChuong.layDanhSachChuong(maMon)
		
		self.createNoteDialog.handleGetChapterList(chapterList)
	# --------------------------------------------------------------------