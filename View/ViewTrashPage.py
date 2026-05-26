from PyQt6.QtWidgets import (
	QWidget,
	QPushButton,
	QListWidget,
	QLabel,
	QVBoxLayout, QHBoxLayout,
	QListWidgetItem
)
from PyQt6.QtCore import Qt, pyqtSignal
from lang.strings import Text


class ViewTrashPage(QWidget):
	subj_recover_request = pyqtSignal()
	subj_hardDelete_request = pyqtSignal()
	subjAll_hardDelete_request = pyqtSignal()

	def __init__(self):
		super().__init__()

		self.title = QLabel()
		self.trashSubjList = QListWidget()
		self.threeBtns = QWidget()
		self.recoverBtn = QPushButton()
		self.deleteBtn = QPushButton()
		self.deleteAllBtn = QPushButton()

		self.setupLayout()
		self.setStyles()
		self.updateUIText()
		self.emitSignal()

	def setupLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.addWidget(self.title)
		mainLayout.addWidget(self.trashSubjList)
		mainLayout.addWidget(self.threeBtns)

		threeBtnsLayout = QHBoxLayout(self.threeBtns)
		threeBtnsLayout.addWidget(self.recoverBtn)
		threeBtnsLayout.addWidget(self.deleteBtn)
		threeBtnsLayout.addWidget(self.deleteAllBtn)

	def setStyles(self):
		self.title.setProperty("type", "title")
		self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

	def updateUIText(self):
		self.title.setText(Text.TRASH_TITLE)
		self.recoverBtn.setText(Text.RECORVER_BTN)
		self.deleteBtn.setText(Text.DELETE_BTN)
		self.deleteAllBtn.setText(Text.DELETE_ALL_BTN)

	def emitSignal(self):
		self.recoverBtn.clicked.connect(lambda: self.subj_recover_request.emit())
		self.deleteBtn.clicked.connect(lambda: self.subj_hardDelete_request.emit())
		self.deleteAllBtn.clicked.connect(lambda: self.subjAll_hardDelete_request.emit())

		self.trashSubjList.itemSelectionChanged.connect(self.setWhenSelectedStateBtn)

	def setDefaultStateBtn(self):
		self.recoverBtn.setEnabled(False)
		self.deleteBtn.setEnabled(False)
		self.deleteAllBtn.setEnabled(self.trashSubjList.count()>0)

	def setWhenSelectedStateBtn(self):
		state = self.trashSubjList.currentItem() is not None
		self.recoverBtn.setEnabled(state)
		self.deleteBtn.setEnabled(state)
		self.deleteAllBtn.setEnabled(self.trashSubjList.count()>0)

	def showTrashSubjList(self, subjList):
		self.trashSubjList.clear()
		for subj in subjList:
			item = QListWidgetItem(subj['tenMon'])
			item.setData(Qt.ItemDataRole.UserRole, subj["maMon"])
			self.trashSubjList.addItem(item)
		self.setDefaultStateBtn()
		
	def getCurrentMaMon(self):
		item = self.trashSubjList.currentItem()
		if item:
			return item.data(Qt.ItemDataRole.UserRole)
		else:
			return None