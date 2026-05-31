from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from View import ViewMainWindow
from Controller import ControllerMainWindow
import styles.get_styles as get_styles
import repositories.RepoCaiDat as RepoCaiDat
import sys
import ctypes
try:
    myappid = 'helloworld'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception as e:
    print("Không thể thiết lập AppUserModelID:", e)

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("assets/icon.svg"))

# Đọc theme từ cài đặt, mặc định là dark nếu chưa có
settings = RepoCaiDat.layThongTinCaiDat()
theme = settings.get('theme', 'dark') if settings else 'dark'
get_styles.load(app, theme)

window = ViewMainWindow()
controllWindow = ControllerMainWindow(window)
window.show()
app.exec()

# Lệnh push github
# git add .
# git commit -m "Comment"
# git push