# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tran.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HeaderT(object):
    def setupUi(self, HeaderT):
        HeaderT.setObjectName("HeaderT")
        HeaderT.resize(474, 376)
        self.centralwidget = QtWidgets.QWidget(HeaderT)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        HeaderT.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HeaderT)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 474, 23))
        self.menubar.setObjectName("menubar")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        HeaderT.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HeaderT)
        self.statusbar.setObjectName("statusbar")
        HeaderT.setStatusBar(self.statusbar)
        self.actionfile = QtWidgets.QAction(HeaderT)
        self.actionfile.setObjectName("actionfile")
        self.menutest.addAction(self.actionfile)
        self.menubar.addAction(self.menutest.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(HeaderT)
        self.pushButton.clicked.connect(self.button_clicked)
        QtCore.QMetaObject.connectSlotsByName(HeaderT)

    def retranslateUi(self, HeaderT):
        _translate = QtCore.QCoreApplication.translate
        HeaderT.setWindowTitle(_translate("HeaderT", "MainWindow"))
        self.label.setText(_translate("HeaderT", "请输入想要转换的header:"))
        self.label_2.setText(_translate("HeaderT", "字典:"))
        self.pushButton.setText(_translate("HeaderT", "转换"))
        self.pushButton_2.setText(_translate("HeaderT", "导出"))
        self.menutest.setTitle(_translate("HeaderT", "File"))
        self.menuHelp.setTitle(_translate("HeaderT", "Help"))
        self.actionfile.setText(_translate("HeaderT", "save"))



    def button_clicked(self):
        self.statusbar.showMessage("you clicked the trainslate button")
        # print(self.textEdit.toPlainText())
        try:
            headers = dict([line.split(": ", 1) for line in """{}""".format(self.textEdit.toPlainText()).split("\n")])
            self.textBrowser.clear()
            self.textBrowser.append(str(headers))
        except Exception as e:
            print(e)
        # self.textBrowser.append(str(headers))