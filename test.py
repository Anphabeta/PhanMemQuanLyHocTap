from models.TacVuMonHoc import(
	layDanhSachMon, themMon, capNhatTruyCapGanNhat, suaTenMon, moveMonToTrash, khoiPhucMon, xoaMon, layDanhSachMonTrash
)
import models.TacVuChuong as TacVuChuong
# from ui.main_window import Sidebar, MainWindow
from View.ViewMainWindow import ViewMainWindow
from View.ViewChapterBlock import ViewChapterBlock
from View.ViewNoteBlock import ViewNoteBlock
from View.ViewTrashPage import ViewTrashPage
from View.ViewSubjectPage import ViewSubjectPage
from View.ViewSidebar import ViewSidebar
from View.ViewCreateNoteDialog import ViewCreateNoteDialog
from View.ViewHomePage import ViewHomePage

from Controller.ControllerMainWindow import ControllerMainWindow
from Controller.ControllerNoteBlock import ControllerNoteBlock
from Controller.ControllerChapterBlock import ControllerChapterBlock
from Controller.ControllerTrashPage import ControllerTrashPage
from Controller.ControllerSubjectPage import ControllerSubjectPage
from Controller.ControllerSidebar import ControllerSidebar
from Controller.ControllerCreateNoteDialog import ControllerCreateNoteDialog
from Controller.ControllerHomePage import ControllerHomePage

import sys
from PyQt6.QtWidgets import QApplication

from View.QDefine import InputDialog

app = QApplication(sys.argv)
window = ViewMainWindow()

viewNoteBlock = ViewNoteBlock("abc",1)
controllerNoteBlock = ControllerNoteBlock(viewNoteBlock)

viewChapterBlock = ViewChapterBlock("abc",2)
controllerChapterBlock = ControllerChapterBlock(viewChapterBlock)

viewTrashPage = ViewTrashPage()
controllerTrashPage = ControllerTrashPage(viewTrashPage)

viewSubjectPage = ViewSubjectPage()
controllerSubjectPage = ControllerSubjectPage(viewSubjectPage)

viewSidebar = ViewSidebar()
controllerSidebar = ControllerSidebar(viewSidebar)

viewCreateNoteDialog = ViewCreateNoteDialog()
controllerCreateNoteDialog = ControllerCreateNoteDialog(viewCreateNoteDialog)

viewHomePage = ViewHomePage()
controllerHomePage = ControllerHomePage(viewHomePage)


print("Test thành công")
app.exec()

print("Kết thúc")