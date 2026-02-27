from PyQt6.QtCore import Qt, QObject, pyqtSignal
from lang.strings import Text
from services import TacVuMonHoc

class ControllerTrashPage(QObject):
	subjList_update_request = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.trashPage = view

		# ----------------------------------------------------------------------------------------------
		self.trashPage.subj_recover_request.connect(self.handleRecover)
		# ----------------------------------------------------------------------------------------------
		self.trashPage.subj_hardDelete_request.connect(self.handleDelete)
		# ----------------------------------------------------------------------------------------------
		self.trashPage.subjAll_hardDelete_request.connect(self.handleDeleteAll)
		# ----------------------------------------------------------------------------------------------

		self.updateTrashSubjList()

	def handleRecover(self):
		maMon = self.trashPage.getCurrentMaMon()
		if maMon:
			TacVuMonHoc.khoiPhucMon(maMon)
			print("Đã khôi phục môn")
			self.updateTrashSubjList()
			self.subjList_update_request.emit()

	def handleDelete(self):
		maMon = self.trashPage.getCurrentMaMon()
		if maMon:
			TacVuMonHoc.xoaMon(maMon)
			print("Đã xóa môn vĩnh viễn")
			self.updateTrashSubjList()

	def handleDeleteAll(self):
		TacVuMonHoc.xoaTatCaMon()
		print("Đã xóa tất cả môn")
		self.updateTrashSubjList()

	def updateTrashSubjList(self):
		trashSubjList = TacVuMonHoc.layDanhSachMonTrash()
		self.trashPage.showTrashSubjList(trashSubjList)