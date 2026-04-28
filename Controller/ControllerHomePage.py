from PyQt6.QtCore import QObject, pyqtSignal
from Controller.ControllerCreateNoteDialog import ControllerCreateNoteDialog

from debug.log_writer import log_controller, plainLog
import models.TacVuMonHoc as TacVuMonHoc
import models.TacVuChuong as TacVuChuong
import models.TacVuNote as TacVuNote

class ControllerHomePage(QObject):
	subjList_update_request = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.homePage = view

		self.homePage.noteDialog_create_request.connect(self.handleConnectNoteDialog)

		self.homePage.familyNote_create_request.connect(self.destructoring)

	def handleConnectNoteDialog(self):
		log_controller("Tạo view và controller NoteDialog và kết nối chúng")
		viewNoteDialog = self.homePage.createNoteDialog()

		controllerNoteDialog = ControllerCreateNoteDialog(viewNoteDialog)

		self.homePage.exeNoteDialog(viewNoteDialog)

	def destructoring(self, data):
		subjectId = data["subject"]["id"]
		if subjectId is None:
			TacVuMonHoc.themMon(data["subject"]["text"])
			subjectId = TacVuMonHoc.layMaMonMoiNhat()["maMon"]
			print(subjectId)
		chapterId = data["chapter"]["id"]
		if chapterId is None:
			TacVuChuong.themChuong(data["chapter"]["text"], subjectId)
			chapterId = TacVuChuong.layMaChuongMoiNhat()["maChuong"]
			print(chapterId)
		TacVuNote.themNote(chapterId, data["note"]["content"], data["note"]["isRecall"])
		log_controller("Đã thêm thành công")
		self.subjList_update_request.emit()
