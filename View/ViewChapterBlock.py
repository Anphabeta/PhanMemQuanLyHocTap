from PyQt6.QtWidgets import(
	QWidget,
	QPushButton,
	QLabel,
	QHBoxLayout, QVBoxLayout
)
from lang.strings import Text
from lang.icons import Icon

class ViewChapterBlock(QWidget):
	def __init__(self,tenChuong):
		super().__init__()

		self.titleArea = QWidget()
		self.titleChapter = QLabel(tenChuong)
		self.addNoteBtn = QPushButton(Icon.ADD_NOTE_BTN)
		self.editChapterBtn = QPushButton(Icon.EDIT_CHAPTER_BTN)
		self.deleteChapterBtn = QPushButton(Icon.DELETE_CHAPTER_BTN)

		self.noteArea = QWidget()

		self.setLayout()
		self.setSize()

	def setLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.addWidget(self.titleArea)
		mainLayout.addWidget(self.noteArea)

		titleLayout = QHBoxLayout(self.titleArea)
		titleLayout.addWidget(self.titleChapter)
		titleLayout.addWidget(self.addNoteBtn)
		titleLayout.addWidget(self.editChapterBtn)
		titleLayout.addWidget(self.deleteChapterBtn)

	def setSize(self):
		self.addNoteBtn.setFixedWidth(100)
		self.editChapterBtn.setFixedWidth(100)
		self.deleteChapterBtn.setFixedWidth(100)

	# def showNoteList(self, noteList):
	# 	for note in noteList:
			
