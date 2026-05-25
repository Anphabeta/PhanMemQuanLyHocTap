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
	QLabel,
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
	cancelEdit = pyqtSignal()

	def __init__(self, noiDungNote):
		super().__init__()

		self.textEdit = TextEdit(noiDungNote)

		self.checkBoxAndOKWidget = QWidget()
		self.checkBoxRecall = QCheckBox()
		self.checkBoxRecall.setChecked(True)
		self.okBtn = QPushButton("✔️")
		self.cancelBtn = QPushButton("❌")

		self.setupLayout()
		self.setIdQSS()
		self.updateUIText()
		self.emitSignal()

	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.textEdit)
		layout.addWidget(self.checkBoxAndOKWidget)

		checkBoxAndOKLayout = QHBoxLayout(self.checkBoxAndOKWidget)
		checkBoxAndOKLayout.addWidget(self.checkBoxRecall)
		checkBoxAndOKLayout.addWidget(self.okBtn)
		checkBoxAndOKLayout.addWidget(self.cancelBtn)

	def setIdQSS(self):
		self.okBtn.setProperty("type", "iconButton")
		self.cancelBtn.setProperty("type", "iconButton")

	def updateUIText(self):
		self.checkBoxRecall.setText(Text.CHECK_BOX_RECALL)

	def emitSignal(self):
		self.okBtn.clicked.connect(self.editingFinished.emit)
		self.cancelBtn.clicked.connect(self.cancelEdit.emit)
		self.checkBoxRecall.stateChanged.connect(self.stateChanged.emit)

	def setPlainText(self, newText):
		self.textEdit.setPlainText(newText)

	def setFocus(self):
		self.textEdit.setFocus()

	def toPlainText(self):
		return self.textEdit.toPlainText()

	def getCheckBoxState(self):
		return self.checkBoxRecall.isChecked()

class QuestionEdit(QWidget):
	question_send_request = pyqtSignal(int, str)

	def __init__(self, cauHoi, noteId):
		super().__init__()

		self.questionShowArea = QWidget()
		cauHoi = cauHoi if cauHoi != "" else Text.NOT_ADD_QUESTION
		self.questionShow = QLabel(cauHoi, self.questionShowArea)
		self.hideQuestionBtn = QPushButton("🔼", self.questionShowArea)
		self.editQuestionBtn = QPushButton("🖊️", self.questionShowArea)

		self.questionEditArea = QWidget()
		self.questionEdit = TextEdit(cauHoi, self.questionEditArea)
		self.okQuestionBtn = QPushButton("✔️", self.questionEditArea)
		self.cancelQuestionBtn = QPushButton("❌", self.questionEditArea)
		self.questionEditArea.hide()

		self.noteId = noteId

		self.setupLayout()
		self.setIdQSS()
		self.emitSignal()

	def setupLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.addWidget(self.questionShowArea)
		mainLayout.addWidget(self.questionEditArea)

		questionShowLayout = QVBoxLayout(self.questionShowArea)
		questionShowLayout.addWidget(self.questionShow)
		btnsShow = QWidget()
		btnsShowLayout = QHBoxLayout(btnsShow)
		btnsShowLayout.addStretch()
		btnsShowLayout.addWidget(self.hideQuestionBtn)
		btnsShowLayout.addWidget(self.editQuestionBtn)
		questionShowLayout.addWidget(btnsShow)

		questionEditLayout = QVBoxLayout(self.questionEditArea)
		questionEditLayout.addWidget(self.questionEdit)
		btnsEdit = QWidget()
		btnsEditLayout = QHBoxLayout(btnsEdit)
		btnsEditLayout.addStretch()
		btnsEditLayout.addWidget(self.okQuestionBtn)
		btnsEditLayout.addWidget(self.cancelQuestionBtn)
		questionEditLayout.addWidget(btnsEdit)

	def setIdQSS(self):
		self.hideQuestionBtn.setProperty("type", "iconButton")
		self.editQuestionBtn.setProperty("type", "iconButton")
		self.okQuestionBtn.setProperty("type", "iconButton")
		self.cancelQuestionBtn.setProperty("type", "iconButton")

	def emitSignal(self):
		self.hideQuestionBtn.clicked.connect(self.hideQuestion)
		self.editQuestionBtn.clicked.connect(self.openEditQuestion)
		self.okQuestionBtn.clicked.connect(self.handleSendQuestion)
		self.cancelQuestionBtn.clicked.connect(self.closeEditQuestion)		

	def openEditQuestion(self):
		self.questionShowArea.hide()
		self.questionEditArea.show()
		self.questionEdit.setPlainText(self.questionShow.text())
		self.questionEdit.show()
		self.questionEdit.setFocus()
		self.questionEdit.selectAll()

	def closeEditQuestion(self):
		self.questionShowArea.show()
		self.questionEditArea.hide()

	def hideQuestion(self):
		self.hide()

	def showQuestion(self):
		self.show()

	def handleSendQuestion(self):
		oldQuestion = self.questionShow.text()
		newQuestion = self.questionEdit.toPlainText()

		if newQuestion != oldQuestion:
			self.question_send_request.emit(self.noteId, newQuestion)
		else:
			self.closeEditQuestion()

	def setText(self, cauHoi):
		self.questionShow.setText(cauHoi)


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


class ViewSettingDialog(QDialog):
	def __init__(self):
		super().__init__()

		self.mainArea = QWidget()
		self.language = QWidget(self.mainArea)
		self.languageTitle = QLabel(Text.CHOOSE_LANGUAGE, self.language)
		self.comboBoxLang = QComboBox(self.language)
		self.comboBoxLang.addItem(Text.VIETNAMESE, "vi")
		self.comboBoxLang.addItem(Text.ENGLISH, "en")


		self.theme = QWidget()
		self.themeTitle = QLabel(Text.CHOOSE_THEME, self.theme)

		self.applyBtn = QPushButton(Text.OK)
		self.cancelBtn = QPushButton(Text.CANCEL)

		self.settingObj = {}

		self.setFixedSize(400, 200)
		self.setupLayout()
		self.emitSignal()

	def setupLayout(self):
		mainLayout = QVBoxLayout(self)

		languageLayout = QVBoxLayout(self.language)
		languageLayout.addWidget(self.languageTitle)
		languageLayout.addWidget(self.comboBoxLang)

		themeLayout = QVBoxLayout(self.theme)
		themeLayout.addWidget(self.themeTitle)

		btnsArea = QWidget()
		btnsAreaLayout = QHBoxLayout(btnsArea)
		btnsAreaLayout.addStretch()
		btnsAreaLayout.addWidget(self.applyBtn)
		btnsAreaLayout.addWidget(self.cancelBtn)

		mainLayout.addWidget(self.language)
		mainLayout.addWidget(self.theme)
		mainLayout.addStretch()
		mainLayout.addWidget(btnsArea)

	def emitSignal(self):
		self.applyBtn.clicked.connect(self.accept)
		self.cancelBtn.clicked.connect(self.reject)

	def setState(self, data):
		self.settingObj = data
		
		index = self.comboBoxLang.findData(data['lang'])
		if index != -1:
		    self.comboBoxLang.setCurrentIndex(index)

	def updateState(self):
		self.settingObj['lang'] = self.comboBoxLang.currentData()

	def getData(self):
		return self.settingObj



