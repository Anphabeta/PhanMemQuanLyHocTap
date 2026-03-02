from PyQt6.QtCore import QObject, pyqtSignal
import services.TacVuChuong as TacVuChuong

class ControllerChapterBlock(QObject):
	chapterBlock_update_request = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.chapterBlock = view

		self.chapterBlock.chapter_edit_request.connect(self.handleEditChapter)

		self.chapterBlock.chapter_delete_request.connect(self.handleDeleteChapter)

	def handleEditChapter(self, maChuong, newName):
		TacVuChuong.suaTenChuong(maChuong,newName)
		chuong = TacVuChuong.layChuong(maChuong)
		print("Đã sửa tên chương")
		self.chapterBlock.handleReceiveChapterName(chuong["tenChuong"])

	def handleDeleteChapter(self, maChuong):
		TacVuChuong.xoaChuong(maChuong)
		print("Đã xóa chương")
		self.chapterBlock_update_request.emit()