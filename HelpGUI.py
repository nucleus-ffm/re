# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(800, 600)
        HelpWindow.setStyleSheet("background-color: rgb(58, 67, 81);\n"
"color: rgb(255, 255, 255);\n"
"border:0;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.ok = QtWidgets.QPushButton(self.frame)
        self.ok.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255); \n"
"    color: rgb(0, 0, 0);\n"
"    border: 1; \n"
"    padding: 10px; \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(79, 92, 111)\n"
"}")
        self.ok.setObjectName("ok")
        self.verticalLayout_2.addWidget(self.ok)
        self.verticalLayout.addWidget(self.frame)
        HelpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        HelpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelpWindow)
        self.statusbar.setObjectName("statusbar")
        HelpWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(HelpWindow)
        self.toolBar.setObjectName("toolBar")
        HelpWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("HelpWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Hilfe:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\">Dieses Programm wurde in </span><span style=\" font-family:\'Basic Roman\'; font-weight:600; color:#ffffff;\">Python 3</span><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\"> geschrieben. Die Muster der regulären Ausdrücke unterliegen den Konventionen des Python-Moduls </span><span style=\" font-family:\'Basic Roman\'; font-weight:600; color:#ffffff;\">re</span><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\">. </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\"> </span><span style=\" color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; font-weight:600; color:#ffffff;\">Hier einige Beispiele: </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\">.     passt auf jedes beliebige Zeichen</span><span style=\" color:#ffffff;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\">*    passt auf 0 oder mehrere Zeichen</span><span style=\" color:#ffffff;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\">+     passt auf mindestens 1 oder mehr Zeichen</span><span style=\" color:#ffffff;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\">?     passt auf 0 oder 1 Zeichen</span><span style=\" color:#ffffff;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\">[...]    passt auf eine gegebene Menge z.b. [a-zA-Z]</span><span style=\" color:#ffffff;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\">(...)     grenzt den Ausdruck ein z.b. (1,5) -&gt; kann 1 bis 5 mal vorkommen.</span><span style=\" color:#ffffff;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\"> </span><span style=\" color:#ffffff;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Basic Roman\'; color:#ffffff;\">Weitere re-Muster finden Sie auf: </span><a href=\"https://docs.python.org/3/library/re.html \"><span style=\" text-decoration: underline; color:#ffffff;\">https://docs.python.org/3/library/re.html </span></a></p></body></html>"))
        self.ok.setText(_translate("HelpWindow", "OK"))
        self.toolBar.setWindowTitle(_translate("HelpWindow", "toolBar"))
