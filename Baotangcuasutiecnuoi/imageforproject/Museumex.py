import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from Museumdesign import Ui_StackedWidget  # Import giao diện

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StackedWidget()  # Khởi tạo giao diện
        self.ui.setupUi(self)         # Thiết lập giao diện từ file .py

        # Thêm logic, ví dụ: chuyển đổi giữa các trang
        self.ui.pushButton.clicked.connect(self.switch_page)

    def switch_page(self):
        # Chuyển đổi giữa các trang trong QStackedWidget
        current_index = self.currentIndex()
        self.setCurrentIndex((current_index + 1) % self.count())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
