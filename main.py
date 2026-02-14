from services.TacVuMonHoc import(
	layDanhSachMon, themMon, capNhatTruyCapGanNhat, suaTenMon, moveMonToTrash, khoiPhucMon, xoaMon, layDanhSachMonTrash
) 
from ui.main_window import Sidebar, MainWindow
import sys
from PyQt6.QtWidgets import QApplication



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

