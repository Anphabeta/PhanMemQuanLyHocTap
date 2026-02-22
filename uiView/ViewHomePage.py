from PyQt6.QtWidgets import(
	QWidget,
	QVBoxLayout,
	QLabel
)


class ViewHomePage(QWidget):
	def __init__(self):
		super().__init__()

		self.title = QLabel("Trang chủ")

		self.setupLayout()


	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.title)
