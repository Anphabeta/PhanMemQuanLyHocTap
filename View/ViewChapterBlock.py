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

from View.ViewNoteBlock import ViewNoteBlock

class ViewChapterBlock(QWidget):
	chapter_edit_request = pyqtSignal(int,str)
	chapter_delete_request = pyqtSignal(int)

	def __init__(self,tenChuong):
		super().__init__()

		self.titleArea = QWidget()
		self.titleChapterShow = QLabel(tenChuong)
		self.titleChapterEdit = QLineEdit()
		self.titleChapterEdit.hide()
		self.addNoteBtn = QPushButton(Icon.ADD_NOTE_BTN)
		self.editChapterBtn = QPushButton(Icon.EDIT_CHAPTER_BTN)
		self.deleteChapterBtn = QPushButton(Icon.DELETE_CHAPTER_BTN)

		self.noteArea = QWidget()
		self.noteBlockList = []
		self.noteLayout = QVBoxLayout(self.noteArea)

		self.setLayout()
		self.setSize()
		self.emitSignal()


	# Phụ trách khởi tạo --------------------------------------------------------
	def setLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.addWidget(self.titleArea)
		mainLayout.addWidget(self.noteArea)

		titleLayout = QHBoxLayout(self.titleArea)
		titleLayout.addWidget(self.titleChapterShow)
		titleLayout.addWidget(self.titleChapterEdit)
		titleLayout.addWidget(self.addNoteBtn)
		titleLayout.addWidget(self.editChapterBtn)
		titleLayout.addWidget(self.deleteChapterBtn)


		print("Đã setup layout chapter Block")

	def setSize(self):
		self.addNoteBtn.setFixedWidth(100)
		self.editChapterBtn.setFixedWidth(100)
		self.deleteChapterBtn.setFixedWidth(100)

	def setChapterId(self, maChuong):
		self.chapterId = maChuong	
	# ----------------------------------------------------------------------------


	# Phụ trách xử lý phát signal ------------------------------------------------
	def emitSignal(self):
		self.editChapterBtn.clicked.connect(self.openEditInline)
		self.titleChapterEdit.editingFinished.connect(self.handleSendChapterName)
		self.deleteChapterBtn.clicked.connect(self.handleDeleteChapter)

	def openEditInline(self):
		self.titleChapterShow.hide()
		self.titleChapterEdit.setText(self.titleChapterShow.text())
		self.titleChapterEdit.show()
		self.titleChapterEdit.setFocus()
		self.titleChapterEdit.selectAll()

	def handleSendChapterName(self):
		oldText = self.titleChapterShow.text()
		newText = self.titleChapterEdit.text().strip()

		if newText != "" and newText != oldText:
			self.chapter_edit_request.emit(self.chapterId, newText)
		else:
			self.closeEditInline()
		
	def handleDeleteChapter(self):
		self.chapter_delete_request.emit(self.chapterId)
	# ----------------------------------------------------------------------------


	# Phụ trách xử lý nhận signal ------------------------------------------------
	def handleReceiveChapterName(self, newName):
		self.titleChapterShow.setText(newName)
		self.titleChapterEdit.setText(newName)
		self.closeEditInline()

	def closeEditInline(self):
		self.titleChapterShow.show()
		self.titleChapterEdit.hide()
	# ----------------------------------------------------------------------------


	# Phụ trách hiển thị note block ----------------------------------------------
	def createNoteBlock(self, note):
		noteBlock = ViewNoteBlock(note["noiDung"])
		noteBlock.setNoteId(note["maNote"])

		idx = self.noteLayout.count() - 1
		self.noteLayout.insertWidget(idx, noteBlock)

		print("Đã tạo note block")
		return noteBlock

	def clearNoteLayout(self):
		for i in reversed(range(self.noteLayout.count())):
			item = self.noteLayout.itemAt(i)

			widget = item.widget()
			if widget is not None:
				widget.deleteLater()
	# ----------------------------------------------------------------------------



		
			
