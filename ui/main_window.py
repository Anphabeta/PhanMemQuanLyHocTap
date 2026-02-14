import sys
from PyQt6.QtWidgets import(
	QApplication,
	QMainWindow,
	QWidget,
	QPushButton,
	QListWidget,
	QVBoxLayout,
	QHBoxLayout,
	QDialog,
	QLineEdit,
	QListWidgetItem,
	QMenu
)
from PyQt6.QtCore import Qt
import services.TacVuMonHoc as TacVuMonHoc
from lang.strings import Text

class Sidebar(QWidget):
	# Class này chỉ dùng để hiển thị UI, không được gọi hàm từ file khác
	def __init__(self):
		# Trong hàm này cần: Khởi tạo, xử lý layout, connect các widget con
		super().__init__()
		#
		self.homeBtn = QPushButton(Text.HOME)
		self.newSubjBtn = QPushButton(Text.NEWSUBJ)
		self.trashBtn = QPushButton(Text.TRASH)
		self.subjListWidget = QListWidget()
		#
		self.setFixedWidth(250)
		self.setupLayout()

	def setupLayout(self):
		layout = QVBoxLayout(self)
		layout.addWidget(self.homeBtn)
		layout.addWidget(self.newSubjBtn)
		layout.addWidget(self.trashBtn)
		layout.addWidget(self.subjListWidget)

	def updateSubjList(self, subjList):
		self.subjListWidget.clear()
		for subj in subjList:
			self.subjListWidget.addItem(subj)

class NewSubjDialog(QDialog):
    def __init__(self):
        super().__init__()
        #
        self.inputText = QLineEdit()
        self.btnWidgets = QWidget()
        self.okBtn = QPushButton(Text.OK)
        self.cancelBtn = QPushButton(Text.CANCEL)
        #
        self.setFixedSize(400,200)
        self.setupLayout()
        self.setupConnectBtn()

    def setupLayout(self):
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.inputText)
        mainLayout.addWidget(self.btnWidgets)
        mainLayout.addStretch()
        #
        btnLayout = QHBoxLayout(self.btnWidgets)
        btnLayout.addWidget(self.okBtn)
        btnLayout.addWidget(self.cancelBtn)

    def setupConnectBtn(self):
        self.okBtn.clicked.connect(self.accept)
        self.cancelBtn.clicked.connect(self.reject)

    def textOutput(self):
        return self.inputText.text()

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		# Xử lý sidebar ---------------------------
		self.sidebar = Sidebar()
		self.sidebar.newSubjBtn.clicked.connect(self.handleAddSubj)
		# -----------------------------------------
		# Xử lý main area -------------------------
		self.mainarea = QWidget()
		#
		self.resize(950,600)
		self.setWindowTitle(Text.WINDOW_TITLE)
		self.setupUI()
		#
		# Xử lý Context Menu -------------------------------------
		self.sidebar.subjListWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
		self.sidebar.subjListWidget.customContextMenuRequested.connect(self.showContextMenu)
		# --------------------------------------------------------

	def updateSubjListForSidebar(self):
		subjList = []
		for subj in TacVuMonHoc.layDanhSachMon():
			item = QListWidgetItem(subj["tenMon"])
			item.setData(Qt.ItemDataRole.UserRole, subj["maMon"])
			subjList.append(item)
		self.sidebar.updateSubjList(subjList)

	def setupUI(self):
		central = QWidget()
		self.setCentralWidget(central)
		#
		self.updateSubjListForSidebar()
		#
		layout = QHBoxLayout(central)
		layout.addWidget(self.sidebar)
		layout.addWidget(self.mainarea)

	def handleAddSubj(self):
		dialog = NewSubjDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_THEMMON)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			TacVuMonHoc.themMon(dialog.textOutput())

		self.updateSubjListForSidebar()

	def handleMoveSubj(self,maMon):
		TacVuMonHoc.moveMonToTrash(maMon)
		
		self.updateSubjListForSidebar()
		print("Đã chuyển qua thùng rác")

	def handleSuaSubj(self,maMon):
		dialog = NewSubjDialog()
		dialog.setWindowTitle(Text.DIALOG_TITLE_SUAMON)
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			TacVuMonHoc.suaTenMon(maMon,dialog.textOutput())
		
		self.updateSubjListForSidebar()
		print("Đã sửa")

	def showContextMenu(self,pos):
		item = self.sidebar.subjListWidget.itemAt(pos)

		if item is None:
			return

		maMon = item.data(Qt.ItemDataRole.UserRole)
		contextMenu = QMenu()

		action_sua = contextMenu.addAction(Text.A_SUA)
		action_move = contextMenu.addAction(Text.A_MOVE)
		action_thich = contextMenu.addAction(Text.A_THICH)

		action_sua.triggered.connect(lambda _, ma=maMon: self.handleSuaSubj(ma))
		action_move.triggered.connect(lambda: self.handleMoveSubj(maMon))

		contextMenu.exec(self.sidebar.subjListWidget.mapToGlobal(pos))
		

