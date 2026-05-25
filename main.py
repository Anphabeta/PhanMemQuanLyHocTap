from PyQt6.QtWidgets import QApplication
from View import ViewMainWindow
from Controller import ControllerMainWindow
import sys


app = QApplication(sys.argv)

with open("styles/main.qss", 'r', encoding="utf-8") as styleSheetFile:
	app.setStyleSheet(styleSheetFile.read())

window = ViewMainWindow()
controllWindow = ControllerMainWindow(window)
window.show()
app.exec()

# Lệnh push github
# git add .
# git commit -m "Comment"
# git push