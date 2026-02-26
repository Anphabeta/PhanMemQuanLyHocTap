from PyQt6.QtWidgets import(
	QDialog,
	QMenu,
	QListWidgetItem
)
from PyQt6.QtCore import Qt, QObject, pyqtSignal
from lang.strings import Text
from services import TacVuMonHoc
from uiView.ViewDialog import InputDialog

class ControllerSidebar(QObject):
	pushBtn = pyqtSignal(str)
	moveToTrash = pyqtSignal()
	subjClicked = pyqtSignal(int)
	changePageAfterDelete = pyqtSignal()

	def __init__(self, sidebar):
		super().__init__()
		
		self.sidebar = sidebar
		# ----------------------------------------------------------------------------------------------
		self.sidebar.pushBtn.connect(self.handlePushBtn)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.addSubject.connect(self.handleAddSubj)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.editSubject.connect(self.handleEditSubj)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.menuContextRequest.connect(self.chooseAction)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.leftClickOnSubjList.connect(self.handleSwitchSubject)
		# ----------------------------------------------------------------------------------------------
		self.updateSubjList()

	def handlePushBtn(self, action):
		if action == "HomePage":
			self.pushBtn.emit("HomePage")
		elif action == "TrashPage":
			self.pushBtn.emit("TrashPage")

	def handleSwitchSubject(self, maMon):
		self.subjClicked.emit(maMon)
		print("Đã chuyển môn")

	def handleAddSubj(self, tenMon):
		TacVuMonHoc.themMon(tenMon)

		self.updateSubjList()
		print("Đã thêm môn")

	def handleMoveSubjToTrash(self,maMon):
		# Nếu môn học đang trỏ tới bị xóa, tự động hiển thị home page
		item = self.sidebar.subjListWidget.currentItem()
		if item is not None and item.data(Qt.ItemDataRole.UserRole) == maMon:
			self.changePageAfterDelete.emit()

		TacVuMonHoc.moveMonToTrash(maMon)

		self.updateSubjList()
		self.moveToTrash.emit()
		print("Đã chuyển qua thùng rác")

	def handleEditSubj(self,maMon,newName):
		TacVuMonHoc.suaTenMon(maMon,newName)
		
		self.updateSubjList()
		print("Đã sửa")

	def chooseAction(self, maMon, action):
		if action == "move":
			self.handleMoveSubjToTrash(maMon)

	def updateSubjList(self):
		subjList = TacVuMonHoc.layDanhSachMon()
		self.sidebar.showSubjList(subjList)