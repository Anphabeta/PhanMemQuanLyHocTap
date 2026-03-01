from PyQt6.QtWidgets import(
	QWidget,
	QVBoxLayout,
	QLabel,
	QPushButton,
	QScrollArea
)
from View.ViewChapterBlock import ViewChapterBlock
from lang.strings import Text


class ViewSubjectPage(QWidget):
	def __init__(self):
		super().__init__()

		self.titleSubj = QLabel("Môn học")
		self.addChapterBtn = QPushButton(Text.ADD_CHAPTER_BTN)
		self.scrollArea = QScrollArea()
		self.containerWidget = QWidget()
		self.scrollArea.setWidget(self.containerWidget)
		self.scrollArea.setWidgetResizable(True)

		self.chapterLayout = QVBoxLayout(self.containerWidget)
		self.setupLayout()

	def setTitle(self,tenMon):
		self.titleSubj.setText(tenMon)

	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.titleSubj)
		layout.addWidget(self.addChapterBtn)
		layout.addWidget(self.scrollArea)

	def setSubjId(self,maMon):
		self.subjId = maMon

	def clearChapterLayout(self):
		while self.chapterLayout.count()>0:
			item = self.chapterLayout.takeAt(0)

			widget = item.widget()
			if widget is not None:
				widget.deleteLater()

	def showChapterBlockList(self,listChapter):
		self.clearChapterLayout()
		self.scrollArea.verticalScrollBar().setValue(0)

		for chapter in listChapter:
			blockChapter = ViewChapterBlock(chapter["tenChuong"])
			self.chapterLayout.addWidget(blockChapter)
		self.chapterLayout.addStretch()
		


