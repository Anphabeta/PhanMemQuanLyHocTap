from PyQt6.QtCore import QObject, pyqtSignal
from uiController.ControllerSidebar import ControllerSidebar
from uiController.ControllerTrashPage import ControllerTrashPage



class ControllerMainWindow:


	def __init__(self, view):

		self.mainWindow = view

		# Khởi tạo controller sidebar và kết nối các signal Sidebar -> Main Window
		self.controllerSidebar = ControllerSidebar(view.sidebar)
		self.controllerSidebar.pushBtn.connect(self.switchPage)
		self.controllerSidebar.subjClicked.connect(self.switchSubj)
		self.controllerSidebar.changePageAfterDelete.connect(self.setPageAfterDelete)

		# Khởi tạo controller sidebar và kết nối các signal Trash Page -> Main Window
		self.controllerTrashPage = ControllerTrashPage(view.trashPage)

		# Kết nối signal của các Widget khác không liên quan Main Window
		self.controllerSidebar.moveToTrash.connect(self.controllerTrashPage.updateTrashSubjList)
		self.controllerTrashPage.recoverSubj.connect(self.controllerSidebar.updateSubjList)

	def switchPage(self, page):
		if page == "HomePage":
			self.mainWindow.stackedWidget.setCurrentWidget(self.mainWindow.homePage)
		elif page == "TrashPage":
			self.controllerTrashPage.trashPage.setDefaultStateBtn()
			self.mainWindow.stackedWidget.setCurrentWidget(self.mainWindow.trashPage)

	def switchSubj(self, maMon):
		self.mainWindow.stackedWidget.setCurrentWidget(self.mainWindow.subjPage)

	def setPageAfterDelete(self):
		if self.mainWindow.stackedWidget.currentWidget() == self.mainWindow.subjPage:
			self.switchPage("HomePage")