from PyQt6.QtWidgets import(
	QDialog,
	QWidget,
	QPushButton,
	QLineEdit,
	QVBoxLayout,
	QHBoxLayout,
	QPlainTextEdit,
	QCheckBox,
	QComboBox,
	QLabel
)
from PyQt6.QtCore import Qt, pyqtSignal

from lang.strings import Text
from View.QDefine import TextEdit, InputDialog
from debug.log_writer import log_view, plainLog


class ViewReviewDialog(QDialog):
	def __init__(self, noiDungNote, cauHoi, noteId):
		super().__init__()
		#
		self.setWindowTitle(Text.DIALOG_TITLE_ONTAP)
		#
		self.note = QLabel(noiDungNote)
		self.question = QLabel(cauHoi)
		self.flipBtn = QPushButton(Text.FLIP)
		self.flipState = False
		#
		self.judgeYourSelf = QLabel(Text.JUDGE_YOUR_SELF)
		self.scoreBtnList = []
		for i in range(0,6):
			scoreBtn = QPushButton(Text.SCORE_BTN[i])
			scoreBtn.setProperty("score", i)

			self.scoreBtnList.append(scoreBtn)
		#
		self.noteId = noteId
		#
		self.setFixedSize(700,400)
		self.setupLayout()
		self.emitSignal()
		#
		self.showTag()


	def getNoteId(self):
		return self.noteId

	def getDiem(self):
		return self.diem

	def setupLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.addWidget(self.note)
		mainLayout.addWidget(self.question)
		mainLayout.addWidget(self.flipBtn)
		mainLayout.addWidget(self.judgeYourSelf)
		for scoreBtn in self.scoreBtnList:
			mainLayout.addWidget(scoreBtn)

		mainLayout.addStretch()

	def emitSignal(self):
		self.flipBtn.clicked.connect(self.flip)
		for scoreBtn in self.scoreBtnList:
			scoreBtn.clicked.connect(lambda check=False,diem=scoreBtn.property("score"): self.handleSendScore(diem))

	def flip(self):
		self.flipState = not self.flipState
		self.showTag()

	def showTag(self):
		if(self.question.text().strip() == ""): 
			self.flipBtn.setEnabled(False)
			self.flipState = True

		if self.flipState:
			self.note.show()
			self.question.hide()
		else:
			self.note.hide()
			self.question.show()

	def handleSendScore(self, diem):
		self.diem = diem
		self.accept()


class ViewReviewTag(QWidget):
	clicked = pyqtSignal(int)

	def __init__(self, tenMon, tenChuong, maNote, cauHoi, noiDungNote):
		super().__init__()

		path = f"{tenMon} > {tenChuong}"
		self.path = QLabel(path)
		
		if cauHoi.strip() == "":
			brief = noiDungNote[:100] + "..." if len(noiDungNote)>100 else noiDungNote
		else:
			brief = cauHoi[:100] + "..." if len(cauHoi)>100 else cauHoi
		self.brief = QLabel(brief)

		self.hovered = False
		self.pressed = False
		self.setMouseTracking(True)

		self.noteId = maNote

		self.setupLayout()

	def setupLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.addWidget(self.path)
		mainLayout.addWidget(self.brief)
		self.makeChildrenTransparent()

	def enterEvent(self, event):
		self.hovered = True
		self.update()

	def leaveEvent(self, event):
		self.hovered = False
		self.pressed = False
		self.update()

	def mousePressEvent(self, event):
		if event.button() == Qt.MouseButton.LeftButton:
			self.pressed = True
			self.update()

	def mouseReleaseEvent(self, event):
		if self.pressed:
			self.pressed = False
			self.update()

			if self.rect().contains(event.pos()):
				self.clicked.emit(self.noteId)

	def makeChildrenTransparent(self):
		for child in self.findChildren(QWidget):
			child.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
	

	