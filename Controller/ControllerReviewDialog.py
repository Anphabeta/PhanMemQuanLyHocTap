from PyQt6.QtCore import QObject, pyqtSignal

import models.TacVuNote as TacVuNote
from debug.log_writer import log_controller, plainLog

class ControllerReviewDialog(QObject):
	reviewList_update_request = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.createNoteDialog = view

	# Phụ trách xử lý signal ---------------------------------------------
	def handleSendScore(self, maNote, diem):
		TacVuNote.capNhatThongSo(maNote, diem)
		
		self.reviewList_update_request.emit()
	# --------------------------------------------------------------------