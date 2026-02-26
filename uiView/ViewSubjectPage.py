from PyQt6.QtWidgets import(
	QWidget,
	QVBoxLayout,
	QLabel,
	QPushButton,
	QScrollArea
)
from lang.strings import Text


class ViewSubjectPage(QWidget):
	def __init__(self):
		super().__init__()

		self.titleSubj = QLabel("Môn học")
		self.addChapterBtn = QPushButton(Text.ADD_CHAPTER_BTN)
		self.scrollArea = QScrollArea()
		self.containerWidget = QWidget()
		self.scrollArea.setWidget(self.containerWidget)

		self.setupLayout()
		# self.setTitle(maMon)


	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.titleSubj)
		layout.addWidget(self.addChapterBtn)
		layout.addWidget(self.scrollArea)

	# def setupContent(self,listChapterAndNote):
		
