# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JarvisUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisVirtualAssistent(object):
    def setupUi(self, JarvisVirtualAssistent):
        JarvisVirtualAssistent.showFullScreen()
        JarvisVirtualAssistent.setObjectName("JarvisVirtualAssistent")
        JarvisVirtualAssistent.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(JarvisVirtualAssistent)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "main-Comp-1.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(585, 360, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        # self.pushButton.setStyleSheet(
        #     "background-color: rgb(0, 0, 0);  color: white;")
        self.pushButton.setObjectName("pushButton")
        JarvisVirtualAssistent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JarvisVirtualAssistent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1371, 26))
        self.menubar.setObjectName("menubar")
        JarvisVirtualAssistent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JarvisVirtualAssistent)
        self.statusbar.setObjectName("statusbar")
        JarvisVirtualAssistent.setStatusBar(self.statusbar)

        self.retranslateUi(JarvisVirtualAssistent)
        QtCore.QMetaObject.connectSlotsByName(JarvisVirtualAssistent)

    def retranslateUi(self, JarvisVirtualAssistent):
        _translate = QtCore.QCoreApplication.translate
        JarvisVirtualAssistent.setWindowTitle(
            _translate("JarvisVirtualAssistent", "MainWindow"))
        self.pushButton.setText(_translate("JarvisVirtualAssistent", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisVirtualAssistent = QtWidgets.QMainWindow()
    ui = Ui_JarvisVirtualAssistent()
    ui.setupUi(JarvisVirtualAssistent)
    JarvisVirtualAssistent.show()
    sys.exit(app.exec_())
