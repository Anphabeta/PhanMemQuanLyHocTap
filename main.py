from PyQt6.QtWidgets import QApplication
from View import ViewMainWindow
from Controller import ControllerMainWindow
import sys


app = QApplication(sys.argv)
window = ViewMainWindow()
controllWindow = ControllerMainWindow(window)
window.show()
app.exec()

# Lệnh push github
# git add .
# git commit -m "Comment"
# git push