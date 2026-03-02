from PyQt6.QtWidgets import(
	QWidget,
	QPushButton,
	QLabel,
	QHBoxLayout, QVBoxLayout,
	QLineEdit
)
from PyQt6.QtCore import pyqtSignal
from lang.strings import Text
from lang.icons import Icon

class ViewChapterBlock(QWidget):
	chapter_edit_request = pyqtSignal(int,str)
	chapter_delete_request = pyqtSignal(int)

	def __init__(self,tenChuong):
		super().__init__()

		self.titleArea = QWidget()
		self.titleChapter = QLabel(tenChuong)
		self.titleChapterEdit = QLineEdit()
		self.titleChapterEdit.hide()
		self.addNoteBtn = QPushButton(Icon.ADD_NOTE_BTN)
		self.editChapterBtn = QPushButton(Icon.EDIT_CHAPTER_BTN)
		self.deleteChapterBtn = QPushButton(Icon.DELETE_CHAPTER_BTN)

		self.noteArea = QWidget()

		self.setLayout()
		self.setSize()
		self.emitSignal()

	def setLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.addWidget(self.titleArea)
		mainLayout.addWidget(self.noteArea)

		titleLayout = QHBoxLayout(self.titleArea)
		titleLayout.addWidget(self.titleChapter)
		titleLayout.addWidget(self.titleChapterEdit)
		titleLayout.addWidget(self.addNoteBtn)
		titleLayout.addWidget(self.editChapterBtn)
		titleLayout.addWidget(self.deleteChapterBtn)

	def setSize(self):
		self.addNoteBtn.setFixedWidth(100)
		self.editChapterBtn.setFixedWidth(100)
		self.deleteChapterBtn.setFixedWidth(100)

	def emitSignal(self):
		self.editChapterBtn.clicked.connect(self.openEditInline)
		self.titleChapterEdit.editingFinished.connect(self.handleSendChapterName)
		self.deleteChapterBtn.clicked.connect(self.handleDeleteChapter)

	def setChapterId(self, maChuong):
		self.chapterId = maChuong

	def openEditInline(self):
		self.titleChapter.hide()
		self.titleChapterEdit.setText(self.titleChapter.text())
		self.titleChapterEdit.show()
		self.titleChapterEdit.setFocus()
		self.titleChapterEdit.selectAll()

	def closeEditInline(self):
		self.titleChapter.show()
		self.titleChapterEdit.hide()

	def handleSendChapterName(self):
		oldText = self.titleChapter.text()
		newText = self.titleChapterEdit.text().strip()

		if newText != "" and newText != oldText:
			self.chapter_edit_request.emit(self.chapterId, newText)
		else:
			self.closeEditInline()

	def handleReceiveChapterName(self, newName):
		self.titleChapter.setText(newName)
		self.titleChapterEdit.setText(newName)
		self.closeEditInline()
		
	def handleDeleteChapter(self):
		self.chapter_delete_request.emit(self.chapterId)

	# def showNoteList(self, noteList):
	# 	for note in noteList:
			
