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
from View.ViewDialog import InputDialog

class ViewSidebar(QWidget):
	homePage_request = pyqtSignal()
	subj_add_request = pyqtSignal(str)
	trashPage_request = pyqtSignal()

	subjItem_selected = pyqtSignal(int)

	subj_edit_request = pyqtSignal(int,str)
	subj_softDelete_request = pyqtSignal(int)
	subj_addFavorite_request = pyqtSignal(int)

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


	# Phụ trách khởi tạo --------------------------------------------------
	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.homeBtn)
		layout.addWidget(self.newSubjBtn)
		layout.addWidget(self.trashBtn)
		layout.addWidget(self.subjListWidget)
	# ---------------------------------------------------------------------


	# Phụ trách phát tín hiệu ---------------------------------------------
	def emitSignal(self):
		self.homeBtn.clicked.connect(self.handleSwitchHomePage)
		self.newSubjBtn.clicked.connect(self.createInputDialogAddSubject)
		self.trashBtn.clicked.connect(self.handleSwitchTrashPage)

		self.subjListWidget.customContextMenuRequested.connect(self.createContextMenu)
		self.subjListWidget.itemClicked.connect(self.sendCurrentMaMon)

	def handleSwitchHomePage(self):
		self.subjListWidget.clearSelection()
		self.homePage_request.emit()

	def handleSwitchTrashPage(self):
		self.subjListWidget.clearSelection()
		self.trashPage_request.emit()

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
			self.subj_softDelete_request.emit(maMon)
		elif action == contextMenu.action_favorite:
			self.subj_addFavorite_request.emit(maMon)

	def createInputDialogAddSubject(self):
		dialog = InputDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_THEMMON)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			self.subj_add_request.emit(dialog.textOutput())

	def createInputDialogEditSubject(self, maMon):
		dialog = InputDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_SUAMON)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			self.subj_edit_request.emit(maMon, dialog.textOutput())

	def sendCurrentMaMon(self, item):
		subjClickedId = item.data(Qt.ItemDataRole.UserRole)
		self.subjItem_selected.emit(subjClickedId)
	# ---------------------------------------------------------------------


	# Hàm để gọi bên ngoài ------------------------------------------------
	def getCurrentMaMon(self):
		item = self.subjListWidget.currentItem()
		if item:
			return item.data(Qt.ItemDataRole.UserRole)
		else:
			return None

	def showSubjList(self, subjList):
		self.subjListWidget.clear()
		for subj in subjList:
			item = QListWidgetItem(subj["tenMon"])
			item.setData(Qt.ItemDataRole.UserRole, subj["maMon"])
			self.subjListWidget.addItem(item)
	# ---------------------------------------------------------------------
	


class ViewContextMenu(QMenu):
	def __init__(self):
		super().__init__()

		self.action_edit = self.addAction(Text.A_SUA)
		self.action_move = self.addAction(Text.A_MOVE)
		self.action_favorite = self.addAction(Text.A_THICH)

