# Form implementation generated from reading ui file '/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/MuseumDesign.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.setEnabled(True)
        StackedWidget.resize(1280, 664)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setKerning(True)
        StackedWidget.setFont(font)
        StackedWidget.setAutoFillBackground(True)
        StackedWidget.setStyleSheet("#page{ \n"
"background-image: url(\'/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/background1.png\');\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;\n"
"}\n"
"#page_2{ \n"
"background-image: url(\'/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/France.png\');\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;\n"
"}\n"
"#page_3{ \n"
"background-image: url(\'/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/Vietnam.png\');\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;\n"
"}\n"
"#page_4{ \n"
"background-image: url(\'/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/Spain.png\');\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;\n"
"}\n"
"#page_5{ \n"
"background-image: url(\'/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/analysis.png\');\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;\n"
"}\n"
"#page_6{ \n"
"background-image: url(\'/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/Goodbye.png\');\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;\n"
"}")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(parent=self.page)
        self.label.setGeometry(QtCore.QRect(840, 250, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.page)
        self.label_2.setGeometry(QtCore.QRect(530, 180, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.page)
        self.label_3.setGeometry(QtCore.QRect(530, 490, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.page)
        self.label_4.setGeometry(QtCore.QRect(690, 500, 611, 191))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.checkBox_10 = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_10.setGeometry(QtCore.QRect(0, 50, 91, 81))
        self.checkBox_10.setStyleSheet("QCheckBox::indicator:checked {\n"
"    opacity: 0.5;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    opacity: 0.5;\n"
"}\n"
"#toolButton_10 {\n"
"    opacity: 0.5;  /* Đặt độ mờ cho toàn bộ nút */\n"
"}\n"
"\n"
"")
        self.checkBox_10.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/cd.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.checkBox_10.setIcon(icon)
        self.checkBox_10.setIconSize(QtCore.QSize(70, 70))
        self.checkBox_10.setObjectName("checkBox_10")
        self.toolButton = QtWidgets.QToolButton(parent=self.page)
        self.toolButton.setGeometry(QtCore.QRect(1220, 380, 51, 51))
        self.toolButton.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 50);  /* Nền màu đen mờ */\n"
"    border: none;  /* Không có viền */\n"
"}\n"
"\n"
"QToolButton::icon {\n"
"    opacity: 1; \n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/lui.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(25, 25))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.checkBox_10.raise_()
        StackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.checkBox_6 = QtWidgets.QCheckBox(parent=self.page_2)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 60, 91, 81))
        self.checkBox_6.setStyleSheet("QCheckBox::indicator:checked {\n"
"    opacity: 0.5;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    opacity: 0.5;\n"
"}\n"
"\n"
"")
        self.checkBox_6.setText("")
        self.checkBox_6.setIcon(icon)
        self.checkBox_6.setIconSize(QtCore.QSize(70, 70))
        self.checkBox_6.setObjectName("checkBox_6")
        self.toolButton_2 = QtWidgets.QToolButton(parent=self.page_2)
        self.toolButton_2.setGeometry(QtCore.QRect(1200, 350, 51, 51))
        self.toolButton_2.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 50);  /* Nền màu đen mờ */\n"
"    border: none;  /* Không có viền */\n"
"}\n"
"\n"
"QToolButton::icon {\n"
"    opacity: 1; \n"
"}\n"
"\n"
"")
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(parent=self.page_2)
        self.toolButton_3.setGeometry(QtCore.QRect(30, 350, 51, 51))
        self.toolButton_3.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 50);  /* Nền màu đen mờ */\n"
"    border: none;  /* Không có viền */\n"
"}\n"
"\n"
"QToolButton::icon {\n"
"    opacity: 1; \n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/pass.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_3.setObjectName("toolButton_3")
        StackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_8 = QtWidgets.QLabel(parent=self.page_3)
        self.label_8.setGeometry(QtCore.QRect(290, 160, 681, 551))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/C:/Users/ASUS/Downloads/168 Of The Most Famous Paintings In Art History (1).jpg"))
        self.label_8.setObjectName("label_8")
        self.checkBox_7 = QtWidgets.QCheckBox(parent=self.page_3)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 140, 91, 81))
        self.checkBox_7.setStyleSheet("QCheckBox::indicator:checked {\n"
"    opacity: 0.5;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    opacity: 0.5;\n"
"}\n"
"\n"
"")
        self.checkBox_7.setText("")
        self.checkBox_7.setIcon(icon)
        self.checkBox_7.setIconSize(QtCore.QSize(70, 70))
        self.checkBox_7.setObjectName("checkBox_7")
        self.toolButton_4 = QtWidgets.QToolButton(parent=self.page_3)
        self.toolButton_4.setGeometry(QtCore.QRect(1200, 340, 51, 51))
        self.toolButton_4.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 50);  /* Nền màu đen mờ */\n"
