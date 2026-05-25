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
    QSplitter,
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

left = QLabel("LEFT")
right = QLabel("RIGHT")

splitter = QSplitter()
splitter.addWidget(left)
splitter.addWidget(right)

splitter.setSizes([240, 500])
layout.addWidget(splitter)

window.show()

app.exec()




