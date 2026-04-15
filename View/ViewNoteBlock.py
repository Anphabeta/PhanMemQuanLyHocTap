from PyQt6.QtWidgets import (
	QWidget, 
	QPlainTextEdit,
	QPushButton,
	QLabel,
	QHBoxLayout, QVBoxLayout
)
from PyQt6.QtCore import pyqtSignal, Qt

from debug.log_writer import log_view, plainLog

class NoteEdit(QPlainTextEdit):
	editingFinished = pyqtSignal()

	def focusOutEvent(self, event):
		super().focusOutEvent(event)
		self.editingFinished.emit()
		
class ViewNoteBlock(QWidget):
	note_edit_request = pyqtSignal(int,str)
	note_delete_request = pyqtSignal(int)
	note_moveUp_request = pyqtSignal(int)
	note_moveDown_request = pyqtSignal(int)
	note_create_request = pyqtSignal()

	def __init__(self, noiDungNote, maNote):
		super().__init__()
		self.noteId = maNote

		self.textArea = QWidget()
		self.noteShow = QLabel(noiDungNote)
		self.noteEdit = NoteEdit(noiDungNote)
		self.noteEdit.hide()

		self.hoverBtns = QWidget()
		self.addNoteBtn = QPushButton("➕")
		self.deleteNoteBtn = QPushButton("🗑️")
		self.editNoteBtn = QPushButton("🖊️")
		self.moveUpBtn = QPushButton("⬆️")
		self.moveDownBtn = QPushButton("⬇️")
		self.moreOptionBtn = QPushButton("⛏️")

		self.addNoteBtn.hide()
		self.moreOptionBtn.hide()

		self.setupLayout()
		self.setSize(30)
		self.setAlign()
		self.emitSignal()


	# Phụ trách khởi tạo --------------------------------------------
	def setupLayout(self):
		mainLayout = QHBoxLayout(self)
		mainLayout.addWidget(self.hoverBtns)
		mainLayout.addWidget(self.textArea,1)

		hoverBtnsLayout = QVBoxLayout(self.hoverBtns)
		hoverBtnsLayout.addWidget(self.addNoteBtn)
		hoverBtnsLayout.addWidget(self.deleteNoteBtn)
		hoverBtnsLayout.addWidget(self.editNoteBtn)
		hoverBtnsLayout.addWidget(self.moveUpBtn)
		hoverBtnsLayout.addWidget(self.moveDownBtn)
		hoverBtnsLayout.addWidget(self.moreOptionBtn)

		textAreaLayout = QVBoxLayout(self.textArea)
		textAreaLayout.addWidget(self.noteShow)
		textAreaLayout.addWidget(self.noteEdit)

	def setSize(self, width):
		self.addNoteBtn.setFixedWidth(width)
		self.deleteNoteBtn.setFixedWidth(width)
		self.editNoteBtn.setFixedWidth(width)
		self.moveUpBtn.setFixedWidth(width)
		self.moveDownBtn.setFixedWidth(width)
		self.moreOptionBtn.setFixedWidth(width)

		self.noteShow.setWordWrap(True)

	def setAlign(self):
		self.noteShow.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)	
	# ---------------------------------------------------------------


	# Phụ trách phát tín hiệu ---------------------------------------
	def emitSignal(self):
		self.addNoteBtn.clicked.connect(self.handleAddNote)
		self.deleteNoteBtn.clicked.connect(self.handleDeleteNote)
		self.editNoteBtn.clicked.connect(self.openEditInline)
		self.noteEdit.editingFinished.connect(self.handleSendNote)
		self.moveUpBtn.clicked.connect(self.handleMoveUp)
		self.moveDownBtn.clicked.connect(self.handleMoveDown)
		self.moreOptionBtn.clicked.connect(self.handleMoreOption)

	def handleAddNote(self):
		plainLog("add note event")

		log_view("Phát tín hiệu")
		self.note_create_request.emit()

	def handleDeleteNote(self):
		plainLog("deleta note event")

		log_view("Phát tín hiệu")
		self.note_delete_request.emit(self.noteId)

	def handleMoveUp(self):
		plainLog("move up note event")

		log_view("Phát tín hiệu")
		self.note_moveUp_request.emit(self.noteId)

	def handleMoveDown(self):
		plainLog("move down note event")

		log_view("Phát tín hiệu")
		self.note_moveDown_request.emit(self.noteId)

	def handleMoreOption(self):
		pass

	def openEditInline(self):
		self.noteShow.hide()
		self.noteEdit.setPlainText(self.noteShow.text())
		self.noteEdit.show()
		self.noteEdit.setFocus()

	def closeEditInline(self):
		self.noteShow.show()
		self.noteEdit.hide()

	def handleSendNote(self):
		oldText = self.noteShow.text()
		newText = self.noteEdit.toPlainText()

		if newText != "" and newText != oldText:
			self.note_edit_request.emit(self.noteId, newText)
		else:
			self.closeEditInline()
	# ---------------------------------------------------------------


	# Phụ trách nhận tín hiệu ---------------------------------------
	def handleReceiveNote(self, note):
		self.noteShow.setText(note)
		self.closeEditInline()
	# ---------------------------------------------------------------




	
