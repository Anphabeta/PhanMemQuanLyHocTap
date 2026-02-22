from PyQt6.QtWidgets import (
	QWidget,
	QPushButton,
	QListWidget,
	QLabel,
	QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt
from lang.strings import Text


class ViewTrashPage(QWidget):
	def __init__(self):
		super().__init__()

		self.title = QLabel(Text.TRASH_TITLE)
		self.trashSubjList = QListWidget()
		self.threeBtns = QWidget()
		self.recoverBtn = QPushButton(Text.RECORVER_BTN)
		self.deleteBtn = QPushButton(Text.DELETE_BTN)
		self.deleteAllBtn = QPushButton(Text.DELETE_ALL_BTN)

		self.setupLayout()

	def setupLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.addWidget(self.title)
		mainLayout.addWidget(self.trashSubjList)
		mainLayout.addWidget(self.threeBtns)

		threeBtnsLayout = QHBoxLayout(self.threeBtns)
		threeBtnsLayout.addWidget(self.recoverBtn)
		threeBtnsLayout.addWidget(self.deleteBtn)
		threeBtnsLayout.addWidget(self.deleteAllBtn)

	def setDefaultStateBtn(self):
		self.deleteAllBtn.setEnabled(self.trashSubjList.count()>0)
		self.recoverBtn.setEnabled(False)
		self.deleteBtn.setEnabled(False)

	def showTrashSubjList(self, subjList):
		self.trashSubjList.clear()
		for subj in subjList:
			self.trashSubjList.addItem(subj)
		self.setDefaultStateBtn()
		
	def getId_item_selected(self):
		item = self.trashSubjList.currentItem()

		if not item is None:
			return item.data(Qt.ItemDataRole.UserRole)
		return None