from PyQt6.QtWidgets import(
	QDialog,
	QWidget,
	QPushButton,
	QLineEdit,
	QVBoxLayout,
	QHBoxLayout
)
from lang.strings import Text

class InputDialog(QDialog):
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