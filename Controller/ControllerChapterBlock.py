from PyQt6.QtCore import QObject, pyqtSignal

import services.TacVuChuong as TacVuChuong
import services.TacVuNote as TacVuNote
from Controller.ControllerNoteBlock import ControllerNoteBlock

class ControllerChapterBlock(QObject):
	chapterBlock_update_request = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.chapterBlock = view

		self.chapterBlock.chapter_edit_request.connect(self.handleEditChapter)

		self.chapterBlock.chapter_delete_request.connect(self.handleDeleteChapter)

		self.viewNoteBlockList = []
		self.controllerNoteBlockList = []

	# Phụ trách xử lý signal ----------------------------------------------
	def handleEditChapter(self, maChuong, newName):
		TacVuChuong.suaTenChuong(maChuong,newName)
		chuong = TacVuChuong.layChuong(maChuong)
		print("Đã sửa tên chương")
		self.chapterBlock.handleReceiveChapterName(chuong["tenChuong"])

	def handleDeleteChapter(self, maChuong):
		TacVuChuong.xoaChuong(maChuong)
		print("Đã xóa chương")
		self.chapterBlock_update_request.emit()
	# ----------------------------------------------------------------------


	# Phụ trách hiển thị nội dung bên trong Chapter ------------------------
	def initContent(self):
		self.updateNoteBlockList()
	# ----------------------------------------------------------------------


	# Phụ trách hiển thị Note Block ----------------------------------------
	def connectViewAndControllerNoteBlock(self, viewNoteBlock):
		controllerNoteBlock = ControllerNoteBlock(viewNoteBlock)
		self.controllerNoteBlockList.append(controllerNoteBlock)

		# Viết signal vào đây
		controllerNoteBlock.noteBlock_update_request.connect(self.updateNoteBlockList)

	def createViewAndControllerNoteBlock(self):
		dsNote = TacVuNote.layDanhSachNote(self.chapterBlock.chapterId)

		for note in dsNote:
			viewNoteBlock = self.chapterBlock.createNoteBlock(note)
			self.viewNoteBlockList.append(viewNoteBlock)
			self.connectViewAndControllerNoteBlock(viewNoteBlock)

	def deleteViewAndControllerNoteBlock(self):
		self.chapterBlock.clearNoteLayout()
		self.viewNoteBlockList.clear()
		self.controllerNoteBlockList.clear()

	def updateNoteBlockList(self):
		self.deleteViewAndControllerNoteBlock()
		self.createViewAndControllerNoteBlock()
	# ----------------------------------------------------------------------