"    border: none;  /* Không có viền */\n"
"}\n"
"\n"
"QToolButton::icon {\n"
"    opacity: 1; \n"
"}\n"
"\n"
"")
        self.toolButton_4.setIcon(icon1)
        self.toolButton_4.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_7 = QtWidgets.QToolButton(parent=self.page_3)
        self.toolButton_7.setGeometry(QtCore.QRect(30, 340, 51, 51))
        self.toolButton_7.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 50);  /* Nền màu đen mờ */\n"
"    border: none;  /* Không có viền */\n"
"}\n"
"\n"
"QToolButton::icon {\n"
"    opacity: 1; \n"
"}\n"
"\n"
"")
        self.toolButton_7.setIcon(icon2)
        self.toolButton_7.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_7.setObjectName("toolButton_7")
        StackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_13 = QtWidgets.QLabel(parent=self.page_4)
        self.label_13.setGeometry(QtCore.QRect(370, 20, 511, 671))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/C:/Users/ASUS/Downloads/thiếunu.jpg"))
        self.label_13.setObjectName("label_13")
        self.checkBox_8 = QtWidgets.QCheckBox(parent=self.page_4)
        self.checkBox_8.setGeometry(QtCore.QRect(30, 10, 91, 81))
        self.checkBox_8.setStyleSheet("QCheckBox::indicator:checked {\n"
"    opacity: 0.5;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    opacity: 0.5;\n"
"}\n"
"\n"
"")
        self.checkBox_8.setText("")
        self.checkBox_8.setIcon(icon)
        self.checkBox_8.setIconSize(QtCore.QSize(70, 70))
        self.checkBox_8.setObjectName("checkBox_8")
        self.toolButton_5 = QtWidgets.QToolButton(parent=self.page_4)
        self.toolButton_5.setGeometry(QtCore.QRect(1200, 360, 51, 51))
        self.toolButton_5.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 50);  /* Nền màu đen mờ */\n"
"    border: none;  /* Không có viền */\n"
"}\n"
"\n"
"QToolButton::icon {\n"
"    opacity: 1; \n"
"}\n"
"\n"
"")
        self.toolButton_5.setIcon(icon1)
        self.toolButton_5.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_8 = QtWidgets.QToolButton(parent=self.page_4)
        self.toolButton_8.setGeometry(QtCore.QRect(30, 350, 51, 51))
        self.toolButton_8.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 50);  /* Nền màu đen mờ */\n"
"    border: none;  /* Không có viền */\n"
"}\n"
"\n"
"QToolButton::icon {\n"
"    opacity: 1; \n"
"}\n"
"\n"
"")
        self.toolButton_8.setIcon(icon2)
        self.toolButton_8.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_8.setObjectName("toolButton_8")
        StackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.checkBox_9 = QtWidgets.QCheckBox(parent=self.page_5)
        self.checkBox_9.setGeometry(QtCore.QRect(0, 10, 91, 81))
        self.checkBox_9.setStyleSheet("QCheckBox::indicator:checked {\n"
"    opacity: 0.5;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    opacity: 0.5;\n"
"}\n"
"\n"
"")
        self.checkBox_9.setText("")
        self.checkBox_9.setIcon(icon)
        self.checkBox_9.setIconSize(QtCore.QSize(70, 70))
        self.checkBox_9.setObjectName("checkBox_9")
        self.toolButton_6 = QtWidgets.QToolButton(parent=self.page_5)
        self.toolButton_6.setGeometry(QtCore.QRect(1210, 310, 51, 51))
        self.toolButton_6.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 50);  /* Nền màu đen mờ */\n"
