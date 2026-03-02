from PyQt6.QtWidgets import(
	QMainWindow,
	QWidget,
	QVBoxLayout,
	QHBoxLayout,
	QStackedWidget
)
from View.ViewSidebar import ViewSidebar
from View.ViewTrashPage import ViewTrashPage
from View.ViewHomePage import ViewHomePage
from View.ViewSubjectPage import ViewSubjectPage
from Controller.ControllerSidebar import ControllerSidebar
from lang.strings import Text

class ViewMainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.sidebar = ViewSidebar()
		self.trashPage = ViewTrashPage()
		self.subjPage = ViewSubjectPage()
		self.homePage = ViewHomePage()
		self.stackedWidget = QStackedWidget()
		self.stackedWidget.addWidget(self.homePage)
		self.stackedWidget.addWidget(self.trashPage)
		self.stackedWidget.addWidget(self.subjPage)
		#
		self.setupUI()

	def setupUI(self):
		self.resize(950,900)
		self.setWindowTitle(Text.WINDOW_TITLE)
		central = QWidget()
		self.setCentralWidget(central)
		#
		layout = QHBoxLayout(central)
		layout.addWidget(self.sidebar)
		layout.addWidget(self.stackedWidget)

	def showHomePage(self):
		self.stackedWidget.setCurrentWidget(self.homePage)

	def showSubjPage(self):
		self.stackedWidget.setCurrentWidget(self.subjPage)

	def showTrashPage(self):
		self.stackedWidget.setCurrentWidget(self.trashPage)

	