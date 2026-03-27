from PyQt6.QtCore import QObject, pyqtSignal

import services.TacVuNote as TacVuNote


class ControllerNoteBlock(QObject):
	noteBlock_update_request = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.noteBlock = view

		self.noteBlock.note_edit_request.connect(self.handleEditNote)

		self.noteBlock.note_delete_request.connect(self.handleDeleteNote)

	# Phụ trách xử lý signal ---------------------------------------------
	def handleEditNote(self, maNote, newNoiDung):
		TacVuNote.suaNote(maNote,newNoiDung)
		note = TacVuNote.layNote(maNote)
		print("Đã sửa note")
		self.noteBlock.handleReceiveNote(note["noiDung"])

	def handleDeleteNote(self, maNote):
		TacVuNote.xoaNote(maNote)
		print("Đã xóa note")
		self.noteBlock_update_request.emit()
	# --------------------------------------------------------------------