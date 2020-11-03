# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1163, 737)
        MainWindow.setStyleSheet("background-color: rgb(58, 67, 81);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(39, 45, 54);\n"
"border:0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Ubuntu\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(0, 0, 0); \n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        spacerItem = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox, 0, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(165, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.test = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test.sizePolicy().hasHeightForWidth())
        self.test.setSizePolicy(sizePolicy)
        self.test.setMinimumSize(QtCore.QSize(3, 0))
        self.test.setMaximumSize(QtCore.QSize(16777215, 16777193))
        self.test.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    color: rgb(0, 0, 0);\n"
"    border: 1; \n"
"    padding: 10px; \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(79, 92, 111)\n"
"}")
        self.test.setObjectName("test")
        self.horizontalLayout_4.addWidget(self.test)
        spacerItem2 = QtWidgets.QSpacerItem(165, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Ubuntu\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(39, 45, 54);\n"
"border:0;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255)")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_4.addWidget(self.listWidget)
        spacerItem3 = QtWidgets.QSpacerItem(20, 114, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.use = QtWidgets.QPushButton(self.frame_2)
        self.use.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    color: rgb(0, 0, 0);\n"
"    border: 1; \n"
"    padding: 10px; \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(79, 92, 111)\n"
"}")
        self.use.setObjectName("use")
        self.horizontalLayout_3.addWidget(self.use)
        self.add = QtWidgets.QPushButton(self.frame_2)
        self.add.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    color: rgb(0, 0, 0);\n"
"    border: 1; \n"
"    padding: 10px; \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(79, 92, 111)\n"
"}")
        self.add.setObjectName("add")
        self.horizontalLayout_3.addWidget(self.add)
        self.edit = QtWidgets.QPushButton(self.frame_2)
        self.edit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    color: rgb(0, 0, 0);\n"
"    border: 1; \n"
"    padding: 10px; \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(79, 92, 111)\n"
"}")
        self.edit.setObjectName("edit")
        self.horizontalLayout_3.addWidget(self.edit)
        self.delete_2 = QtWidgets.QPushButton(self.frame_2)
        self.delete_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    color: rgb(0, 0, 0);\n"
"    border: 1; \n"
"    padding: 10px; \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(79, 92, 111)\n"
"}")
        self.delete_2.setObjectName("delete_2")
        self.horizontalLayout_3.addWidget(self.delete_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 114, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(0, 0, 0); \n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 22))
        self.menubar.setObjectName("menubar")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setGeometry(QtCore.QRect(330, 152, 200, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuTest.sizePolicy().hasHeightForWidth())
        self.menuTest.setSizePolicy(sizePolicy)
        self.menuTest.setObjectName("menuTest")
        self.menuHilfe = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuHilfe.sizePolicy().hasHeightForWidth())
        self.menuHilfe.setSizePolicy(sizePolicy)
        self.menuHilfe.setObjectName("menuHilfe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHilfe = QtWidgets.QAction(MainWindow)
        self.actionHilfe.setObjectName("actionHilfe")
        self.action_ber = QtWidgets.QAction(MainWindow)
        self.action_ber.setObjectName("action_ber")
        self.actionbeenden = QtWidgets.QAction(MainWindow)
        self.actionbeenden.setObjectName("actionbeenden")
        self.actionHilfe_2 = QtWidgets.QAction(MainWindow)
        self.actionHilfe_2.setObjectName("actionHilfe_2")
        self.actionueber = QtWidgets.QAction(MainWindow)
        self.actionueber.setObjectName("actionueber")
        self.menuTest.addAction(self.actionbeenden)
        self.menuHilfe.addAction(self.actionHilfe_2)
        self.menuHilfe.addAction(self.actionueber)
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Hier bitte den zu überprüfenden Ausdruck eingeben"))
        self.label_3.setText(_translate("MainWindow", "Wähle einen Ausdruck...."))
        self.checkBox.setText(_translate("MainWindow", "Groß-Kleinschreibung beachten"))
        self.test.setText(_translate("MainWindow", "überprüfen"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Es wurde noch nichts überprüft....</p></body></html>"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Hallo Welt"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.use.setText(_translate("MainWindow", "benutzen"))
        self.add.setText(_translate("MainWindow", "hinzufügen"))
        self.edit.setText(_translate("MainWindow", "bearbeiten"))
        self.delete_2.setText(_translate("MainWindow", "löschen"))
        self.label.setText(_translate("MainWindow", "Füge einen neuen Ausdruck hinzu"))
        self.menuTest.setTitle(_translate("MainWindow", "Datei"))
        self.menuHilfe.setTitle(_translate("MainWindow", "Hilfe"))
        self.actionHilfe.setText(_translate("MainWindow", "Hilfe"))
        self.action_ber.setText(_translate("MainWindow", "Über"))
        self.actionbeenden.setText(_translate("MainWindow", "beenden"))
        self.actionHilfe_2.setText(_translate("MainWindow", "Hilfe"))
        self.actionueber.setText(_translate("MainWindow", "Über"))
