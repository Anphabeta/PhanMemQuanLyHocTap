from services.TacVuMonHoc import(
	layDanhSachMon, themMon, capNhatTruyCapGanNhat, suaTenMon, moveMonToTrash, khoiPhucMon, xoaMon, layDanhSachMonTrash
)
import services.TacVuChuong as TacVuChuong
# from ui.main_window import Sidebar, MainWindow
from uiView import ViewMainWindow
from uiController import ControllerMainWindow
import sys
from PyQt6.QtWidgets import QApplication

from uiView.ViewDialog import InputDialog