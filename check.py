from PyQt6.QtCore import QFileInfo

file_path = "Baotangcuasutiecnuoi/imageforproject/image/back1.png"
file_info = QFileInfo(file_path)

if file_info.exists():
    print("File found!")
else:
    print("File not found!")
