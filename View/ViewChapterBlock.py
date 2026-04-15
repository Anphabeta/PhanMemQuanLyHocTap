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
from View.ViewNoteBlock import NoteEdit

from debug.log_writer import log_view, plainLog

class ViewChapterBlock(QWidget):
	chapter_edit_request = pyqtSignal(int,str)
	chapter_delete_request = pyqtSignal(int)
	note_add_request = pyqtSignal(int, str)

	def __init__(self,tenChuong,maChuong):
		super().__init__()
		self.chapterId = maChuong	

		self.titleArea = QWidget()
		self.titleChapterShow = QLabel(tenChuong)
		self.titleChapterEdit = QLineEdit()
		self.titleChapterEdit.hide()
		self.addNoteBtn = QPushButton(Icon.ADD_NOTE_BTN)
		self.editChapterBtn = QPushButton(Icon.EDIT_CHAPTER_BTN)
		self.deleteChapterBtn = QPushButton(Icon.DELETE_CHAPTER_BTN)

		self.tempInput = NoteEdit("")
		self.tempInput.hide()

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

		self.noteLayout.addWidget(self.tempInput)

	def setSize(self):
		self.addNoteBtn.setFixedWidth(100)
		self.editChapterBtn.setFixedWidth(100)
		self.deleteChapterBtn.setFixedWidth(100)
	# ----------------------------------------------------------------------------


	# Phụ trách xử lý phát signal ------------------------------------------------
	def emitSignal(self):
		self.editChapterBtn.clicked.connect(self.openEditInline)
		self.titleChapterEdit.editingFinished.connect(self.handleSendChapterName)
		self.deleteChapterBtn.clicked.connect(self.handleDeleteChapter)
		self.addNoteBtn.clicked.connect(self.handleAddNote)

		self.tempInput.editingFinished.connect(self.checkCondition)

	def openEditInline(self):
		plainLog("EDIT CHAPTER EVENT")
		log_view("Handle open edit in line")
		self.titleChapterShow.hide()
		self.titleChapterEdit.setText(self.titleChapterShow.text())
		self.titleChapterEdit.show()
		self.titleChapterEdit.setFocus()
		self.titleChapterEdit.selectAll()

	def handleSendChapterName(self):
		oldText = self.titleChapterShow.text()
		newText = self.titleChapterEdit.text().strip()

		if newText != "" and newText != oldText:
			log_view("Handle send new chapter name")
			self.chapter_edit_request.emit(self.chapterId, newText)
		else:
			self.closeEditInline()
		
	def handleDeleteChapter(self):
		plainLog("delete chapter event")
		log_view("Handle delete chapter")
		self.chapter_delete_request.emit(self.chapterId)

	def handleAddNote(self):
		plainLog("add note event")
		log_view("Handle add note")
		self.tempInput.show()
		self.tempInput.setFocus()

	def checkCondition(self):
		newText = self.tempInput.toPlainText().strip()

		if newText != "":
			self.note_add_request.emit(self.chapterId, newText)
		self.closeTemp()
			
	def closeTemp(self):
		self.tempInput.setPlainText("")
		self.tempInput.hide()
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
		noteBlock = ViewNoteBlock(note["noiDung"], note["maNote"])

		idx = self.noteLayout.count()
		self.noteLayout.insertWidget(idx, noteBlock)

		# log_view(f"Đã tạo note block {note["maNote"]}")
		return noteBlock

	def clearNoteLayout(self):
		for i in reversed(range(self.noteLayout.count())):
			item = self.noteLayout.itemAt(i)
			widget = item.widget()

			if widget is not None and widget != self.tempInput:
				self.noteLayout.removeWidget(widget)
				widget.deleteLater()
	# ----------------------------------------------------------------------------



		
			
