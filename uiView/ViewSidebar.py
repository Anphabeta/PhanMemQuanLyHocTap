from PyQt6.QtWidgets import (
	QWidget,
	QPushButton,
	QListWidget,
	QVBoxLayout,
	QMenu,
	QDialog,
	QListWidgetItem
)
from PyQt6.QtCore import Qt, pyqtSignal
from lang.strings import Text
from uiView.ViewDialog import InputDialog

class ViewSidebar(QWidget):
	pushBtn = pyqtSignal(str)
	# rightClickOnSubjList = pyqtSignal()
	leftClickOnSubjList = pyqtSignal(int)
	menuContextRequest = pyqtSignal(int,str)
	addSubject = pyqtSignal(str)
	editSubject = pyqtSignal(int,str)

	def __init__(self):
		# Trong hàm này cần: Khởi tạo, xử lý layout, connect các widget con
		super().__init__()
		#
		self.homeBtn = QPushButton(Text.HOME)
		self.newSubjBtn = QPushButton(Text.NEWSUBJ)
		self.trashBtn = QPushButton(Text.TRASH)
		self.subjListWidget = QListWidget()
		self.subjListWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		#
		self.setFixedWidth(250)
		self.setupLayout()
		self.emitSignal()

	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.homeBtn)
		layout.addWidget(self.newSubjBtn)
		layout.addWidget(self.trashBtn)
		layout.addWidget(self.subjListWidget)

	def showSubjList(self, subjList):
		self.subjListWidget.clear()
		for subj in subjList:
			item = QListWidgetItem(subj["tenMon"])
			item.setData(Qt.ItemDataRole.UserRole, subj["maMon"])
			self.subjListWidget.addItem(item)

	def emitSignal(self):
		self.homeBtn.clicked.connect(lambda: self.pushBtn.emit("HomePage"))
		self.newSubjBtn.clicked.connect(self.createInputDialogAddSubject)
		self.trashBtn.clicked.connect(lambda: self.pushBtn.emit("TrashPage"))

		self.subjListWidget.customContextMenuRequested.connect(self.createContextMenu)
		self.subjListWidget.itemClicked.connect(self.sendCurrentMaMon)

	def createContextMenu(self,pos):
		item = self.subjListWidget.itemAt(pos)

		if item is None:
			return

		maMon = item.data(Qt.ItemDataRole.UserRole)
		contextMenu = ViewContextMenu()

		action = contextMenu.exec(self.subjListWidget.mapToGlobal(pos))

		if action == contextMenu.action_edit:
			self.createInputDialogEditSubject(maMon)
		elif action == contextMenu.action_move:
			self.menuContextRequest.emit(maMon,"move")
		elif action == contextMenu.action_favorite:
			self.menuContextRequest.emit(maMon,"favorite")

	def createInputDialogAddSubject(self):
		dialog = InputDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_THEMMON)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			self.addSubject.emit(dialog.textOutput())

	def createInputDialogEditSubject(self, maMon):
		dialog = InputDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_SUAMON)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			self.editSubject.emit(maMon, dialog.textOutput())

	def sendCurrentMaMon(self, item):
		subjClickedId = item.data(Qt.ItemDataRole.UserRole)
		self.leftClickOnSubjList.emit(subjClickedId)


class ViewContextMenu(QMenu):
	def __init__(self):
		super().__init__()

		self.action_edit = self.addAction(Text.A_SUA)
		self.action_move = self.addAction(Text.A_MOVE)
		self.action_favorite = self.addAction(Text.A_THICH)

