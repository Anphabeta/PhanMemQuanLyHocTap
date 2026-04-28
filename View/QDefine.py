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
)
from PyQt6.QtCore import pyqtSignal

from lang.strings import Text


class TextEdit(QPlainTextEdit):
	editingFinished = pyqtSignal()

	def focusOutEvent(self, event):
		super().focusOutEvent(event)
		self.editingFinished.emit()	

	def hasText(self):
		text = self.toPlainText().strip()
		return text != ""

class NoteEdit(QWidget):
	editingFinished = pyqtSignal()
	stateChanged = pyqtSignal(int)

	def __init__(self, noiDungNote):
		super().__init__()

		self.textEdit = TextEdit(noiDungNote)

		self.checkBoxAndOKWidget = QWidget()
		self.checkBoxRecall = QCheckBox(Text.CHECK_BOX_RECALL)
		self.checkBoxRecall.setChecked(True)
		self.okBtn = QPushButton("✔️")

		self.setupLayout()
		self.emitSignal()

	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.textEdit)
		layout.addWidget(self.checkBoxAndOKWidget)

		checkBoxAndOKLayout = QHBoxLayout(self.checkBoxAndOKWidget)
		checkBoxAndOKLayout.addWidget(self.checkBoxRecall)
		checkBoxAndOKLayout.addWidget(self.okBtn)

	def emitSignal(self):
		self.okBtn.clicked.connect(self.editingFinished.emit)
		self.checkBoxRecall.stateChanged.connect(self.stateChanged.emit)

	def setPlainText(self, newText):
		self.textEdit.setPlainText(newText)

	def setFocus(self):
		self.textEdit.setFocus()

	def toPlainText(self):
		return self.textEdit.toPlainText()

	def getCheckBoxState(self):
		return self.checkBoxRecall.isChecked()



class InputDialog(QDialog):
	def __init__(self):
		super().__init__()
		#
		self.inputText = QLineEdit()
		self.btnWidgets = QWidget()
		self.okBtn = QPushButton(Text.OK)
		self.okBtn.setEnabled(False)
		self.cancelBtn = QPushButton(Text.CANCEL)
		#
		self.setFixedSize(400,200)
		self.setupLayout()
		self.setupConnectBtn()

	def setupLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.addWidget(self.inputText)
		mainLayout.addWidget(self.btnWidgets)
		mainLayout.addStretch()
		#
		btnLayout = QHBoxLayout(self.btnWidgets)
		btnLayout.addWidget(self.okBtn)
		btnLayout.addWidget(self.cancelBtn)

	def setupConnectBtn(self):
		self.inputText.textChanged.connect(self.checkOKBtn)
		self.okBtn.clicked.connect(self.accept)
		self.cancelBtn.clicked.connect(self.reject)

	def textOutput(self):
		return self.inputText.text()

	def checkOKBtn(self):
		self.okBtn.setEnabled(self.inputText.text().strip() != "")






