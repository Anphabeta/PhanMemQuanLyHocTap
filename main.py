from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from View import ViewMainWindow
from Controller import ControllerMainWindow
import styles.get_styles as get_styles
import sys
import ctypes
try:
    myappid = 'helloworld'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception as e:
    print("Không thể thiết lập AppUserModelID:", e)

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("assets/icon.svg"))
get_styles.load(app)

window = ViewMainWindow()
controllWindow = ControllerMainWindow(window)
window.show()
app.exec()

# Lệnh push github
# git add .
# git commit -m "Comment"
# git push