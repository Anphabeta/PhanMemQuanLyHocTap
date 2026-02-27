from PyQt6.QtWidgets import(
	QMainWindow,
	QWidget,
	QVBoxLayout,
	QHBoxLayout,
	QStackedWidget
)
from uiView.ViewSidebar import ViewSidebar
from uiView.ViewTrashPage import ViewTrashPage
from uiView.ViewHomePage import ViewHomePage
from uiView.ViewSubjectPage import ViewSubjectPage
from uiController.ControllerSidebar import ControllerSidebar
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
		self.resize(950,600)
		self.setWindowTitle(Text.WINDOW_TITLE)
		central = QWidget()
		self.setCentralWidget(central)
		#
		layout = QHBoxLayout(central)
		layout.addWidget(self.sidebar)
		layout.addWidget(self.stackedWidget)

	def showHomePage(self):
		self.stackedWidget.setCurrentWidget(self.homePage)

	def showSubjPage(self, maMon):
		self.stackedWidget.setCurrentWidget(self.subjPage)

	def showTrashPage(self):
		self.stackedWidget.setCurrentWidget(self.trashPage)

	