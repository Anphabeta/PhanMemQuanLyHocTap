from PyQt6.QtWidgets import(
	QWidget,
	QVBoxLayout,
	QHBoxLayout,
	QLabel,
	QPushButton,
	QScrollArea,
	QDialog,
)
from PyQt6.QtCore import pyqtSignal, Qt
from lang.strings import Text

from debug.log_writer import log_view, plainLog

from View.ViewCreateNoteDialog import ViewCreateNoteDialog
from View.ViewReviewDialog import ViewReviewTag, ViewReviewDialog
from View.QDefine import ViewSettingDialog

class ViewHomePage(QWidget):
	noteDialog_create_request = pyqtSignal()
	familyNote_create_request = pyqtSignal(object)
	settingDialog_open_request = pyqtSignal()

	def __init__(self):
		super().__init__()

		self.title = QLabel()

		self.createNoteBtn = QPushButton()
		self.settingBtn = QPushButton()

		self.scrollArea = QScrollArea()
		self.containerWidget = QWidget()
		self.scrollArea.setWidget(self.containerWidget)
		self.scrollArea.setWidgetResizable(True)

		self.reviewTagLayout = QVBoxLayout(self.containerWidget)

		self.settingBtn.setFixedWidth(30)
		self.setupLayout()
		self.setStyles()
		self.updateUIText()
		self.emitSignal()


	def setupLayout(self):
		layout = QVBoxLayout(self)
		firstLine = QWidget()
		firstLineLayout = QHBoxLayout(firstLine)
		firstLineLayout.addWidget(self.title)
		firstLineLayout.addWidget(self.settingBtn)
		layout.addWidget(firstLine)
		layout.addWidget(self.createNoteBtn)
		layout.addWidget(self.scrollArea)

		self.reviewTagLayout.addStretch()

	def setStyles(self):
		self.settingBtn.setProperty("type", "iconButton")
		self.settingBtn.setObjectName("setting")
		self.createNoteBtn.setObjectName("add-new-note")
		self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.title.setProperty("type", "title")

	def updateUIText(self):
		self.title.setText(Text.TITLE_HOMEPAGE)
		self.createNoteBtn.setText(Text.CREATE_NOTE_BTN)

	def emitSignal(self):
		self.createNoteBtn.clicked.connect(self.noteDialog_create_request.emit)
		self.settingBtn.clicked.connect(self.settingDialog_open_request.emit)

	# -----------------------------------------------------
	def createNoteDialog(self):
		log_view("Tạo note dialog theo yêu cầu của controller")
		viewCreateNoteDialog = ViewCreateNoteDialog()
		viewCreateNoteDialog.setWindowTitle(Text.DIALOG_TITLE_THEMNOTE)
		return viewCreateNoteDialog

	def exeNoteDialog(self, viewCreateNoteDialog):
		log_view("Thực thi note dialog theo yêu cầu của controller")
		result = viewCreateNoteDialog.exec()

		if result == QDialog.DialogCode.Accepted:
			self.familyNote_create_request.emit(viewCreateNoteDialog.dataOutput())
	# -----------------------------------------------------

	# Hàm dùng để gọi từ bên ngoài ------------------------
	def createViewReviewDialog(self, data):
		viewReviewDialog = ViewReviewDialog(data["noiDung"], data["cauHoi"], data["maNote"])

		return viewReviewDialog

	def createViewSettingDialog(self):
		return ViewSettingDialog()
	# -----------------------------------------------------

	# Phụ trách hiển thị review tag --------------------------------------- 
	def clearReviewTagLayout(self):
		for i in reversed(range(self.reviewTagLayout.count())):
			item = self.reviewTagLayout.itemAt(i)

			widget = item.widget()
			if widget is not None:
				widget.deleteLater()

		self.scrollArea.verticalScrollBar().setValue(0)

	def createReviewTag(self, reviewTag):
		viewReviewTag = ViewReviewTag(reviewTag["tenMon"], reviewTag["tenChuong"], reviewTag["maNote"], reviewTag["cauHoi"], reviewTag["noiDung"])

		idx = self.reviewTagLayout.count() - 1
		self.reviewTagLayout.insertWidget(idx, viewReviewTag)

		# print(f'Đã tạo chapter block có mã {chuong["maChuong"]}')
		return viewReviewTag
	# ------------------------------------------------------------------------