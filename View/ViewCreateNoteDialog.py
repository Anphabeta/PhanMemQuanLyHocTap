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
from View.QDefine import TextEdit, InputDialog
from debug.log_writer import log_view, plainLog


class ViewCreateNoteDialog(QDialog):
	subjList_get_request = pyqtSignal() # Dùng để yêu cầu controller gửi danh sách môn học
	chapterList_get_request = pyqtSignal(int) # Dùng để yêu cầu controller gửi danh sách chương
	subject_choose_request = pyqtSignal(int) # Dùng để xử lý việc hiển thị chapter list mỗi khi đổi một môn học


	def __init__(self):
		super().__init__()
		#
		self.inputText = TextEdit("")

		self.checkBoxRecall = QCheckBox(Text.CHECK_BOX_RECALL)
		self.checkBoxRecall.setChecked(True)

		self.comboBoxSubj = QComboBox()
		self.showComboBoxSubj()
		self.comboBoxChapter = QComboBox()
		self.showComboBoxChapter()

		self.btnWidgets = QWidget()
		self.okBtn = QPushButton(Text.OK)
		self.okBtn.setEnabled(False)
		self.cancelBtn = QPushButton(Text.CANCEL)
		#
		self.subjId = None
		self.chapterId = None
		#
		self.newSubjectText = None
		self.newChapterText = None
		#
		self.setFixedSize(700,400)
		self.setupLayout()
		self.emitSignal()

	def setupLayout(self):
		mainLayout = QVBoxLayout(self)
		mainLayout.addWidget(self.inputText)
		mainLayout.addWidget(self.checkBoxRecall)
		mainLayout.addWidget(self.comboBoxSubj)
		mainLayout.addWidget(self.comboBoxChapter)
		mainLayout.addWidget(self.btnWidgets)
		# mainLayout.addStretch()
		#
		btnLayout = QHBoxLayout(self.btnWidgets)
		btnLayout.addWidget(self.okBtn)
		btnLayout.addWidget(self.cancelBtn)

	def emitSignal(self):
		self.comboBoxSubj.activated.connect(self.handleChooseSubject)
		self.comboBoxChapter.activated.connect(self.handleChooseChapter)
		self.inputText.textChanged.connect(self.checkOKBtn)
		self.comboBoxSubj.activated.connect(self.checkOKBtn)
		self.comboBoxChapter.activated.connect(self.checkOKBtn)

		self.okBtn.clicked.connect(self.accept)
		self.cancelBtn.clicked.connect(self.reject)

	def dataOutput(self):
		data = {
			"subject":{
				"id": self.subjId,
				"text": self.newSubjectText,
			},
			"chapter":{
				"id": self.chapterId,
				"text": self.newChapterText,
			},
			"note":{
				"content": self.inputText.toPlainText().strip(),
				"isRecall": self.checkBoxRecall.isChecked(),
			},
		}

		return data

	def checkOKBtn(self):
		check = True
		check = check and self.inputText.toPlainText().strip() != ""
		check = check and self.comboBoxSubj.currentText() not in (Text.CHOOSE_SUBJECT_TEXT, Text.CREATE_SUBJECT_TEXT)
		check = check and self.comboBoxChapter.currentText() not in (Text.CHOOSE_SUBJECT_FIRST, Text.CHOOSE_CHAPTER_TEXT, Text.CREATE_CHAPTER_TEXT)

		self.okBtn.setEnabled(check)
    # ------------------------------------------------------------------------
	def showComboBoxSubj(self): # Hàm này để phát yêu cầu được lấy thông tin để hiển thị khi khởi tạo
		plainLog("get combobox subject list event")
		log_view("Phát tín hiệu")
		self.subjList_get_request.emit()

	def handleGetSubjList(self, subjList): # Hàm này sẽ gọi bên ngoài dùng để hiển thị comboBox subjList
		log_view("Đã nhận subject list từ controller")
		self.comboBoxSubj.addItem(Text.CHOOSE_SUBJECT_TEXT, None)

		for subj in subjList:
			self.comboBoxSubj.addItem(subj["tenMon"], subj["maMon"])

		self.comboBoxSubj.addItem(Text.CREATE_SUBJECT_TEXT, None)

	def handleChooseSubject(self, index): # Hàm này để gọi mỗi lần người dùng chọn một môn học nào đó
		plainLog("choose subject event")
		log_view("Lấy mã môn và phát tín hiệu")
		maMon = self.comboBoxSubj.itemData(index)
		tenMon = self.comboBoxSubj.itemText(index)
		self.subjId = maMon
		if tenMon == Text.CREATE_SUBJECT_TEXT:
			self.handleCreateAddSubjectDialog()
		elif tenMon == Text.CHOOSE_SUBJECT_TEXT:
			self.comboBoxChapter.clear()
			self.comboBoxChapter.addItem(Text.CHOOSE_SUBJECT_FIRST, None)
		else:
			self.chapterList_get_request.emit(maMon)
			
	def handleCreateAddSubjectDialog(self):
		plainLog("add subject event")
		log_view("Tạo dialog")
		dialog = InputDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_THEMMON)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			self.newSubjectText = dialog.textOutput()
			self.comboBoxSubj.clear()
			self.comboBoxSubj.addItem(self.newSubjectText, None)

			self.comboBoxChapter.clear()
			self.comboBoxChapter.addItem(Text.CREATE_CHAPTER_TEXT, None)
	# ------------------------------------------------------------------------

	def showComboBoxChapter(self): # Hàm này để phát yêu cầu được lấy thông tin để hiển thị khi khởi tạo
		plainLog("show combobox chapter event")
		log_view("Phát tín hiệu chứa mã môn")
		self.comboBoxChapter.addItem(Text.CHOOSE_SUBJECT_FIRST, None)
		# self.subject_choose_request.emit(maMon)

	def handleGetChapterList(self, chapterList): # Hàm này sẽ gọi bên ngoài dùng để hiển thị comboBox chapterList
		log_view("Đã nhận chapter list từ controller")
		self.comboBoxChapter.clear()
		self.comboBoxChapter.addItem(Text.CHOOSE_CHAPTER_TEXT, None)

		for chapter in chapterList:
			self.comboBoxChapter.addItem(chapter["tenChuong"], chapter["maChuong"])

		self.comboBoxChapter.addItem(Text.CREATE_CHAPTER_TEXT, None)

	def handleChooseChapter(self, index): # Hàm này để gọi mỗi lần người dùng chọn một chương nào đó
		plainLog("choose chapter event")
		log_view("Lấy mã chương")
		maChuong = self.comboBoxChapter.itemData(index)
		tenChuong = self.comboBoxChapter.itemText(index)
		self.chapterId = maChuong
		if tenChuong == Text.CREATE_CHAPTER_TEXT:
			self.handleCreateAddChapterDialog()

	def handleCreateAddChapterDialog(self):
		plainLog("add subject event")
		log_view("Tạo dialog")
		dialog = InputDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_THEMMON)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			self.newChapterText = dialog.textOutput()
			self.comboBoxChapter.clear()
			self.comboBoxChapter.addItem(self.newChapterText, None)