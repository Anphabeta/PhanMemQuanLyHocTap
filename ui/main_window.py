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
	QLineEdit
)
from services.TacVuMonHoc import(
	layDanhSachMon,
	themMon,
	capNhatTruyCapGanNhat,
	suaTenMon
) 
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
		self.subjListWidget.addItems(subjList)

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
        self.setWindowTitle(Text.DIALOG_TITLE)
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

	def setupUI(self):
		central = QWidget()
		self.setCentralWidget(central)
		#
		subjList = [x["tenMon"] for x in layDanhSachMon()]
		self.sidebar.updateSubjList(subjList)
		#
		layout = QHBoxLayout(central)
		layout.addWidget(self.sidebar)
		layout.addWidget(self.mainarea)

	def handleAddSubj(self):
		dialog = NewSubjDialog()
		result = dialog.exec()

		if result == QDialog.DialogCode.Accepted:
			themMon(dialog.textOutput())
		subjList = [x["tenMon"] for x in layDanhSachMon()]
		self.sidebar.updateSubjList(subjList)