import sys
from PyQt6.QtWidgets import (
    QApplication, # Tạo event loop
    QMainWindow,
    QWidget, # Tạo widget nói chung
    QHBoxLayout, # Tạo layout ngang
    QVBoxLayout, # Tạo layout dọc
    QPushButton, # Tạo nút bấm
    QLabel, # Tạo văn bản
    QListWidget, # Tạo danh sách widget
    QDialog,
    QLineEdit,
    QMenu,
    QStackedWidget,
    QScrollArea,
    QLineEdit,
    QTextEdit,
    QPlainTextEdit,
    QCheckBox,
    QComboBox,
)
from PyQt6.QtCore import Qt, QPoint, QObject, pyqtSignal
from PyQt6.QtGui import QCursor

class TextBlock(QWidget):
    def __init__(self, initial_text=""):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.text_edit = QPlainTextEdit()
        self.text_edit.setPlainText(initial_text)
        self.layout.addWidget(self.text_edit)

    def getText(self):
        return self.text_edit.toPlainText()

    def setText(self, text):
        self.text_edit.setPlainText(text)

def handleClicked(text):
    print(text)
    textShow.setText(text)
    textEdit.hide()
    textShow.show()

def toggle(textEdit, textShow):
    textEdit.show()
    textShow.hide()

def checkStatus(status):
    print(status)

app = QApplication(sys.argv)
window = QWidget()
window.resize(950,600)

layout = QVBoxLayout(window)

textEdit = TextBlock()
textEdit.setText("Hello")
textEdit.hide()

textShow = QLabel(textEdit.getText())

submitBtn = QPushButton("Submit")
submitBtn.clicked.connect(lambda: handleClicked(textEdit.getText()))

editBtn = QPushButton("Edit")
editBtn.clicked.connect(lambda: toggle(textEdit,textShow))

checkBox = QCheckBox("Đã làm")
checkBox.stateChanged.connect(checkStatus)

comboBox = QComboBox()
comboBox.addItems(["--Chọn môn học--", "Toán", "Lý", "Hóa", "--Thêm môn học mới--"])

layout.addWidget(textEdit)
layout.addWidget(textShow)
layout.addWidget(submitBtn)
layout.addWidget(editBtn)
layout.addWidget(checkBox)
layout.addWidget(comboBox)
layout.addStretch()

window.show()

app.exec()




