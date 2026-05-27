import os

def get_style_path(filename):
	dir_path = os.path.dirname(os.path.abspath(__file__))
	return os.path.join(dir_path, filename)

def load(app):
    styles = []
    
    file_names = ["main.qss", "icon.qss", "dark.qss"]
    
    for file_name in file_names:
        path = get_style_path(file_name)
        if os.path.exists(path):
            with open(path, 'r', encoding="utf-8") as f:
                styles.append(f.read())
                
    combined_style = "\n".join(styles)
    app.setStyleSheet(combined_style)
