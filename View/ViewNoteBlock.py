from PyQt6.QtWidgets import (
	QWidget, 
	QPushButton,
	QLabel,
	QHBoxLayout, QVBoxLayout,
	QMenu,
	QSizePolicy,
	QStyle, QStyleOption,
)
from PyQt6.QtGui import QAction, QPainter, QIcon
from PyQt6.QtCore import pyqtSignal, Qt

from debug.log_writer import log_view, plainLog
from View.QDefine import NoteEdit, TextEdit, QuestionEdit
from lang.strings import Text
from styles.get_styles import get_resource_path
		
class ViewNoteBlock(QWidget):
	note_edit_request = pyqtSignal(int,str)
	note_delete_request = pyqtSignal(int)
	note_moveUp_request = pyqtSignal(int)
	note_moveDown_request = pyqtSignal(int)
	note_create_request = pyqtSignal()
	note_change_recallState = pyqtSignal(int, int)
	question_edit_request = pyqtSignal(int, str)

	def __init__(self, noiDungNote, cauHoi, maNote, isNhacLai):
		super().__init__()
		self.noteId = maNote

		self.textArea = QWidget()
		self.noteShow = QLabel(noiDungNote)
		self.noteEdit = NoteEdit(noiDungNote, isNhacLai)
		self.noteEdit.hide()

		self.questionArea = QuestionEdit(cauHoi, maNote)
		self.questionArea.hide()

		self.hoverBtns = QWidget()
		self.questionBtn = QPushButton()
		self.moreOptionBtn = QPushButton()

		self.optionMenu = QMenu(self.hoverBtns)
		self.editNoteAction = QAction(QIcon(get_resource_path("assets/edit.ico")), Text.NOTE_EDIT_BTN, self.hoverBtns)
		self.deleteNoteAction = QAction(QIcon(get_resource_path("assets/trash.ico")), Text.NOTE_DELETE_BTN, self.hoverBtns)
		self.moveUpAction = QAction(QIcon(get_resource_path("assets/up.ico")), Text.NOTE_MOVEUP_BTN, self.hoverBtns)
		self.moveDownAction = QAction(QIcon(get_resource_path("assets/down.ico")), Text.NOTE_MOVEDOWN_BTN, self.hoverBtns)
		self.addAction()
		self.moreOptionBtn.setMenu(self.optionMenu)

		# self.addNoteBtn = QPushButton("➕")

		sp1 = self.questionBtn.sizePolicy()
		sp1.setRetainSizeWhenHidden(True)
		self.questionBtn.setSizePolicy(sp1)

		sp2 = self.moreOptionBtn.sizePolicy()
		sp2.setRetainSizeWhenHidden(True)
		self.moreOptionBtn.setSizePolicy(sp2)

		self.questionBtn.hide()
		self.moreOptionBtn.hide()

		self.setupLayout()
		self.setStyles()
		self.setAlign()
		self.emitSignal()


	# Phụ trách khởi tạo --------------------------------------------
	def setupLayout(self):
		mainLayout = QHBoxLayout(self)
		mainLayout.setContentsMargins(16, 0, 0, 0)
		mainLayout.setSpacing(0)
		mainLayout.addWidget(self.textArea,1)
		mainLayout.addWidget(self.hoverBtns)

		hoverBtnsLayout = QVBoxLayout(self.hoverBtns)
		hoverBtnsLayout.setContentsMargins(0,0,0,0)
		hoverBtnsLayout.setSpacing(0)
		hoverArea = QWidget()
		hoverAreaLayout = QHBoxLayout(hoverArea)
		hoverAreaLayout.setContentsMargins(0,0,0,0)
		hoverAreaLayout.setSpacing(0)
		hoverAreaLayout.addWidget(self.questionBtn)
		hoverAreaLayout.addWidget(self.moreOptionBtn)

		hoverBtnsLayout.addWidget(hoverArea)
		hoverBtnsLayout.addStretch()
		
		textAreaLayout = QVBoxLayout(self.textArea)
		textAreaLayout.setContentsMargins(0,0,0,0)
		textAreaLayout.setSpacing(8)
		textAreaLayout.addWidget(self.noteShow)
		textAreaLayout.addWidget(self.noteEdit)
		textAreaLayout.addWidget(self.questionArea)
		textAreaLayout.addStretch()

	def paintEvent(self, event):
		opt = QStyleOption()
		opt.initFrom(self)
		p = QPainter(self)
		self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)

	def setStyles(self):
		self.questionBtn.setProperty("type", "iconButton")
		self.moreOptionBtn.setProperty("type", "iconButton")

		self.questionBtn.setObjectName("question")
		self.moreOptionBtn.setObjectName("h-dots")
		self.noteShow.setWordWrap(True)

	def addAction(self):
		self.optionMenu.addAction(self.editNoteAction)
		self.optionMenu.addAction(self.deleteNoteAction)
		self.optionMenu.addAction(self.moveUpAction)
		self.optionMenu.addAction(self.moveDownAction)

	def setAlign(self):
		self.noteShow.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)	

	def enterEvent(self, event):
		self.questionBtn.show()
		self.moreOptionBtn.show()
		super().enterEvent(event)

	def leaveEvent(self, event):
		self.questionBtn.hide()
		self.moreOptionBtn.hide()
		super().leaveEvent(event)
	# ---------------------------------------------------------------


	# Phụ trách phát tín hiệu ---------------------------------------
	def emitSignal(self):
		# self.addNoteBtn.clicked.connect(self.handleAddNote)
		self.deleteNoteAction.triggered.connect(self.handleDeleteNote)
		self.editNoteAction.triggered.connect(self.openEditInline)
		self.noteEdit.editingFinished.connect(self.handleSendNote)
		self.noteEdit.stateChanged.connect(self.handleChangeRecallState)
		self.noteEdit.cancelEdit.connect(self.closeEditInline)
		self.moveUpAction.triggered.connect(self.handleMoveUp)
		self.moveDownAction.triggered.connect(self.handleMoveDown)
		self.questionBtn.clicked.connect(self.questionArea.showQuestion)
		self.questionArea.question_send_request.connect(self.question_edit_request.emit)


	# def handleAddNote(self):
	# 	plainLog("add note event")

	# 	log_view("Phát tín hiệu")
	# 	self.note_create_request.emit()

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

	def handleChangeRecallState(self, state):
		plainLog("change recall state event")

		log_view("Phát tín hiệu")
		self.note_change_recallState.emit(self.noteId, state)	
	# ---------------------------------------------------------------


	# Phụ trách nhận tín hiệu ---------------------------------------
	def handleReceiveNote(self, note):
		self.noteShow.setText(note)
		self.closeEditInline()

	def handleReceiveQuestion(self, cauHoi):
		self.questionArea.setText(cauHoi)
		self.questionArea.closeEditQuestion()
	# ---------------------------------------------------------------




	
