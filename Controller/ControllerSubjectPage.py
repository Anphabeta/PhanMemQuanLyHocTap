from PyQt6.QtCore import Qt, QObject, pyqtSignal
from Controller.ControllerChapterBlock import ControllerChapterBlock
from services import TacVuChuong
from services import TacVuMonHoc

class ControllerSubjectPage(QObject):
	chapterBlock_update_request = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.subjectPage = view
		# ----------------------------------------------------------------------------------------------
		self.subjectPage.chapter_add_request.connect(self.handleAddChapter)
		# ----------------------------------------------------------------------------------------------

		self.controllerChapterBlockList = []
		self.viewChapterBlockList = []

	def initContent(self,maMon):
		self.setMaMon(maMon)
		self.getTenMon()

		self.updateChapterBlockList()

	def getNavigateRequest(self,maMon):
		self.initContent(maMon)

	def connectViewAndControllerChapterBlock(self, chapterBlock):
		controllerChapterBlock = ControllerChapterBlock(chapterBlock)
		self.controllerChapterBlockList.append(controllerChapterBlock)
		
		controllerChapterBlock.chapterBlock_update_request.connect(self.updateChapterBlockList)
		

	def createViewAndControllerChapterBlock(self):
		chapterList = TacVuChuong.layDanhSachChuong(self.maMon)

		for chapter in chapterList:
			# print(chapter)
			chapterBlock = self.subjectPage.createChapterBlock(chapter)
			self.viewChapterBlockList.append(chapterBlock)
			self.connectViewAndControllerChapterBlock(chapterBlock)

	def deleteViewAndControllerChapterBlock(self):
		self.subjectPage.clearChapterLayout()
		self.controllerChapterBlockList.clear()
		self.viewChapterBlockList.clear()

	def updateChapterBlockList(self):
		self.deleteViewAndControllerChapterBlock()
		self.createViewAndControllerChapterBlock()

		
	def setMaMon(self,maMon):
		self.maMon = maMon
		self.subjectPage.setSubjId(maMon)

	def getTenMon(self):
		mon = TacVuMonHoc.layMon(self.maMon)
		self.subjectPage.setTitle(mon["tenMon"])

	def handleAddChapter(self,maMon,tenChuong):
		TacVuChuong.themChuong(tenChuong, maMon)
		self.updateChapterBlockList()