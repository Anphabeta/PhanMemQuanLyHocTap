from PyQt6.QtWidgets import(
	QWidget,
	QPushButton,
	QLabel,
	QHBoxLayout, QVBoxLayout,
	QLineEdit,
	QSizePolicy,
)
from PyQt6.QtCore import pyqtSignal, Qt
from lang.strings import Text


from View.ViewNoteBlock import ViewNoteBlock
from View.QDefine import NoteEdit

from debug.log_writer import log_view, plainLog

class ViewChapterBlock(QWidget):
	chapter_edit_request = pyqtSignal(int,str)
	chapter_delete_request = pyqtSignal(int)
	note_add_request = pyqtSignal(int, str, str, bool)

	def __init__(self,tenChuong,maChuong):
		super().__init__()
		self.chapterId = maChuong	

		self.titleArea = QWidget()
		self.titleChapterShow = QLabel(tenChuong)
		self.titleChapterEdit = QLineEdit()
		self.titleChapterEdit.hide()
		self.addNoteBtn = QPushButton()
		self.editChapterBtn = QPushButton()
		self.deleteChapterBtn = QPushButton()
		self.addNoteBtn.hide()
		self.editChapterBtn.hide()
		self.deleteChapterBtn.hide()

		self.tempInput = NoteEdit("", "disable")
		self.tempInput.hide()

		self.noteArea = QWidget()
		self.noteBlockList = []
		self.noteLayout = QVBoxLayout(self.noteArea)

		self.setLayout()
		self.setStyles()
		self.setSize()
		self.emitSignal()


	# Phụ trách khởi tạo --------------------------------------------------------
	def setLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.setContentsMargins(56,0,0,0)
		mainLayout.setSpacing(0)
		mainLayout.addWidget(self.titleArea)
		mainLayout.addWidget(self.noteArea)

		titleLayout = QHBoxLayout(self.titleArea)
		titleLayout.addWidget(self.titleChapterShow)
		titleLayout.addWidget(self.titleChapterEdit)
		titleLayout.addWidget(self.addNoteBtn)
		titleLayout.addWidget(self.editChapterBtn)
		titleLayout.addWidget(self.deleteChapterBtn)

	def setSize(self):
		self.addNoteBtn.setFixedWidth(100)
		self.editChapterBtn.setFixedWidth(100)
		self.deleteChapterBtn.setFixedWidth(100)

	def setStyles(self):
		self.titleChapterShow.setProperty("type", "chapter-title")
		self.titleChapterEdit.setProperty("type", "chapter-title")
		self.addNoteBtn.setProperty("type", "iconButton")
		self.editChapterBtn.setProperty("type", "iconButton")
		self.deleteChapterBtn.setProperty("type", "iconButton")
		self.addNoteBtn.setObjectName("new")
		self.editChapterBtn.setObjectName("edit")
		self.deleteChapterBtn.setObjectName("trash")

	def enterEvent(self, event):
		self.addNoteBtn.show()
		self.editChapterBtn.show()
		self.deleteChapterBtn.show()
		super().enterEvent(event)

	def leaveEvent(self, event):
		self.addNoteBtn.hide()
		self.editChapterBtn.hide()
		self.deleteChapterBtn.hide()
		super().leaveEvent(event)
	# ----------------------------------------------------------------------------


	# Phụ trách xử lý phát signal ------------------------------------------------
	def emitSignal(self):
		self.editChapterBtn.clicked.connect(self.openEditInline)
		self.titleChapterEdit.editingFinished.connect(self.handleSendChapterName)
		self.deleteChapterBtn.clicked.connect(self.handleDeleteChapter)
		self.addNoteBtn.clicked.connect(self.handleAddNote)
		self.tempInput.cancelEdit.connect(self.closeTemp)

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
			self.note_add_request.emit(self.chapterId, newText, "",  self.tempInput.getCheckBoxState())
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
		noteBlock = ViewNoteBlock(note["noiDung"], note["cauHoi"], note["maNote"], note["trangThaiThongBao"])

		idx = self.noteLayout.count()
		self.noteLayout.insertWidget(idx, noteBlock, 0, Qt.AlignmentFlag.AlignTop)

		# log_view(f"Đã tạo note block {note["maNote"]}")
		return noteBlock

	def setTempInput(self):
		self.noteLayout.addWidget(self.tempInput, 0, Qt.AlignmentFlag.AlignTop)

	def clearNoteLayout(self):
		for i in reversed(range(self.noteLayout.count())):
			item = self.noteLayout.itemAt(i)
			widget = item.widget()

			if widget is not None and widget != self.tempInput:
				self.noteLayout.removeWidget(widget)
				widget.deleteLater()
	# ----------------------------------------------------------------------------



		
			
