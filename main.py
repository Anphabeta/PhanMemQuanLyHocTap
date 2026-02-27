from services.TacVuMonHoc import(
	layDanhSachMon, themMon, capNhatTruyCapGanNhat, suaTenMon, moveMonToTrash, khoiPhucMon, xoaMon, layDanhSachMonTrash
) 
# from ui.main_window import Sidebar, MainWindow
from uiView import ViewMainWindow
from uiController import ControllerMainWindow
import sys
from PyQt6.QtWidgets import QApplication

from uiView.ViewDialog import InputDialog


app = QApplication(sys.argv)
window = ViewMainWindow()
controllWindow = ControllerMainWindow(window)
window.show()
app.exec()

# Lệnh push github
# git add .
# git commit -m "Comment"
# git push