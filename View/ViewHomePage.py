from PyQt6.QtWidgets import(
	QWidget,
	QVBoxLayout,
	QHBoxLayout,
	QLabel,
	QPushButton,
	QScrollArea,
	QDialog,
)
from PyQt6.QtCore import pyqtSignal
from lang.strings import Text
from lang.icons import Icon
from debug.log_writer import log_view, plainLog

from View.ViewCreateNoteDialog import ViewCreateNoteDialog
from View.ViewReviewDialog import ViewReviewTag, ViewReviewDialog

class ViewHomePage(QWidget):
	noteDialog_create_request = pyqtSignal()
	familyNote_create_request = pyqtSignal(object)

	def __init__(self):
		super().__init__()

		self.title = QLabel("Trang chủ")

		self.createNoteBtn = QPushButton(Text.CREATE_NOTE_BTN)

		self.scrollArea = QScrollArea()
		self.containerWidget = QWidget()
		self.scrollArea.setWidget(self.containerWidget)
		self.scrollArea.setWidgetResizable(True)

		self.reviewTagLayout = QVBoxLayout(self.containerWidget)

		self.setupLayout()
		self.emitSignal()


	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.title)
		layout.addWidget(self.createNoteBtn)
		layout.addWidget(self.scrollArea)

		self.reviewTagLayout.addStretch()

	def emitSignal(self):
		self.createNoteBtn.clicked.connect(self.noteDialog_create_request.emit)



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