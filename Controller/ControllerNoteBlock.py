from PyQt6.QtCore import QObject, pyqtSignal

import models.TacVuNote as TacVuNote

from debug.log_writer import log_controller, plainLog


class ControllerNoteBlock(QObject):
	noteBlock_update_request = pyqtSignal()
	noteBlock_moveUp_request = pyqtSignal(int)
	noteBlock_moveDown_request = pyqtSignal(int)
	recentAccess_update_request = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.noteBlock = view

		self.noteBlock.note_edit_request.connect(self.handleEditNote)

		self.noteBlock.note_delete_request.connect(self.handleDeleteNote)

		self.noteBlock.note_moveUp_request.connect(self.handleMoveUpNote)

		self.noteBlock.note_moveDown_request.connect(self.handleMoveDownNote)

		self.noteBlock.note_change_recallState.connect(self.handleChangeRecallState)

	# Phụ trách xử lý signal ---------------------------------------------
	def handleEditNote(self, maNote, newNoiDung):
		log_controller("Kết nối model để sửa")
		TacVuNote.suaNote(maNote,newNoiDung)
		note = TacVuNote.layNote(maNote)
		self.noteBlock.handleReceiveNote(note["noiDung"])

	def handleDeleteNote(self, maNote):
		log_controller("Kết nối model để xóa note")
		TacVuNote.xoaNote(maNote)
		self.noteBlock_update_request.emit()

	def handleMoveUpNote(self, maNote):
		log_controller("Truyền tín hiệu di chuyển lên cho Chapter Block")
		self.noteBlock_moveUp_request.emit(maNote)

	def handleMoveDownNote(self, maNote):
		log_controller("Truyền tín hiệu di chuyển xuống cho Chapter Block")
		self.noteBlock_moveDown_request.emit(maNote)

	def handleChangeRecallState(self, maNote, state):
		if state == 0:
			TacVuNote.tatThongBao(maNote)
		else:
			TacVuNote.batThongBao(maNote)
	# --------------------------------------------------------------------