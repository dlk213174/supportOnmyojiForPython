# Form implementation generated from reading ui file 'c:\Users\DLK_WIN\supportOnmyojiForPython\GUI.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(210, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 200, 560))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(80, 0, 100, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 20, 100, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 0, 80, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 80, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(0, 40, 80, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(0, 60, 80, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(0, 80, 80, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(0, 100, 80, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(0, 120, 80, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(0, 180, 80, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(0, 220, 80, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(0, 200, 80, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(0, 140, 80, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(0, 160, 80, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(0, 240, 80, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(0, 300, 80, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(0, 260, 80, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(0, 320, 80, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(0, 280, 80, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(0, 340, 80, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(0, 400, 80, 20))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(0, 360, 80, 20))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(0, 420, 80, 20))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(0, 380, 80, 20))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(0, 440, 80, 20))
        self.label_23.setObjectName("label_23")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(0, 460, 80, 20))
        self.label_25.setObjectName("label_25")
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(0, 480, 80, 20))
        self.label_27.setObjectName("label_27")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 40, 100, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 60, 100, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 80, 100, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 100, 100, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 160, 100, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(80, 140, 100, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 120, 100, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(80, 180, 100, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_11.setGeometry(QtCore.QRect(80, 200, 100, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 260, 100, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_13.setGeometry(QtCore.QRect(80, 240, 100, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_14.setGeometry(QtCore.QRect(80, 220, 100, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_15.setGeometry(QtCore.QRect(80, 280, 100, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_16.setGeometry(QtCore.QRect(80, 300, 100, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_17.setGeometry(QtCore.QRect(80, 360, 100, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_18.setGeometry(QtCore.QRect(80, 340, 100, 20))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_19.setGeometry(QtCore.QRect(80, 320, 100, 20))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_20.setGeometry(QtCore.QRect(80, 380, 100, 20))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_21.setGeometry(QtCore.QRect(80, 400, 100, 20))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_22.setGeometry(QtCore.QRect(80, 460, 100, 20))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_23.setGeometry(QtCore.QRect(80, 440, 100, 20))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_24.setGeometry(QtCore.QRect(80, 420, 100, 20))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_25.setGeometry(QtCore.QRect(80, 480, 100, 20))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(60, 500, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 210, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setTabletTracking(True)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        self.action1.setFont(font)
        self.action1.setObjectName("action1")
        self.action2 = QtGui.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action1_2 = QtGui.QAction(MainWindow)
        self.action1_2.setObjectName("action1_2")
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SOFP"))
        self.label.setText(_translate("MainWindow", "window_0"))
        self.label_2.setText(_translate("MainWindow", "window_0"))
        self.label_3.setText(_translate("MainWindow", "preset_war"))
        self.label_4.setText(_translate("MainWindow", "preset_def"))
        self.label_5.setText(_translate("MainWindow", "preset_sog"))
        self.label_6.setText(_translate("MainWindow", "preset_mit"))
        self.label_7.setText(_translate("MainWindow", "preset_exp"))
        self.label_8.setText(_translate("MainWindow", "times_mit"))
        self.label_9.setText(_translate("MainWindow", "sleep_war"))
        self.label_10.setText(_translate("MainWindow", "times_exp"))
        self.label_11.setText(_translate("MainWindow", "times_def"))
        self.label_12.setText(_translate("MainWindow", "times_sog"))
        self.label_13.setText(_translate("MainWindow", "sleep_def"))
        self.label_14.setText(_translate("MainWindow", "sleep_exp"))
        self.label_15.setText(_translate("MainWindow", "sleep_sog"))
        self.label_16.setText(_translate("MainWindow", "buff_exp_0"))
        self.label_17.setText(_translate("MainWindow", "sleep_mit"))
        self.label_18.setText(_translate("MainWindow", "buff_exp_1"))
        self.label_19.setText(_translate("MainWindow", "option_war"))
        self.label_20.setText(_translate("MainWindow", "buff_mit_0"))
        self.label_21.setText(_translate("MainWindow", "option_aera"))
        self.label_22.setText(_translate("MainWindow", "buff_mit_1"))
        self.label_23.setText(_translate("MainWindow", "option_team"))
        self.label_25.setText(_translate("MainWindow", "option_det_1"))
        self.label_27.setText(_translate("MainWindow", "option_det_2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "????????????"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menu.setTitle(_translate("MainWindow", "??????"))
        self.action1.setText(_translate("MainWindow", "????????????"))
        self.action2.setText(_translate("MainWindow", "????????????"))
        self.action1_2.setText(_translate("MainWindow", "1"))
