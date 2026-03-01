from services.TacVuMonHoc import(
	layDanhSachMon, themMon, capNhatTruyCapGanNhat, suaTenMon, moveMonToTrash, khoiPhucMon, xoaMon, layDanhSachMonTrash
)
import services.TacVuChuong as TacVuChuong
# from ui.main_window import Sidebar, MainWindow
from View import ViewMainWindow
from Controller import ControllerMainWindow
import sys
from PyQt6.QtWidgets import QApplication

from View.ViewDialog import InputDialog