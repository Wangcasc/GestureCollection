# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MAIN_WINDOW(object):
    def setupUi(self, MAIN_WINDOW):
        MAIN_WINDOW.setObjectName("MAIN_WINDOW")
        MAIN_WINDOW.resize(1621, 846)
        self.tabWidget = QtWidgets.QTabWidget(MAIN_WINDOW)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 1601, 791))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(18)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_RGB_0 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_RGB_0.setGeometry(QtCore.QRect(910, 50, 631, 661))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.groupBox_RGB_0.setFont(font)
        self.groupBox_RGB_0.setStyleSheet("QGroupBox {     \n"
"border: 1px solid gray;     \n"
"border-radius: 9px;     \n"
"margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {     \n"
"subcontrol-origin: margin;     \n"
"left: 10px;     \n"
"padding: 0 3px 0 3px;\n"
" }")
        self.groupBox_RGB_0.setObjectName("groupBox_RGB_0")
        self.groupBox_RGB_1 = QtWidgets.QGroupBox(self.groupBox_RGB_0)
        self.groupBox_RGB_1.setGeometry(QtCore.QRect(220, 230, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_RGB_1.setFont(font)
        self.groupBox_RGB_1.setObjectName("groupBox_RGB_1")
        self.label_RGB = QtWidgets.QLabel(self.groupBox_RGB_1)
        self.label_RGB.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_RGB.setText("")
        self.label_RGB.setObjectName("label_RGB")
        self.groupBox_RGB_2 = QtWidgets.QGroupBox(self.groupBox_RGB_0)
        self.groupBox_RGB_2.setGeometry(QtCore.QRect(220, 20, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_RGB_2.setFont(font)
        self.groupBox_RGB_2.setObjectName("groupBox_RGB_2")
        self.label_RGB_2 = QtWidgets.QLabel(self.groupBox_RGB_2)
        self.label_RGB_2.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_RGB_2.setText("")
        self.label_RGB_2.setObjectName("label_RGB_2")
        self.groupBox_RGB_3 = QtWidgets.QGroupBox(self.groupBox_RGB_0)
        self.groupBox_RGB_3.setGeometry(QtCore.QRect(220, 440, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_RGB_3.setFont(font)
        self.groupBox_RGB_3.setObjectName("groupBox_RGB_3")
        self.label_RGB_3 = QtWidgets.QLabel(self.groupBox_RGB_3)
        self.label_RGB_3.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_RGB_3.setText("")
        self.label_RGB_3.setObjectName("label_RGB_3")
        self.groupBox_RGB_4 = QtWidgets.QGroupBox(self.groupBox_RGB_0)
        self.groupBox_RGB_4.setGeometry(QtCore.QRect(20, 230, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_RGB_4.setFont(font)
        self.groupBox_RGB_4.setObjectName("groupBox_RGB_4")
        self.label_RGB_4 = QtWidgets.QLabel(self.groupBox_RGB_4)
        self.label_RGB_4.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_RGB_4.setText("")
        self.label_RGB_4.setObjectName("label_RGB_4")
        self.groupBox_RGB_5 = QtWidgets.QGroupBox(self.groupBox_RGB_0)
        self.groupBox_RGB_5.setGeometry(QtCore.QRect(420, 230, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_RGB_5.setFont(font)
        self.groupBox_RGB_5.setObjectName("groupBox_RGB_5")
        self.label_RGB_5 = QtWidgets.QLabel(self.groupBox_RGB_5)
        self.label_RGB_5.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_RGB_5.setText("")
        self.label_RGB_5.setObjectName("label_RGB_5")
        self.label_frameRates_1 = QtWidgets.QLabel(self.groupBox_RGB_0)
        self.label_frameRates_1.setGeometry(QtCore.QRect(260, 420, 101, 21))
        self.label_frameRates_1.setObjectName("label_frameRates_1")
        self.label_frameRates_2 = QtWidgets.QLabel(self.groupBox_RGB_0)
        self.label_frameRates_2.setGeometry(QtCore.QRect(260, 210, 101, 21))
        self.label_frameRates_2.setObjectName("label_frameRates_2")
        self.label_frameRates_3 = QtWidgets.QLabel(self.groupBox_RGB_0)
        self.label_frameRates_3.setGeometry(QtCore.QRect(260, 630, 101, 21))
        self.label_frameRates_3.setObjectName("label_frameRates_3")
        self.label_frameRates_4 = QtWidgets.QLabel(self.groupBox_RGB_0)
        self.label_frameRates_4.setGeometry(QtCore.QRect(50, 420, 111, 21))
        self.label_frameRates_4.setObjectName("label_frameRates_4")
        self.label_frameRates_5 = QtWidgets.QLabel(self.groupBox_RGB_0)
        self.label_frameRates_5.setGeometry(QtCore.QRect(450, 420, 111, 21))
        self.label_frameRates_5.setObjectName("label_frameRates_5")
        self.groupBox_RGB_6 = QtWidgets.QGroupBox(self.groupBox_RGB_0)
        self.groupBox_RGB_6.setGeometry(QtCore.QRect(20, 20, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_RGB_6.setFont(font)
        self.groupBox_RGB_6.setObjectName("groupBox_RGB_6")
        self.label_RGB_6 = QtWidgets.QLabel(self.groupBox_RGB_6)
        self.label_RGB_6.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_RGB_6.setText("")
        self.label_RGB_6.setObjectName("label_RGB_6")
        self.label_frameRates_6 = QtWidgets.QLabel(self.groupBox_RGB_0)
        self.label_frameRates_6.setGeometry(QtCore.QRect(50, 210, 111, 21))
        self.label_frameRates_6.setObjectName("label_frameRates_6")
        self.groupBox_RGB_7 = QtWidgets.QGroupBox(self.groupBox_RGB_0)
        self.groupBox_RGB_7.setGeometry(QtCore.QRect(420, 20, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_RGB_7.setFont(font)
        self.groupBox_RGB_7.setObjectName("groupBox_RGB_7")
        self.label_RGB_7 = QtWidgets.QLabel(self.groupBox_RGB_7)
        self.label_RGB_7.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_RGB_7.setText("")
        self.label_RGB_7.setObjectName("label_RGB_7")
        self.label_frameRates_7 = QtWidgets.QLabel(self.groupBox_RGB_0)
        self.label_frameRates_7.setGeometry(QtCore.QRect(460, 210, 111, 21))
        self.label_frameRates_7.setObjectName("label_frameRates_7")
        self.groupBox_regist = QtWidgets.QGroupBox(self.tab)
        self.groupBox_regist.setGeometry(QtCore.QRect(10, 10, 681, 271))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.groupBox_regist.setFont(font)
        self.groupBox_regist.setStyleSheet("QGroupBox {     \n"
"border: 1px solid gray;     \n"
"border-radius: 9px;     \n"
"margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {     \n"
"subcontrol-origin: margin;     \n"
"left: 10px;     \n"
"padding: 0 3px 0 3px;\n"
" }")
        self.groupBox_regist.setObjectName("groupBox_regist")
        self.label_NUM = QtWidgets.QLabel(self.groupBox_regist)
        self.label_NUM.setGeometry(QtCore.QRect(250, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_NUM.setFont(font)
        self.label_NUM.setObjectName("label_NUM")
        self.lineEdit_NUM = QtWidgets.QLineEdit(self.groupBox_regist)
        self.lineEdit_NUM.setGeometry(QtCore.QRect(350, 130, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lineEdit_NUM.setFont(font)
        self.lineEdit_NUM.setObjectName("lineEdit_NUM")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.groupBox_regist)
        self.lineEdit_ID.setGeometry(QtCore.QRect(110, 80, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.label_ID = QtWidgets.QLabel(self.groupBox_regist)
        self.label_ID.setGeometry(QtCore.QRect(30, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_ID.setFont(font)
        self.label_ID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ID.setObjectName("label_ID")
        self.pushButton_regist = QtWidgets.QPushButton(self.groupBox_regist)
        self.pushButton_regist.setGeometry(QtCore.QRect(70, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.pushButton_regist.setFont(font)
        self.pushButton_regist.setObjectName("pushButton_regist")
        self.pushButton_del = QtWidgets.QPushButton(self.groupBox_regist)
        self.pushButton_del.setGeometry(QtCore.QRect(540, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setObjectName("pushButton_del")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_regist)
        self.progressBar.setGeometry(QtCore.QRect(260, 230, 411, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_status = QtWidgets.QLabel(self.groupBox_regist)
        self.label_status.setGeometry(QtCore.QRect(50, 230, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.label_scene = QtWidgets.QLabel(self.groupBox_regist)
        self.label_scene.setGeometry(QtCore.QRect(290, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_scene.setFont(font)
        self.label_scene.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_scene.setObjectName("label_scene")
        self.lineEdit_scene = QtWidgets.QLineEdit(self.groupBox_regist)
        self.lineEdit_scene.setGeometry(QtCore.QRect(350, 80, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lineEdit_scene.setFont(font)
        self.lineEdit_scene.setObjectName("lineEdit_scene")
        self.lineEdit_gesture_type = QtWidgets.QLineEdit(self.groupBox_regist)
        self.lineEdit_gesture_type.setGeometry(QtCore.QRect(110, 130, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lineEdit_gesture_type.setFont(font)
        self.lineEdit_gesture_type.setObjectName("lineEdit_gesture_type")
        self.label_gesture_type = QtWidgets.QLabel(self.groupBox_regist)
        self.label_gesture_type.setGeometry(QtCore.QRect(0, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_gesture_type.setFont(font)
        self.label_gesture_type.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_gesture_type.setObjectName("label_gesture_type")
        self.label_session = QtWidgets.QLabel(self.groupBox_regist)
        self.label_session.setGeometry(QtCore.QRect(470, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_session.setFont(font)
        self.label_session.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_session.setObjectName("label_session")
        self.lineEdit_session = QtWidgets.QLineEdit(self.groupBox_regist)
        self.lineEdit_session.setGeometry(QtCore.QRect(530, 80, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lineEdit_session.setFont(font)
        self.lineEdit_session.setObjectName("lineEdit_session")
        self.comboBox_sex = QtWidgets.QComboBox(self.groupBox_regist)
        self.comboBox_sex.setGeometry(QtCore.QRect(350, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.comboBox_sex.setFont(font)
        self.comboBox_sex.setObjectName("comboBox_sex")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.addItem("")
        self.label_sex = QtWidgets.QLabel(self.groupBox_regist)
        self.label_sex.setGeometry(QtCore.QRect(270, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_sex.setFont(font)
        self.label_sex.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_sex.setObjectName("label_sex")
        self.label_age = QtWidgets.QLabel(self.groupBox_regist)
        self.label_age.setGeometry(QtCore.QRect(450, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_age.setFont(font)
        self.label_age.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_age.setObjectName("label_age")
        self.lineEdit_age = QtWidgets.QLineEdit(self.groupBox_regist)
        self.lineEdit_age.setGeometry(QtCore.QRect(530, 30, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lineEdit_age.setFont(font)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox_regist)
        self.lineEdit_name.setGeometry(QtCore.QRect(110, 30, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_name = QtWidgets.QLabel(self.groupBox_regist)
        self.label_name.setGeometry(QtCore.QRect(30, 30, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.label_session.raise_()
        self.lineEdit_session.raise_()
        self.label_NUM.raise_()
        self.lineEdit_NUM.raise_()
        self.lineEdit_ID.raise_()
        self.label_ID.raise_()
        self.pushButton_regist.raise_()
        self.pushButton_del.raise_()
        self.progressBar.raise_()
        self.label_status.raise_()
        self.label_scene.raise_()
        self.lineEdit_scene.raise_()
        self.lineEdit_gesture_type.raise_()
        self.label_gesture_type.raise_()
        self.comboBox_sex.raise_()
        self.label_sex.raise_()
        self.label_age.raise_()
        self.lineEdit_age.raise_()
        self.lineEdit_name.raise_()
        self.label_name.raise_()
        self.groupBox_realsense = QtWidgets.QGroupBox(self.tab)
        self.groupBox_realsense.setGeometry(QtCore.QRect(10, 280, 201, 451))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.groupBox_realsense.setFont(font)
        self.groupBox_realsense.setStyleSheet("QGroupBox {     \n"
"border: 1px solid gray;     \n"
"border-radius: 9px;     \n"
"margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {     \n"
"subcontrol-origin: margin;     \n"
"left: 10px;     \n"
"padding: 0 3px 0 3px;\n"
" }")
        self.groupBox_realsense.setObjectName("groupBox_realsense")
        self.groupBox_realsense_RGB = QtWidgets.QGroupBox(self.groupBox_realsense)
        self.groupBox_realsense_RGB.setGeometry(QtCore.QRect(10, 20, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_realsense_RGB.setFont(font)
        self.groupBox_realsense_RGB.setObjectName("groupBox_realsense_RGB")
        self.label_realsense_RGB = QtWidgets.QLabel(self.groupBox_realsense_RGB)
        self.label_realsense_RGB.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_realsense_RGB.setText("")
        self.label_realsense_RGB.setObjectName("label_realsense_RGB")
        self.groupBox_realsense_Depth = QtWidgets.QGroupBox(self.groupBox_realsense)
        self.groupBox_realsense_Depth.setGeometry(QtCore.QRect(10, 230, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_realsense_Depth.setFont(font)
        self.groupBox_realsense_Depth.setObjectName("groupBox_realsense_Depth")
        self.label_realsense_Depth = QtWidgets.QLabel(self.groupBox_realsense_Depth)
        self.label_realsense_Depth.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_realsense_Depth.setText("")
        self.label_realsense_Depth.setObjectName("label_realsense_Depth")
        self.label_frameRates_realsnece_1 = QtWidgets.QLabel(self.groupBox_realsense)
        self.label_frameRates_realsnece_1.setGeometry(QtCore.QRect(50, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_frameRates_realsnece_1.setFont(font)
        self.label_frameRates_realsnece_1.setObjectName("label_frameRates_realsnece_1")
        self.label_frameRates_realsnece_2 = QtWidgets.QLabel(self.groupBox_realsense)
        self.label_frameRates_realsnece_2.setGeometry(QtCore.QRect(50, 420, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_frameRates_realsnece_2.setFont(font)
        self.label_frameRates_realsnece_2.setObjectName("label_frameRates_realsnece_2")
        self.groupBox_infrared = QtWidgets.QGroupBox(self.tab)
        self.groupBox_infrared.setGeometry(QtCore.QRect(650, 280, 251, 281))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.groupBox_infrared.setFont(font)
        self.groupBox_infrared.setStyleSheet("QGroupBox {     \n"
"border: 1px solid gray;     \n"
"border-radius: 9px;     \n"
"margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {     \n"
"subcontrol-origin: margin;     \n"
"left: 10px;     \n"
"padding: 0 3px 0 3px;\n"
" }")
        self.groupBox_infrared.setObjectName("groupBox_infrared")
        self.groupBox_infrared_2 = QtWidgets.QGroupBox(self.groupBox_infrared)
        self.groupBox_infrared_2.setGeometry(QtCore.QRect(10, 20, 231, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_infrared_2.setFont(font)
        self.groupBox_infrared_2.setObjectName("groupBox_infrared_2")
        self.label_infrared = QtWidgets.QLabel(self.groupBox_infrared_2)
        self.label_infrared.setGeometry(QtCore.QRect(10, 20, 211, 211))
        self.label_infrared.setText("")
        self.label_infrared.setObjectName("label_infrared")
        self.label_frameRates_inf = QtWidgets.QLabel(self.groupBox_infrared)
        self.label_frameRates_inf.setGeometry(QtCore.QRect(110, 260, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_frameRates_inf.setFont(font)
        self.label_frameRates_inf.setObjectName("label_frameRates_inf")
        self.groupBox_event = QtWidgets.QGroupBox(self.tab)
        self.groupBox_event.setGeometry(QtCore.QRect(700, 50, 201, 231))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.groupBox_event.setFont(font)
        self.groupBox_event.setStyleSheet("QGroupBox {     \n"
"border: 1px solid gray;     \n"
"border-radius: 9px;     \n"
"margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {     \n"
"subcontrol-origin: margin;     \n"
"left: 10px;     \n"
"padding: 0 3px 0 3px;\n"
" }")
        self.groupBox_event.setObjectName("groupBox_event")
        self.groupBox_event_2 = QtWidgets.QGroupBox(self.groupBox_event)
        self.groupBox_event_2.setGeometry(QtCore.QRect(10, 20, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_event_2.setFont(font)
        self.groupBox_event_2.setObjectName("groupBox_event_2")
        self.label_event = QtWidgets.QLabel(self.groupBox_event_2)
        self.label_event.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_event.setText("")
        self.label_event.setObjectName("label_event")
        self.label_frameRates_event = QtWidgets.QLabel(self.groupBox_event)
        self.label_frameRates_event.setGeometry(QtCore.QRect(40, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_frameRates_event.setFont(font)
        self.label_frameRates_event.setObjectName("label_frameRates_event")
        self.groupBox_ZED = QtWidgets.QGroupBox(self.tab)
        self.groupBox_ZED.setGeometry(QtCore.QRect(220, 280, 411, 451))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.groupBox_ZED.setFont(font)
        self.groupBox_ZED.setStyleSheet("QGroupBox {     \n"
"border: 1px solid gray;     \n"
"border-radius: 9px;     \n"
"margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {     \n"
"subcontrol-origin: margin;     \n"
"left: 10px;     \n"
"padding: 0 3px 0 3px;\n"
" }")
        self.groupBox_ZED.setObjectName("groupBox_ZED")
        self.groupBox_ZED_RGB = QtWidgets.QGroupBox(self.groupBox_ZED)
        self.groupBox_ZED_RGB.setGeometry(QtCore.QRect(10, 20, 391, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_ZED_RGB.setFont(font)
        self.groupBox_ZED_RGB.setObjectName("groupBox_ZED_RGB")
        self.label_ZED_RGB = QtWidgets.QLabel(self.groupBox_ZED_RGB)
        self.label_ZED_RGB.setGeometry(QtCore.QRect(30, 20, 341, 160))
        self.label_ZED_RGB.setText("")
        self.label_ZED_RGB.setObjectName("label_ZED_RGB")
        self.groupBox_ZED_Depth = QtWidgets.QGroupBox(self.groupBox_ZED)
        self.groupBox_ZED_Depth.setGeometry(QtCore.QRect(100, 230, 181, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_ZED_Depth.setFont(font)
        self.groupBox_ZED_Depth.setObjectName("groupBox_ZED_Depth")
        self.label_ZED_Depth = QtWidgets.QLabel(self.groupBox_ZED_Depth)
        self.label_ZED_Depth.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.label_ZED_Depth.setText("")
        self.label_ZED_Depth.setObjectName("label_ZED_Depth")
        self.label_frameRates_ZED = QtWidgets.QLabel(self.groupBox_ZED)
        self.label_frameRates_ZED.setGeometry(QtCore.QRect(140, 420, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_frameRates_ZED.setFont(font)
        self.label_frameRates_ZED.setObjectName("label_frameRates_ZED")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_sample_frame = QtWidgets.QLabel(self.tab_2)
        self.label_sample_frame.setGeometry(QtCore.QRect(100, 70, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_sample_frame.setFont(font)
        self.label_sample_frame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_sample_frame.setObjectName("label_sample_frame")
        self.lineEdit_sample_frame = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_sample_frame.setGeometry(QtCore.QRect(340, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_sample_frame.setFont(font)
        self.lineEdit_sample_frame.setObjectName("lineEdit_sample_frame")
        self.label_save_path = QtWidgets.QLabel(self.tab_2)
        self.label_save_path.setGeometry(QtCore.QRect(130, 160, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_save_path.setFont(font)
        self.label_save_path.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_save_path.setObjectName("label_save_path")
        self.lineEdit_sample_save_path = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_sample_save_path.setGeometry(QtCore.QRect(340, 160, 811, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_sample_save_path.setFont(font)
        self.lineEdit_sample_save_path.setObjectName("lineEdit_sample_save_path")
        self.pushButton_select_path = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_select_path.setGeometry(QtCore.QRect(1190, 160, 91, 41))
        self.pushButton_select_path.setObjectName("pushButton_select_path")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(MAIN_WINDOW)
        self.label.setGeometry(QtCore.QRect(630, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_scut = QtWidgets.QLabel(MAIN_WINDOW)
        self.label_scut.setGeometry(QtCore.QRect(530, 10, 72, 71))
        self.label_scut.setAutoFillBackground(False)
        self.label_scut.setText("")
        self.label_scut.setScaledContents(True)
        self.label_scut.setObjectName("label_scut")
        self.label_BIP = QtWidgets.QLabel(MAIN_WINDOW)
        self.label_BIP.setGeometry(QtCore.QRect(790, 10, 72, 71))
        self.label_BIP.setText("")
        self.label_BIP.setScaledContents(True)
        self.label_BIP.setObjectName("label_BIP")

        self.retranslateUi(MAIN_WINDOW)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MAIN_WINDOW)

    def retranslateUi(self, MAIN_WINDOW):
        _translate = QtCore.QCoreApplication.translate
        MAIN_WINDOW.setWindowTitle(_translate("MAIN_WINDOW", "MAIN_WINDOW"))
        self.groupBox_RGB_0.setTitle(_translate("MAIN_WINDOW", "RGB相机阵列"))
        self.groupBox_RGB_1.setTitle(_translate("MAIN_WINDOW", "RGB1"))
        self.groupBox_RGB_2.setTitle(_translate("MAIN_WINDOW", "RGB2"))
        self.groupBox_RGB_3.setTitle(_translate("MAIN_WINDOW", "RGB3"))
        self.groupBox_RGB_4.setTitle(_translate("MAIN_WINDOW", "RGB4"))
        self.groupBox_RGB_5.setTitle(_translate("MAIN_WINDOW", "RGB5"))
        self.label_frameRates_1.setText(_translate("MAIN_WINDOW", "0"))
        self.label_frameRates_2.setText(_translate("MAIN_WINDOW", "0"))
        self.label_frameRates_3.setText(_translate("MAIN_WINDOW", "0"))
        self.label_frameRates_4.setText(_translate("MAIN_WINDOW", "0"))
        self.label_frameRates_5.setText(_translate("MAIN_WINDOW", "0"))
        self.groupBox_RGB_6.setTitle(_translate("MAIN_WINDOW", "RGB6"))
        self.label_frameRates_6.setText(_translate("MAIN_WINDOW", "0"))
        self.groupBox_RGB_7.setTitle(_translate("MAIN_WINDOW", "RGB7"))
        self.label_frameRates_7.setText(_translate("MAIN_WINDOW", "0"))
        self.groupBox_regist.setTitle(_translate("MAIN_WINDOW", "注册信息"))
        self.label_NUM.setText(_translate("MAIN_WINDOW", "采样次数："))
        self.lineEdit_NUM.setText(_translate("MAIN_WINDOW", "1"))
        self.lineEdit_ID.setText(_translate("MAIN_WINDOW", "1"))
        self.label_ID.setText(_translate("MAIN_WINDOW", "ID:"))
        self.pushButton_regist.setText(_translate("MAIN_WINDOW", "注册用户"))
        self.pushButton_del.setText(_translate("MAIN_WINDOW", "删除样本"))
        self.label_status.setText(_translate("MAIN_WINDOW", "等待采集"))
        self.label_scene.setText(_translate("MAIN_WINDOW", "场景："))
        self.lineEdit_scene.setText(_translate("MAIN_WINDOW", "1"))
        self.lineEdit_gesture_type.setText(_translate("MAIN_WINDOW", "1"))
        self.label_gesture_type.setText(_translate("MAIN_WINDOW", "手势类别："))
        self.label_session.setText(_translate("MAIN_WINDOW", "时期："))
        self.lineEdit_session.setText(_translate("MAIN_WINDOW", "1"))
        self.comboBox_sex.setItemText(0, _translate("MAIN_WINDOW", "男"))
        self.comboBox_sex.setItemText(1, _translate("MAIN_WINDOW", "女"))
        self.label_sex.setText(_translate("MAIN_WINDOW", "性别："))
        self.label_age.setText(_translate("MAIN_WINDOW", "年龄："))
        self.lineEdit_age.setText(_translate("MAIN_WINDOW", "18"))
        self.lineEdit_name.setText(_translate("MAIN_WINDOW", "test"))
        self.label_name.setText(_translate("MAIN_WINDOW", "姓名:"))
        self.groupBox_realsense.setTitle(_translate("MAIN_WINDOW", "realsense"))
        self.groupBox_realsense_RGB.setTitle(_translate("MAIN_WINDOW", "RGB"))
        self.groupBox_realsense_Depth.setTitle(_translate("MAIN_WINDOW", "Depth"))
        self.label_frameRates_realsnece_1.setText(_translate("MAIN_WINDOW", "0"))
        self.label_frameRates_realsnece_2.setText(_translate("MAIN_WINDOW", "0"))
        self.groupBox_infrared.setTitle(_translate("MAIN_WINDOW", "Infrared"))
        self.groupBox_infrared_2.setTitle(_translate("MAIN_WINDOW", "infrared"))
        self.label_frameRates_inf.setText(_translate("MAIN_WINDOW", "0"))
        self.groupBox_event.setTitle(_translate("MAIN_WINDOW", "Event"))
        self.groupBox_event_2.setTitle(_translate("MAIN_WINDOW", "event"))
        self.label_frameRates_event.setText(_translate("MAIN_WINDOW", "0"))
        self.groupBox_ZED.setTitle(_translate("MAIN_WINDOW", "ZED"))
        self.groupBox_ZED_RGB.setTitle(_translate("MAIN_WINDOW", "RGB"))
        self.groupBox_ZED_Depth.setTitle(_translate("MAIN_WINDOW", "Depth"))
        self.label_frameRates_ZED.setText(_translate("MAIN_WINDOW", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MAIN_WINDOW", "图像显示"))
        self.label_sample_frame.setText(_translate("MAIN_WINDOW", "采样帧数："))
        self.lineEdit_sample_frame.setText(_translate("MAIN_WINDOW", "120"))
        self.label_save_path.setText(_translate("MAIN_WINDOW", "存储路径："))
        self.lineEdit_sample_save_path.setText(_translate("MAIN_WINDOW", "../data"))
        self.pushButton_select_path.setText(_translate("MAIN_WINDOW", "选择"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MAIN_WINDOW", "整体设置"))
        self.label.setText(_translate("MAIN_WINDOW", "多路采集系统"))
