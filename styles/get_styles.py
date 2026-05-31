import os
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

    return "\n".join(styles)

def load(app: QApplication, theme: str = "dark"):
    """Gọi lần đầu khi khởi động app."""
    app.setStyleSheet(_build_stylesheet(theme))

def reload(theme: str):
    """Gọi khi người dùng đổi theme trong Setting. Lấy app instance tự động."""
    app = QApplication.instance()
    if app is not None:
        app.setStyleSheet(_build_stylesheet(theme))
