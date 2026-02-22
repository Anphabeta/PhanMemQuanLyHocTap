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
		sb = self.sidebar
		# ----------------------------------------------------------------------------------------------
		sb.newSubjBtn.clicked.connect(self.handleAddSubj)
		# ----------------------------------------------------------------------------------------------
		sb.homeBtn.clicked.connect(lambda: self.pushBtn.emit("HomePage"))
		# ----------------------------------------------------------------------------------------------
		sb.trashBtn.clicked.connect(lambda: self.pushBtn.emit("TrashPage"))
		# ----------------------------------------------------------------------------------------------
		sb.subjListWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		sb.subjListWidget.customContextMenuRequested.connect(self.showContextMenu)
		# ----------------------------------------------------------------------------------------------
		sb.subjListWidget.itemClicked.connect(self.handleSwitchSubject)
		# ----------------------------------------------------------------------------------------------
		self.updateSubjList()

	def handleSwitchSubject(self, item):
		subjClickedId = item.data(Qt.ItemDataRole.UserRole)
		self.subjClicked.emit(subjClickedId)
		print("Đã chuyển môn")

	def handleAddSubj(self):
		dialog = InputDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_THEMMON)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			TacVuMonHoc.themMon(dialog.textOutput())
			print("Đã thêm môn học")

		self.updateSubjList()

	def handleMoveSubjToTrash(self,maMon):
		# Nếu môn học đang trỏ tới bị xóa, tự động hiển thị home page
		item = self.sidebar.subjListWidget.currentItem()
		if item is not None and item.data(Qt.ItemDataRole.UserRole) == maMon:
			self.changePageAfterDelete.emit()

		TacVuMonHoc.moveMonToTrash(maMon)

		self.updateSubjList()
		self.moveToTrash.emit()
		print("Đã chuyển qua thùng rác")

	def handleEditSubj(self,maMon):
		dialog = InputDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_SUAMON)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			TacVuMonHoc.suaTenMon(maMon,dialog.textOutput())
		
		self.updateSubjList()
		print("Đã sửa")

	def showContextMenu(self,pos):
		item = self.sidebar.subjListWidget.itemAt(pos)

		if item is None:
			return

		maMon = item.data(Qt.ItemDataRole.UserRole)
		contextMenu = QMenu()

		action_sua = contextMenu.addAction(Text.A_SUA)
		action_move = contextMenu.addAction(Text.A_MOVE)
		action_thich = contextMenu.addAction(Text.A_THICH)

		action_sua.triggered.connect(lambda _, ma=maMon: self.handleEditSubj(ma))
		action_move.triggered.connect(lambda: self.handleMoveSubjToTrash(maMon))

		contextMenu.exec(self.sidebar.subjListWidget.mapToGlobal(pos))

	def updateSubjList(self):
		subjList = []
		for subj in TacVuMonHoc.layDanhSachMon():
			item = QListWidgetItem(subj["tenMon"])
			item.setData(Qt.ItemDataRole.UserRole, subj["maMon"])
			subjList.append(item)
		self.sidebar.showSubjList(subjList)