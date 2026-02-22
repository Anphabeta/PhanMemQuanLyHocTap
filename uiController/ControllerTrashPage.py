from PyQt6.QtWidgets import(
	QDialog,
	QMenu,
	QListWidgetItem
)
from PyQt6.QtCore import Qt, QObject, pyqtSignal
from lang.strings import Text
from services import TacVuMonHoc

class ControllerTrashPage(QObject):
	recoverSubj = pyqtSignal()

	def __init__(self, view):
		super().__init__()

		self.trashPage = view

		# ----------------------------------------------------------------------------------------------
		self.trashPage.recoverBtn.clicked.connect(self.handleRecover)
		# ----------------------------------------------------------------------------------------------
		self.trashPage.deleteBtn.clicked.connect(self.handleDelete)
		# ----------------------------------------------------------------------------------------------
		self.trashPage.deleteAllBtn.clicked.connect(self.handleDeleteAll)
		# ----------------------------------------------------------------------------------------------
		self.trashPage.trashSubjList.itemSelectionChanged.connect(self.isSelectedStateBtn)
		# ----------------------------------------------------------------------------------------------

		self.updateTrashSubjList()

	def isSelectedStateBtn(self):
		state = self.trashPage.trashSubjList.currentItem() is not None
		self.trashPage.recoverBtn.setEnabled(state)
		self.trashPage.deleteBtn.setEnabled(state)

		self.trashPage.deleteAllBtn.setEnabled(self.trashPage.trashSubjList.count()>0)

	def handleRecover(self):
		maMon = self.trashPage.getId_item_selected()
		if maMon:
			TacVuMonHoc.khoiPhucMon(maMon)
			print("Đã khôi phục môn")
			self.updateTrashSubjList()
			self.recoverSubj.emit()

	def handleDelete(self):
		maMon = self.trashPage.getId_item_selected()
		if maMon:
			TacVuMonHoc.xoaMon(maMon)
			print("Đã xóa môn vĩnh viễn")
			self.updateTrashSubjList()

	def handleDeleteAll(self):
		TacVuMonHoc.xoaTatCaMon()
		print("Đã xóa tất cả môn")
		self.updateTrashSubjList()

	def updateTrashSubjList(self):
		trashSubjList = []
		for subj in TacVuMonHoc.layDanhSachMonTrash():
			item = QListWidgetItem(subj['tenMon'])
			item.setData(Qt.ItemDataRole.UserRole, subj["maMon"])
			trashSubjList.append(item)
		self.trashPage.showTrashSubjList(trashSubjList)