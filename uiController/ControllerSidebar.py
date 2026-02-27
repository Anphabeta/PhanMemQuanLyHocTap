from PyQt6.QtCore import Qt, QObject, pyqtSignal
from lang.strings import Text
from services import TacVuMonHoc
from uiView.ViewDialog import InputDialog

class ControllerSidebar(QObject):
	homePage_request = pyqtSignal()
	trashPage_request = pyqtSignal()

	trashSubjList_update_request = pyqtSignal()

	subjItem_navigate_request = pyqtSignal(int)

	def __init__(self, sidebar):
		super().__init__()
		
		self.sidebar = sidebar
		# ----------------------------------------------------------------------------------------------
		self.sidebar.homePage_request.connect(lambda: self.homePage_request.emit())
		# ----------------------------------------------------------------------------------------------
		self.sidebar.trashPage_request.connect(lambda: self.trashPage_request.emit())
		# ----------------------------------------------------------------------------------------------
		self.sidebar.subj_add_request.connect(self.handleAddSubj)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.subj_edit_request.connect(self.handleEditSubj)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.subj_softDelete_request.connect(self.handleMoveSubjToTrash)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.subjItem_selected.connect(self.handleSwitchSubject)
		# ----------------------------------------------------------------------------------------------
		self.updateSubjList()

	def handleSwitchSubject(self, maMon):
		self.subjItem_navigate_request.emit(maMon)
		print("Đã chuyển môn")

	def handleAddSubj(self, tenMon):
		TacVuMonHoc.themMon(tenMon)

		self.updateSubjList()
		print("Đã thêm môn")

	def handleMoveSubjToTrash(self,maMon):
		# Nếu môn học đang trỏ tới bị xóa, tự động chuyển về home page
		# Phát tín hiệu đến MainWindow (homePage request)
		currentMaMon = self.sidebar.getCurrentMaMon()
		if currentMaMon and currentMaMon == maMon:
			self.homePage_request.emit()

		# Di chuyển môn trong db
		TacVuMonHoc.moveMonToTrash(maMon)
		self.updateSubjList()

		# Phát tín hiệu cho trashPage cập nhật lại danh sách (trashSubjlist update request)
		self.trashSubjList_update_request.emit()
		print("Đã chuyển qua thùng rác")

	def handleEditSubj(self,maMon,newName):
		TacVuMonHoc.suaTenMon(maMon,newName)
		
		self.updateSubjList()
		print("Đã sửa")

	def updateSubjList(self):
		subjList = TacVuMonHoc.layDanhSachMon()
		self.sidebar.showSubjList(subjList)