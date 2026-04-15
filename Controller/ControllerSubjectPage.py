from PyQt6.QtCore import Qt, QObject, pyqtSignal
from Controller.ControllerChapterBlock import ControllerChapterBlock
import models.TacVuChuong as TacVuChuong
import models.TacVuMonHoc as TacVuMonHoc

class ControllerSubjectPage(QObject):
	# chapterBlock_update_request = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.subjectPage = view
		# ----------------------------------------------------------------------------------------------
		self.subjectPage.chapter_add_request.connect(self.handleAddChapter)
		# ----------------------------------------------------------------------------------------------

		self.controllerChapterBlockList = []
		self.viewChapterBlockList = []


	# Phụ trách khởi tạo nội dung như tên môn học ----------------------------------------------
	def getNavigateRequest(self,maMon):
		self.initContent(maMon)

	def initContent(self,maMon):
		self.setMaMon(maMon)
		self.getTenMon()

		self.updateChapterBlockList()

	def setMaMon(self,maMon):
		self.maMon = maMon
		self.subjectPage.setSubjId(maMon)

	def getTenMon(self):
		mon = TacVuMonHoc.layMon(self.maMon)
		self.subjectPage.setTitle(mon["tenMon"])
	# ------------------------------------------------------------------------------------------


	# Phụ trách hiển thị chapter block ---------------------------------------------------------
	def connectViewAndControllerChapterBlock(self, chapterBlock): # Hàm này làm 2 nhiệm vụ: Tạo controller và connect Signal
		controllerChapterBlock = ControllerChapterBlock(chapterBlock)
		self.controllerChapterBlockList.append(controllerChapterBlock)
		
		# Viết signal vào đây
		controllerChapterBlock.chapterBlock_update_request.connect(self.updateChapterBlockList)

		# Khởi tạo nội dung bên trong chapter block
		controllerChapterBlock.initContent()

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
	# ------------------------------------------------------------------------------------------
		
	
	# Phụ trách xử lý signal -------------------------------------------------------------------
	def handleAddChapter(self,maMon,tenChuong):
		maxOrder = TacVuChuong.layThuTuLonNhat(maMon)
		TacVuChuong.themChuong(tenChuong, maMon, maxOrder+100)
		self.updateChapterBlockList()
	# ------------------------------------------------------------------------------------------