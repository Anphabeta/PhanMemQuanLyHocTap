from PyQt6.QtCore import QObject, pyqtSignal
from Controller.ControllerSidebar import ControllerSidebar
from Controller.ControllerTrashPage import ControllerTrashPage
from Controller.ControllerSubjectPage import ControllerSubjectPage
from Controller.ControllerHomePage import ControllerHomePage


class ControllerMainWindow(QObject):

	def __init__(self, view):
		super().__init__()

		self.mainWindow = view

		# Khởi tạo và kết nối các controller với view tương ứng
		self.controllerSidebar = ControllerSidebar(view.sidebar)
		self.controllerTrashPage = ControllerTrashPage(view.trashPage)
		self.controllerSubjectPage = ControllerSubjectPage(view.subjPage)
		self.controllerHomePage = ControllerHomePage(view.homePage)

		# Kết nối tín hiệu giữa các thành phần
		self.connectSignalFromControllerSidebar()
		self.connectSignalFromControllerTrashPage()
		self.connectSignalFromControllerSubjectPage()
		self.connectSignalFromControllerHomePage()

	def connectSignalFromControllerSidebar(self):
		self.controllerSidebar.homePage_request.connect(self.mainWindow.showHomePage)
		self.controllerSidebar.trashPage_request.connect(self.mainWindow.showTrashPage)
		self.controllerSidebar.trashSubjList_update_request.connect(self.controllerTrashPage.updateTrashSubjList)
		self.controllerSidebar.subjItem_navigate_request.connect(self.handleNavigateSubjPage)

	def connectSignalFromControllerSubjectPage(self):
		self.controllerSubjectPage.recentAccess_update_request.connect(self.controllerSidebar.updateRecentAccess)

	def connectSignalFromControllerHomePage(self):
		self.controllerHomePage.subjList_update_request.connect(self.controllerSidebar.updateSubjList)

	def connectSignalFromControllerTrashPage(self):
		self.controllerTrashPage.subjList_update_request.connect(self.controllerSidebar.updateSubjList)

	def handleNavigateSubjPage(self, maMon):
		self.mainWindow.showSubjPage()
		self.controllerSubjectPage.getNavigateRequest(maMon)

