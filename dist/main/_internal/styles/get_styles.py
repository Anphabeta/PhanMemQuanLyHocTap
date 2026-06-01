import os
import sys
from PyQt6.QtWidgets import QApplication

def get_style_path(filename):
	dir_path = os.path.dirname(os.path.abspath(__file__))
	return os.path.join(dir_path, filename)

def _build_stylesheet(theme: str) -> str:
    """Đọc và ghép các file QSS theo theme được chọn."""
    styles = []
    file_names = ["main.qss", f"{theme}.qss", "icon.qss"]

    for file_name in file_names:
        path = get_style_path(file_name)
        if os.path.exists(path):
            with open(path, 'r', encoding="utf-8") as f:
                styles.append(f.read())

    # Thay thế đường dẫn tương đối "assets/" thành đường dẫn tuyệt đối
    # để icon/ảnh hiển thị đúng cả khi chạy .exe đã đóng gói
    assets_path = get_resource_path("assets").replace("\\", "/")
    return "\n".join(styles).replace('assets/', f'{assets_path}/')

def load(app: QApplication, theme: str = "dark"):
    """Gọi lần đầu khi khởi động app."""
    app.setStyleSheet(_build_stylesheet(theme))

def reload(theme: str):
    """Gọi khi người dùng đổi theme trong Setting. Lấy app instance tự động."""
    app = QApplication.instance()
    if app is not None:
        app.setStyleSheet(_build_stylesheet(theme))


def get_resource_path(relative_path):
    """ Lấy đường dẫn tuyệt đối chính xác tới tài nguyên """
    try:
        # Khi đóng gói, PyInstaller tạo thư mục tạm và lưu ở sys._MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Khi chạy bình thường bằng python main.py
        # __file__ là styles/get_styles.py, nên cần đi lên 1 cấp để ra thư mục gốc dự án
        styles_dir = os.path.abspath(os.path.dirname(__file__))
        base_path = os.path.dirname(styles_dir)
        
    return os.path.join(base_path, relative_path)