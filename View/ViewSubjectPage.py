from PyQt6.QtWidgets import(
	QWidget,
	QVBoxLayout,
	QLabel,
	QPushButton,
	QScrollArea,
	QDialog,
	QSizePolicy
)
from PyQt6.QtCore import pyqtSignal, Qt
from View.ViewChapterBlock import ViewChapterBlock
from View.QDefine import InputDialog
from lang.strings import Text


class ViewSubjectPage(QWidget):
	chapter_add_request = pyqtSignal(int,str)
	chapterList_refresh_request = pyqtSignal()

	def __init__(self):
		super().__init__()

		self.titleSubj = QLabel("")
		self.addChapterBtn = QPushButton()
		self.scrollArea = QScrollArea()
		self.containerWidget = QWidget()
		self.scrollArea.setWidget(self.containerWidget)
		self.scrollArea.setWidgetResizable(True)
		self.setPolicyScrollArea()

		self.chapterLayout = QVBoxLayout(self.containerWidget)
		self.setupLayout()
		self.setStyles()
		self.updateUIText()
		self.emitSignal()

	# Phụ trách khởi tạo ----------------------------------------------------
	def setTitle(self,tenMon):
		self.titleSubj.setText(tenMon)

	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(0)
		layout.addWidget(self.titleSubj)
		layout.addWidget(self.addChapterBtn)
		layout.addWidget(self.scrollArea)

		self.chapterLayout.addStretch()

	def setStyles(self):
		self.titleSubj.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.titleSubj.setProperty("type", "title")

	def updateUIText(self):
		self.addChapterBtn.setText(Text.ADD_CHAPTER_BTN)
		self.chapterList_refresh_request.emit()

	def setSubjId(self,maMon):
		self.subjId = maMon

	def setPolicyScrollArea(self):
		self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
		self.scrollArea.setWidgetResizable(True)
		self.containerWidget.setSizePolicy(
			QSizePolicy.Policy.Preferred,
			QSizePolicy.Policy.MinimumExpanding
		)
	# ------------------------------------------------------------------------


	# Phụ trách xử lý signal -------------------------------------------------
	def emitSignal(self):
		self.addChapterBtn.clicked.connect(self.createInputDialogAddChapter)

	def createInputDialogAddChapter(self):
		dialog = InputDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_THEMCHUONG)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			self.chapter_add_request.emit(self.subjId, dialog.textOutput())
	# ------------------------------------------------------------------------


	# Phụ trách hiển thị chapter block --------------------------------------- 
	def clearChapterLayout(self):
		for i in reversed(range(self.chapterLayout.count())):
			item = self.chapterLayout.itemAt(i)

			widget = item.widget()
			if widget is not None:
				widget.deleteLater()

		self.scrollArea.verticalScrollBar().setValue(0)

	def createChapterBlock(self, chuong):
		chapterBlock = ViewChapterBlock(chuong["tenChuong"], chuong["maChuong"])

		idx = self.chapterLayout.count() - 1
		self.chapterLayout.insertWidget(idx, chapterBlock)

		# print(f'Đã tạo chapter block có mã {chuong["maChuong"]}')
		return chapterBlock
	# ------------------------------------------------------------------------





		


