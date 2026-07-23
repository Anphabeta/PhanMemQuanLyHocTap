from PyQt6.QtCore import Qt, QObject, pyqtSignal
from lang.strings import Text
import models.TacVuMonHoc as TacVuMonHoc
from View.QDefine import InputDialog

from debug.log_writer import log_controller

class ControllerSidebar(QObject):
	homePage_request = pyqtSignal()
	trashPage_request = pyqtSignal()

	trashSubjList_update_request = pyqtSignal()
	reviewTag_update_request = pyqtSignal()

	subjItem_navigate_request = pyqtSignal(int)

	def __init__(self, sidebar):
		super().__init__()
		
		self.sidebar = sidebar
		# ----------------------------------------------------------------------------------------------
		self.sidebar.homePage_request.connect(lambda: self.homePage_request.emit())
		# ----------------------------------------------------------------------------------------------
		self.sidebar.trashPage_request.connect(lambda: self.trashPage_request.emit())
		# ----------------------------------------------------------------------------------------------
		self.sidebar.subj_add_request.connect(self.handleAddSubj)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.subj_edit_request.connect(self.handleEditSubj)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.subj_softDelete_request.connect(self.handleMoveSubjToTrash)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.subjItem_selected.connect(self.handleSwitchSubject)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.subj_addFavorite_request.connect(self.handleAddFavoriteSubject)
		# ----------------------------------------------------------------------------------------------
		self.sidebar.subj_removeFavorite_request.connect(self.handleRemoveFavoriteSubject)
		# ----------------------------------------------------------------------------------------------
		self.updateSubjList()

	def handleSwitchSubject(self, maMon):
		log_controller("Chuyển tiếp tín hiệu cho MainWindow", f"id = {maMon}")
		self.subjItem_navigate_request.emit(maMon)

	def handleAddSubj(self, tenMon):
		log_controller("Thêm môn vào db")
		TacVuMonHoc.themMon(tenMon)

		self.updateSubjList()

		# self.newSubj_switch_request.emit()

	def handleMoveSubjToTrash(self,maMon):
		# Nếu môn học đang trỏ tới bị xóa, tự động chuyển về home page
		# Phát tín hiệu đến MainWindow (homePage request)
		currentMaMon = self.sidebar.getCurrentMaMon()
		if currentMaMon and currentMaMon == maMon:
			log_controller("Vì đang đc trỏ, phát tín hiệu chuyển về homepage")
			self.homePage_request.emit()

		# Di chuyển môn trong db
		log_controller("Xóa mềm môn trong db")
		TacVuMonHoc.moveMonToTrash(maMon)
		self.updateSubjList()

		# Phát tín hiệu cho trashPage cập nhật lại danh sách (trashSubjlist update request)
		self.trashSubjList_update_request.emit()

		# Phát tín hiệu cho homePage cập nhật lại danh sách ôn tập
		self.reviewTag_update_request.emit()

	def handleEditSubj(self,maMon,newName):
		log_controller("Sửa tên môn học trong db")
		TacVuMonHoc.suaTenMon(maMon,newName)
		
		self.updateSubjList()

	def handleAddFavoriteSubject(self, maMon):
		log_controller("Thêm môn học vào mục ưa thích")
		TacVuMonHoc.themUaThich(maMon)

		self.updateSubjList()

	def handleRemoveFavoriteSubject(self, maMon):
		log_controller("Thêm môn học vào mục ưa thích")
		TacVuMonHoc.boUaThich(maMon)

		self.updateSubjList()

	def updateSubjList(self):
		log_controller("Lấy ds môn từ db và hiển thị")
		subjList = TacVuMonHoc.layDanhSachMon()
		self.sidebar.showSubjList(subjList)

		subjListFav = TacVuMonHoc.layDanhSachMonUaThich()
		self.sidebar.showSubjListFav(subjListFav)

	def updateRecentAccess(self, maMon):
		log_controller("Cập nhật truy cập gần nhất cho môn")
		TacVuMonHoc.capNhatTruyCapGanNhat(maMon)

		self.updateSubjList()
