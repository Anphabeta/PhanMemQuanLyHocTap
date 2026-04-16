from PyQt6.QtWidgets import(
	QWidget,
	QVBoxLayout,
	QHBoxLayout,
	QLabel,
	QPushButton,
	QScrollArea,
)
from PyQt6.QtCore import pyqtSignal
from lang.strings import Text
from lang.icons import Icon

class ViewHomePage(QWidget):
	def __init__(self):
		super().__init__()

		self.title = QLabel("Trang chủ")

		self.createNoteBtn = QPushButton(Text.CREATE_NOTE_BTN)

		self.scrollArea = QScrollArea()
		self.containerWidget = QWidget()
		self.scrollArea.setWidget(self.containerWidget)
		self.scrollArea.setWidgetResizable(True)

		self.setupLayout()


	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.title)
		layout.addWidget(self.createNoteBtn)
		layout.addWidget(self.scrollArea)
