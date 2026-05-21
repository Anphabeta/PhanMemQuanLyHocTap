from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from Controller.ControllerCreateNoteDialog import ControllerCreateNoteDialog
from Controller.ControllerReviewDialog import ControllerReviewDialog

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

		self.viewReviewTagList = []

		self.initContent()

		# Cài đặt 60p refresh danh sách 1 lần --------------------
		self.refreshTimer = QTimer(self)
		self.refreshTimer.timeout.connect(self.updateReviewTagList)
		self.refreshTimer.start(3600000)
		# ------------------------------------------------------

	# Phụ trách khởi tạo review tag ----------------------------------
	def initContent(self):
		self.updateReviewTagList()
	# -----------------------------------------------------

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

	def handleCreateReviewDialog(self, maNote):
		log_controller("Tạo review dialog")
		data = TacVuNote.layNote(maNote) # maNote, noiDungNote, cauHoi

		viewReviewDialog = self.homePage.createViewReviewDialog(data)
		controllerReviewDialog = ControllerReviewDialog(viewReviewDialog)

		result = viewReviewDialog.exec()

		if result == QDialog.DialogCode.Accepted:
			controllerReviewDialog.handleSendScore(maNote, viewReviewDialog.getDiem())
			self.updateReviewTagList()


	# Phụ trách hiển thị Review Tag ----------------------------------------
	def createViewReviewTag(self):
		dsReviewTag = TacVuNote.layDanhSachReviewTag() # maNote, tenMonHoc, tenChuong, cauHoi, noiDung

		log_controller("Tạo ds review tag")
		for reviewTag in dsReviewTag:
			viewReviewTag = self.homePage.createReviewTag(reviewTag)
			self.viewReviewTagList.append(viewReviewTag)

			# Viết signal vào đây
			viewReviewTag.clicked.connect(self.handleCreateReviewDialog)


	def deleteViewReviewTag(self):
		log_controller("Xóa ds review tag cũ")
		self.viewReviewTagList.clear()
		self.homePage.clearReviewTagLayout()

	def updateReviewTagList(self):
		log_controller("Cập nhật lại ds review tag")
		self.deleteViewReviewTag()
		self.createViewReviewTag()
	# ----------------------------------------------------------------------