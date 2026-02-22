from PyQt6.QtWidgets import (
	QWidget,
	QPushButton,
	QListWidget,
	QVBoxLayout
)
from lang.strings import Text

class ViewSidebar(QWidget):
	# Class này chỉ dùng để hiển thị UI, không được gọi hàm từ file khác
	def __init__(self):
		# Trong hàm này cần: Khởi tạo, xử lý layout, connect các widget con
		super().__init__()
		#
		self.homeBtn = QPushButton(Text.HOME)
		self.newSubjBtn = QPushButton(Text.NEWSUBJ)
		self.trashBtn = QPushButton(Text.TRASH)
		self.subjListWidget = QListWidget()
		#
		self.setFixedWidth(250)
		self.setupLayout()

	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.homeBtn)
		layout.addWidget(self.newSubjBtn)
		layout.addWidget(self.trashBtn)
		layout.addWidget(self.subjListWidget)

	def showSubjList(self, subjList):
		self.subjListWidget.clear()
		for subj in subjList:
			self.subjListWidget.addItem(subj)