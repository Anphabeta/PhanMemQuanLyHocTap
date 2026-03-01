from PyQt6.QtCore import Qt, QObject, pyqtSignal
from services import TacVuChuong
from services import TacVuMonHoc

class ControllerSubjectPage(QObject):
	def __init__(self, view):
		super().__init__()

		self.subjectPage = view

	def initContent(self,maMon):
		self.setMaMon(maMon)
		self.getTenMon()

		self.updateChapterBlockList()

	def getNavigateRequest(self,maMon):
		self.initContent(maMon)
		
	def setMaMon(self,maMon):
		self.maMon = maMon
		self.subjectPage.setSubjId(maMon)

	def getTenMon(self):
		mon = TacVuMonHoc.layMon(self.maMon)
		self.subjectPage.setTitle(mon["tenMon"])

	def updateChapterBlockList(self):
		chapterList = TacVuChuong.layDanhSachChuong(self.maMon)
		self.subjectPage.showChapterBlockList(chapterList)