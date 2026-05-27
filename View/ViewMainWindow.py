from PyQt6.QtWidgets import(
	QMainWindow,
	QWidget,
	QVBoxLayout,
	QHBoxLayout,
	QStackedWidget,
	QSplitter,
)
from PyQt6.QtCore import Qt
from View.ViewSidebar import ViewSidebar
from View.ViewTrashPage import ViewTrashPage
from View.ViewHomePage import ViewHomePage
from View.ViewSubjectPage import ViewSubjectPage
from Controller.ControllerSidebar import ControllerSidebar
from lang.strings import Text, set_language

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
		self.updateUIText()
		self.setupUI()

	def setupUI(self):
		self.resize(950,900)
		central = QWidget()
		self.setCentralWidget(central)
		#
		splitter = QSplitter()
		splitter.addWidget(self.sidebar)
		splitter.addWidget(self.stackedWidget)
		splitter.setSizes([250,700])
		splitter.setHandleWidth(8)

		layout = QHBoxLayout(central)
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(0)
		layout.addWidget(splitter)

	def showHomePage(self):
		self.stackedWidget.setCurrentWidget(self.homePage)

	def showSubjPage(self):
		self.stackedWidget.setCurrentWidget(self.subjPage)

	def showTrashPage(self):
		self.stackedWidget.setCurrentWidget(self.trashPage)

	def setLanguage(self, lang):
		set_language(lang)

	def updateUIText(self):
		self.setWindowTitle(Text.WINDOW_TITLE)

		self.sidebar.updateUIText()
		self.trashPage.updateUIText()
		self.subjPage.updateUIText()
		self.homePage.updateUIText()


	