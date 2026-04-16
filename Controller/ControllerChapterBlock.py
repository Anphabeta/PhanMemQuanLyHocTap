from PyQt6.QtCore import QObject, pyqtSignal

import models.TacVuChuong as TacVuChuong
import models.TacVuNote as TacVuNote
from Controller.ControllerNoteBlock import ControllerNoteBlock

from debug.log_writer import log_controller, plainLog

class ControllerChapterBlock(QObject):
	chapterBlock_update_request = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.chapterBlock = view

		self.chapterBlock.chapter_edit_request.connect(self.handleEditChapter)

		self.chapterBlock.chapter_delete_request.connect(self.handleDeleteChapter)

		self.chapterBlock.note_add_request.connect(self.handleAddNote)

		self.viewNoteBlockList = []
		self.controllerNoteBlockList = []

		self.chapterId = view.chapterId

	# Phụ trách xử lý signal ----------------------------------------------
	def handleEditChapter(self, maChuong, newName):
		log_controller("Sửa tên chương trong db và lấy tên chương mới từ db")
		TacVuChuong.suaTenChuong(maChuong,newName)
		chuong = TacVuChuong.layChuong(maChuong)
		self.chapterBlock.handleReceiveChapterName(chuong["tenChuong"])

	def handleDeleteChapter(self, maChuong):
		log_controller("Xóa chương trong db")
		TacVuChuong.xoaChuong(maChuong)
		self.chapterBlock_update_request.emit()

	def handleAddNote(self, maChuong, newText, isChecked):
		log_controller("Lấy thứ tự lớn nhất")
		maxOrder = TacVuNote.layThuTuLonNhat(maChuong)

		mapping = {
			True : "enable",
			False : "disable"
		}

		log_controller("Tạo note trong db")
		TacVuNote.themNote(maChuong,newText,maxOrder+100,mapping[isChecked])

		self.updateNoteBlockList()

	def handleMoveUpNote(self, maNote):
		TacVuNote.diChuyenNoteLen(maNote, self.chapterId)

		self.updateNoteBlockList()

	def handleMoveDownNote(self, maNote):
		TacVuNote.diChuyenNoteXuong(maNote, self.chapterId)

		self.updateNoteBlockList()
	# ----------------------------------------------------------------------


	# Phụ trách hiển thị nội dung bên trong Chapter ------------------------
	def initContent(self):
		self.updateNoteBlockList()
	# ----------------------------------------------------------------------


	# Phụ trách hiển thị Note Block ----------------------------------------
	def connectViewAndControllerNoteBlock(self, viewNoteBlock): # Hàm này làm 2 nhiệm vụ: Tạo controller và connect Signal
		controllerNoteBlock = ControllerNoteBlock(viewNoteBlock)
		self.controllerNoteBlockList.append(controllerNoteBlock)

		# Viết signal vào đây
		controllerNoteBlock.noteBlock_update_request.connect(self.updateNoteBlockList)
		controllerNoteBlock.noteBlock_moveUp_request.connect(self.handleMoveUpNote)
		controllerNoteBlock.noteBlock_moveDown_request.connect(self.handleMoveDownNote)

	def createViewAndControllerNoteBlock(self):
		dsNote = TacVuNote.layDanhSachNote(self.chapterBlock.chapterId)

		log_controller("Tạo ds note")
		for note in dsNote:
			viewNoteBlock = self.chapterBlock.createNoteBlock(note)
			self.viewNoteBlockList.append(viewNoteBlock)
			self.connectViewAndControllerNoteBlock(viewNoteBlock)

	def deleteViewAndControllerNoteBlock(self):
		log_controller("Xóa ds note cũ")
		self.chapterBlock.clearNoteLayout()
		self.viewNoteBlockList.clear()
		self.controllerNoteBlockList.clear()

	def updateNoteBlockList(self):
		log_controller("Cập nhật lại ds note")
		self.deleteViewAndControllerNoteBlock()
		self.createViewAndControllerNoteBlock()
	# ----------------------------------------------------------------------
