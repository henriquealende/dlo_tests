# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

import buttons.buttons as bt

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect, QMessageBox, QGraphicsColorizeEffect
from PySide2.QtCore import QFile, QPropertyAnimation, QEasingCurve, QMargins, QTime, QPoint
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QValidator, QDoubleValidator, QColor

class Main_Window(QWidget):
    def __init__(self):
        super(Main_Window, self).__init__()
        loader = QUiLoader()
        file = QFile("form.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        self.oldPos = self.pos()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # GLOBAL BUTTONS
        self.counterTest = 0
        self.ui.nextHomeButton.clicked.connect(lambda: bt.UI_Buttons.nextHome(self))
        
        self.ui.nextRegisterButton.clicked.connect(lambda: bt.UI_Buttons.nextRegister(self))

        self.ui.referenceSoundButtonLow.clicked.connect(lambda: bt.UI_Buttons.playReferenceSound(self, 'Low'))
        self.ui.referenceSoundButtonMid.clicked.connect(lambda: bt.UI_Buttons.playReferenceSound(self, 'Mid'))
        self.ui.referenceSoundButtonHigh.clicked.connect(lambda: bt.UI_Buttons.playReferenceSound(self, 'High'))
        self.ui.readyButton.clicked.connect(lambda: bt.UI_Buttons.startTest(self))
        
        self.ui.testSoundButton.clicked.connect(lambda: bt.UI_Buttons.playTestSound(self))
        self.ui.positiveButton.clicked.connect(lambda: bt.UI_Buttons.positiveAnswer(self))
        self.ui.negativeButton.clicked.connect(lambda: bt.UI_Buttons.negativeAnswer(self))
        self.ui.nextStepButton.clicked.connect(lambda: bt.UI_Buttons.nextStepTest(self))
        self.ui.idUserLine.textChanged.connect(lambda: bt.UI_Buttons.idUserChange(self))
        self.ui.quitButton.clicked.connect(lambda: bt.UI_Buttons.closeApp(self))

        self.ui.closeAllButton.clicked.connect(lambda: bt.UI_Buttons.closeAll(self))
        self.ui.minimizeButton.clicked.connect(lambda: bt.UI_Buttons.minimizeApp(self))

    def ProgressBarValue(self, value):
        # PROGRESSBAR STYLESHEET
        styleSheet = """
        QFrame{
        border-radius:90px;
        background-color: qconicalgradient(cx:0.517, cy:0.488636, angle:90, stop:{STOP_1} rgba(104, 65, 11, 0), stop:{STOP_2} rgba(247, 155, 25, 255));
        }
        """
        htmlText = """
        <html><head/><body><p>{VALUE}<span style=" font-size:26pt; color:#f79b19; vertical-align:sub;">%</span></p></body></html>
        """
        progress = (100-value)/100
        #GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        #SET VALUES TO NEW STYLESHEET
        newStyleSheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        newHtmlText = htmlText.replace("{VALUE}", str(value))
        self.ui.circularProgress.setStyleSheet(newStyleSheet)
        self.ui.percentText.setText(newHtmlText)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

def center_window(widget):
    window = widget.window()
    window.setGeometry(
        QtWidgets.QStyle.alignedRect(
            QtCore.Qt.LeftToRight,
            QtCore.Qt.AlignCenter,
            window.size(),
            QtGui.QGuiApplication.primaryScreen().availableGeometry(),
        ),
    )
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main_Window()
    widget.resize(800,600)
    widget.show()
    QtCore.QTimer.singleShot(0, lambda: center_window(widget))
    sys.exit(app.exec_())

