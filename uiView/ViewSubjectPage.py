from PyQt6.QtWidgets import(
	QWidget,
	QVBoxLayout,
	QLabel
)


class ViewSubjectPage(QWidget):
	def __init__(self):
		super().__init__()

		self.title = QLabel("Môn học")

		self.setupLayout()


	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.title)