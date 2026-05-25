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
from View.ViewReviewDialog import ViewReviewDialog
from View.ViewReviewDialog import ViewReviewTag
from View.QDefine import QuestionEdit,  ViewSettingDialog

from Controller.ControllerMainWindow import ControllerMainWindow
from Controller.ControllerNoteBlock import ControllerNoteBlock
from Controller.ControllerChapterBlock import ControllerChapterBlock
from Controller.ControllerTrashPage import ControllerTrashPage
from Controller.ControllerSubjectPage import ControllerSubjectPage
from Controller.ControllerSidebar import ControllerSidebar
from Controller.ControllerCreateNoteDialog import ControllerCreateNoteDialog
from Controller.ControllerHomePage import ControllerHomePage
from Controller.ControllerReviewDialog import ControllerReviewDialog

import sys
from PyQt6.QtWidgets import QApplication

from View.QDefine import InputDialog

app = QApplication(sys.argv)
window = ViewMainWindow()

viewNoteBlock = ViewNoteBlock("Đây là CSDL nhưng nó phân tán :)", "CSDLPT là gì?", 20)
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

viewReviewDialog = ViewReviewDialog("Đây là CSDL nhưng nó phân tán :)", "CSDLPT là gì?", 20)
controllerReviewDialog = ControllerReviewDialog(viewReviewDialog)

viewReviewTag = ViewReviewTag("detroit", "ý nghĩa", 1, "đây là đâu?", "đây là detroit")
questionEdit = QuestionEdit("Đây là đâu", 1)

viewSettingDialog = ViewSettingDialog()

print("Test thành công")
viewSettingDialog.show()
app.exec()

print("Kết thúc")