"    border: none;  /* Không có viền */\n"
"}\n"
"\n"
"QToolButton::icon {\n"
"    opacity: 1; \n"
"}\n"
"\n"
"")
        self.toolButton_6.setIcon(icon1)
        self.toolButton_6.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_9 = QtWidgets.QToolButton(parent=self.page_5)
        self.toolButton_9.setGeometry(QtCore.QRect(10, 300, 51, 51))
        self.toolButton_9.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 50);  /* Nền màu đen mờ */\n"
"    border: none;  /* Không có viền */\n"
"}\n"
"\n"
"QToolButton::icon {\n"
"    opacity: 1; \n"
"}\n"
"\n"
"")
        self.toolButton_9.setIcon(icon2)
        self.toolButton_9.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_9.setObjectName("toolButton_9")
        self.label_5 = QtWidgets.QLabel(parent=self.page_5)
        self.label_5.setGeometry(QtCore.QRect(270, 80, 751, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(parent=self.page_5)
        self.radioButton.setGeometry(QtCore.QRect(540, 160, 221, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton.setFont(font)
        self.radioButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/France1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton.setIcon(icon3)
        self.radioButton.setIconSize(QtCore.QSize(200, 200))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.page_5)
        self.radioButton_2.setGeometry(QtCore.QRect(540, 320, 221, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/Vietnam1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_2.setIcon(icon4)
        self.radioButton_2.setIconSize(QtCore.QSize(200, 200))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.page_5)
        self.radioButton_3.setGeometry(QtCore.QRect(540, 480, 221, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/Spain1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_3.setIcon(icon5)
        self.radioButton_3.setIconSize(QtCore.QSize(200, 200))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.page_5)
        self.pushButton.setGeometry(QtCore.QRect(290, 290, 113, 32))
        self.pushButton.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.page_5)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 370, 113, 32))
        self.pushButton_2.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.page_5)
        self.groupBox.setGeometry(QtCore.QRect(860, 260, 221, 151))
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 113, 21))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: 1px solid #ccc;  /* Bạn có thể thêm border nếu cần */\n"
"    color: black;  /* Màu chữ */\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 100, 113, 21))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: 1px solid #ccc;  /* Bạn có thể thêm border nếu cần */\n"
"    color: black;  /* Màu chữ */\n"
"}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        StackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.toolButton_10 = QtWidgets.QToolButton(parent=self.page_6)
        self.toolButton_10.setGeometry(QtCore.QRect(10, 320, 51, 51))
        self.toolButton_10.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 50);  /* Nền màu đen mờ */\n"
"    border: none;  /* Không có viền */\n"
"}\n"
"\n"
"QToolButton::icon {\n"
"    opacity: 1; \n"
"}\n"
"\n"
"")
        self.toolButton_10.setIcon(icon2)
        self.toolButton_10.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_10.setObjectName("toolButton_10")
        StackedWidget.addWidget(self.page_6)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        self.toolButton.clicked.connect(self.page.repaint) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.label.setText(_translate("StackedWidget", "NGUYEN NGOC AI THIEN"))
        self.label_2.setText(_translate("StackedWidget", "NGUYEN QUANG VINH"))
        self.label_3.setText(_translate("StackedWidget", "LE DOAN QUOC KHANH"))
        self.label_4.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" color:#7f081d;\">ENJOY ART\'S DIMENSION</span></p></body></html>"))
        self.toolButton.setText(_translate("StackedWidget", "..."))
        self.toolButton_2.setText(_translate("StackedWidget", "..."))
        self.toolButton_3.setText(_translate("StackedWidget", "..."))
        self.toolButton_4.setText(_translate("StackedWidget", "..."))
        self.toolButton_7.setText(_translate("StackedWidget", "..."))
        self.toolButton_5.setText(_translate("StackedWidget", "..."))
        self.toolButton_8.setText(_translate("StackedWidget", "..."))
        self.toolButton_6.setText(_translate("StackedWidget", "..."))
        self.toolButton_9.setText(_translate("StackedWidget", "..."))
        self.label_5.setText(_translate("StackedWidget", "Which painting do you like the most?"))
        self.pushButton.setText(_translate("StackedWidget", "PushResult"))
        self.pushButton_2.setText(_translate("StackedWidget", "WatchResult"))
        self.groupBox.setTitle(_translate("StackedWidget", "Results"))
        self.label_6.setText(_translate("StackedWidget", "No.of.votes"))
        self.label_7.setText(_translate("StackedWidget", "Winners"))
        self.toolButton_10.setText(_translate("StackedWidget", "..."))
