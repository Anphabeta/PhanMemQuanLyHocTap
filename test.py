from models.TacVuMonHoc import(
	layDanhSachMon, themMon, capNhatTruyCapGanNhat, suaTenMon, moveMonToTrash, khoiPhucMon, xoaMon, layDanhSachMonTrash
)
import models.TacVuChuong as TacVuChuong
# from ui.main_window import Sidebar, MainWindow
from View.ViewMainWindow import ViewMainWindow
from View.ViewChapterBlock import ViewChapterBlock
from View.ViewNoteBlock import ViewNoteBlock
from Controller.ControllerMainWindow import ControllerMainWindow
from Controller.ControllerNoteBlock import ControllerNoteBlock
from Controller.ControllerChapterBlock import ControllerChapterBlock
import sys
from PyQt6.QtWidgets import QApplication

from View.ViewDialog import InputDialog

app = QApplication(sys.argv)
window = ViewMainWindow()
viewNoteBlock = ViewNoteBlock("abc",1)
controllerNoteBlock = ControllerNoteBlock(viewNoteBlock)
viewChapterBlock = ViewChapterBlock("abc",2)
controllerChapterBlock = ControllerChapterBlock(viewChapterBlock)

print("Test thành công")
app.exec()

print("Kết thúc")