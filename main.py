#----------------------------------------------------------------------
# FRONT-END
#----------------------------------------------------------------------



# ----------------------------------------
# Importing libraries and modules
# ----------------------------------------

import numpy as np
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QFrame, QLineEdit, QPushButton, QSizePolicy, QStackedWidget, QStatusBar, QWidget
from PySide6.QtCore import QTimer, QCoreApplication, QMetaObject, QRect, Qt 
from PySide6.QtGui import QFont 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.StackedPages = QStackedWidget(self.CentralWidget)
        self.StackedPages.setObjectName(u"StackedPages")
        self.StackedPages.setGeometry(QRect(0, 0, 961, 511))
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.Page1.setStyleSheet(u"background-color: #d9d9d9;")
        self.Page1_Text = QLabel(self.Page1)
        self.Page1_Text.setObjectName(u"Page1_Text")
        self.Page1_Text.setGeometry(QRect(70, 130, 691, 251))
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setBold(False)
        self.Page1_Text.setFont(font)
        self.Page1_Text.setStyleSheet(u"background-color: transparent;")
        self.Page1_Text.setTextFormat(Qt.AutoText)
        self.Page1_Button_GetStarted = QPushButton(self.Page1)
        self.Page1_Button_GetStarted.setObjectName(u"Page1_Button_GetStarted")
        self.Page1_Button_GetStarted.setGeometry(QRect(710, 370, 141, 61))
        font1 = QFont()
        font1.setFamilies([u"Helvetica"])
        font1.setWeight(QFont.Black)
        self.Page1_Button_GetStarted.setFont(font1)
        self.Page1_Button_GetStarted.setStyleSheet(u"background-color: #f5f5f5; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #555555; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: 900;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 15px;")
        self.StackedPages.addWidget(self.Page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        font2 = QFont()
        font2.setFamilies([u"Helvetica"])
        self.Page2.setFont(font2)
        self.Page2.setStyleSheet(u"background-color: #131313;")
        self.Page2_Input = QLineEdit(self.Page2)
        self.Page2_Input.setObjectName(u"Page2_Input")
        self.Page2_Input.setGeometry(QRect(700, 210, 151, 111))
        self.Page2_Input.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"\n"
"font-family: \"Helvetica\"; /* Specify the font family */\n"
"font-size: 60pt; /* Specify the font size */\n"
"font-weight: 100; /* Specify the font weight */\n"
"\n"
"color: #ffffff; /* Specify the text color */\n"
"background-color: #262626; /* Specify the background color */\n"
"border: none; /* Specify the border */\n"
"border-radius: 0px; /* Specify border-radius for rounded corners */\n"
"outline: none; /* Remove the focus outline */")
        self.Page2_Text = QLabel(self.Page2)
        self.Page2_Text.setObjectName(u"Page2_Text")
        self.Page2_Text.setGeometry(QRect(90, 170, 521, 191))
        self.Page2_Text.setStyleSheet(u"background-color: transparent;")
        self.Page2_Button_Next = QPushButton(self.Page2)
        self.Page2_Button_Next.setObjectName(u"Page2_Button_Next")
        self.Page2_Button_Next.setGeometry(QRect(780, 450, 71, 31))
        self.Page2_Button_Next.setStyleSheet(u"background-color: #f5f5f5; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #131313; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 9px;")
        self.Page2_Button_Back = QPushButton(self.Page2)
        self.Page2_Button_Back.setObjectName(u"Page2_Button_Back")
        self.Page2_Button_Back.setGeometry(QRect(700, 450, 71, 31))
        self.Page2_Button_Back.setStyleSheet(u"background-color: #262626; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #f5f5f5; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page2_Button_Home = QPushButton(self.Page2)
        self.Page2_Button_Home.setObjectName(u"Page2_Button_Home")
        self.Page2_Button_Home.setGeometry(QRect(620, 450, 71, 31))
        self.Page2_Button_Home.setStyleSheet(u"background-color: #808080; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #131313; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page2_Text_Invalid1 = QLabel(self.Page2)
        self.Page2_Text_Invalid1.setObjectName(u"Page2_Text_Invalid1")
        self.Page2_Text_Invalid1.setGeometry(QRect(90, 390, 521, 21))
        self.Page2_Text_Invalid1.setStyleSheet(u"background-color: transparent;")
        self.Page2_Text_Invalid2 = QLabel(self.Page2)
        self.Page2_Text_Invalid2.setObjectName(u"Page2_Text_Invalid2")
        self.Page2_Text_Invalid2.setGeometry(QRect(90, 390, 521, 21))
        self.Page2_Text_Invalid2.setStyleSheet(u"background-color: transparent;")
        self.StackedPages.addWidget(self.Page2)
        self.Page3 = QWidget()
        self.Page3.setObjectName(u"Page3")
        self.Page3.setStyleSheet(u"background-color: #131313;")
        self.Page3_Button_Next = QPushButton(self.Page3)
        self.Page3_Button_Next.setObjectName(u"Page3_Button_Next")
        self.Page3_Button_Next.setGeometry(QRect(780, 450, 71, 31))
        self.Page3_Button_Next.setStyleSheet(u"background-color: #f5f5f5; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #131313; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 9px;")
        self.Page3_Button_Back = QPushButton(self.Page3)
        self.Page3_Button_Back.setObjectName(u"Page3_Button_Back")
        self.Page3_Button_Back.setGeometry(QRect(700, 450, 71, 31))
        self.Page3_Button_Back.setStyleSheet(u"background-color: #262626; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #f5f5f5; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page3_Input = QLineEdit(self.Page3)
        self.Page3_Input.setObjectName(u"Page3_Input")
        self.Page3_Input.setGeometry(QRect(700, 210, 151, 111))
        self.Page3_Input.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"\n"
"font-family: \"Helvetica\"; /* Specify the font family */\n"
"font-size: 60pt; /* Specify the font size */\n"
"font-weight: 100; /* Specify the font weight */\n"
"\n"
"color: #ffffff; /* Specify the text color */\n"
"background-color: #262626; /* Specify the background color */\n"
"border: none; /* Specify the border */\n"
"border-radius: 0px; /* Specify border-radius for rounded corners */\n"
"outline: none; /* Remove the focus outline */")
        self.Page3_Button_Home = QPushButton(self.Page3)
        self.Page3_Button_Home.setObjectName(u"Page3_Button_Home")
        self.Page3_Button_Home.setGeometry(QRect(620, 450, 71, 31))
        self.Page3_Button_Home.setStyleSheet(u"background-color: #808080; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #131313; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page3_Text = QLabel(self.Page3)
        self.Page3_Text.setObjectName(u"Page3_Text")
        self.Page3_Text.setGeometry(QRect(90, 170, 521, 191))
        self.Page3_Text.setStyleSheet(u"background-color: transparent;")
        self.Page3_Text_Invalid2 = QLabel(self.Page3)
        self.Page3_Text_Invalid2.setObjectName(u"Page3_Text_Invalid2")
        self.Page3_Text_Invalid2.setGeometry(QRect(90, 390, 521, 21))
        self.Page3_Text_Invalid2.setStyleSheet(u"background-color: transparent;")
        self.Page3_Text_Invalid1 = QLabel(self.Page3)
        self.Page3_Text_Invalid1.setObjectName(u"Page3_Text_Invalid1")
        self.Page3_Text_Invalid1.setGeometry(QRect(90, 390, 521, 21))
        self.Page3_Text_Invalid1.setStyleSheet(u"background-color: transparent;")
        self.StackedPages.addWidget(self.Page3)
        self.Page4 = QWidget()
        self.Page4.setObjectName(u"Page4")
        self.Page4.setStyleSheet(u"background-color: #131313;")
        self.Page4_Text = QLabel(self.Page4)
        self.Page4_Text.setObjectName(u"Page4_Text")
        self.Page4_Text.setGeometry(QRect(90, 170, 521, 191))
        self.Page4_Text.setStyleSheet(u"background-color: transparent;")
        self.Page4_Button_Next = QPushButton(self.Page4)
        self.Page4_Button_Next.setObjectName(u"Page4_Button_Next")
        self.Page4_Button_Next.setGeometry(QRect(780, 450, 71, 31))
        self.Page4_Button_Next.setStyleSheet(u"background-color: #f5f5f5; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #131313; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 9px;")
        self.Page4_Button_Home = QPushButton(self.Page4)
        self.Page4_Button_Home.setObjectName(u"Page4_Button_Home")
        self.Page4_Button_Home.setGeometry(QRect(620, 450, 71, 31))
        self.Page4_Button_Home.setStyleSheet(u"background-color: #808080; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #131313; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page4_Input = QLineEdit(self.Page4)
        self.Page4_Input.setObjectName(u"Page4_Input")
        self.Page4_Input.setGeometry(QRect(700, 210, 151, 111))
        self.Page4_Input.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"\n"
"font-family: \"Helvetica\"; /* Specify the font family */\n"
"font-size: 60pt; /* Specify the font size */\n"
"font-weight: 100; /* Specify the font weight */\n"
"\n"
"color: #ffffff; /* Specify the text color */\n"
"background-color: #262626; /* Specify the background color */\n"
"border: none; /* Specify the border */\n"
"border-radius: 0px; /* Specify border-radius for rounded corners */\n"
"outline: none; /* Remove the focus outline */")
        self.Page4_Button_Back = QPushButton(self.Page4)
        self.Page4_Button_Back.setObjectName(u"Page4_Button_Back")
        self.Page4_Button_Back.setGeometry(QRect(700, 450, 71, 31))
        self.Page4_Button_Back.setStyleSheet(u"background-color: #262626; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #f5f5f5; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page4_Text_Invalid2 = QLabel(self.Page4)
        self.Page4_Text_Invalid2.setObjectName(u"Page4_Text_Invalid2")
        self.Page4_Text_Invalid2.setGeometry(QRect(90, 390, 521, 21))
        self.Page4_Text_Invalid2.setStyleSheet(u"background-color: transparent;")
        self.Page4_Text_Invalid1 = QLabel(self.Page4)
        self.Page4_Text_Invalid1.setObjectName(u"Page4_Text_Invalid1")
        self.Page4_Text_Invalid1.setGeometry(QRect(90, 390, 521, 21))
        self.Page4_Text_Invalid1.setStyleSheet(u"background-color: transparent;")
        self.StackedPages.addWidget(self.Page4)
        self.Page5 = QWidget()
        self.Page5.setObjectName(u"Page5")
        self.Page5.setStyleSheet(u"background-color: #131313;")
        self.Page5_Text = QLabel(self.Page5)
        self.Page5_Text.setObjectName(u"Page5_Text")
        self.Page5_Text.setGeometry(QRect(90, 170, 521, 191))
        self.Page5_Text.setStyleSheet(u"background-color: transparent;")
        self.Page5_Button_Next = QPushButton(self.Page5)
        self.Page5_Button_Next.setObjectName(u"Page5_Button_Next")
        self.Page5_Button_Next.setGeometry(QRect(780, 450, 71, 31))
        self.Page5_Button_Next.setStyleSheet(u"background-color: #f5f5f5; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #131313; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 9px;")
        self.Page5_Button_Home = QPushButton(self.Page5)
        self.Page5_Button_Home.setObjectName(u"Page5_Button_Home")
        self.Page5_Button_Home.setGeometry(QRect(620, 450, 71, 31))
        self.Page5_Button_Home.setStyleSheet(u"background-color: #808080; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #131313; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page5_Input = QLineEdit(self.Page5)
        self.Page5_Input.setObjectName(u"Page5_Input")
        self.Page5_Input.setGeometry(QRect(700, 210, 151, 111))
        self.Page5_Input.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"\n"
"font-family: \"Helvetica\"; /* Specify the font family */\n"
"font-size: 60pt; /* Specify the font size */\n"
"font-weight: 100; /* Specify the font weight */\n"
"\n"
"color: #ffffff; /* Specify the text color */\n"
"background-color: #262626; /* Specify the background color */\n"
"border: none; /* Specify the border */\n"
"border-radius: 0px; /* Specify border-radius for rounded corners */\n"
"outline: none; /* Remove the focus outline */")
        self.Page5_Button_Back = QPushButton(self.Page5)
        self.Page5_Button_Back.setObjectName(u"Page5_Button_Back")
        self.Page5_Button_Back.setGeometry(QRect(700, 450, 71, 31))
        self.Page5_Button_Back.setStyleSheet(u"background-color: #262626; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #f5f5f5; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page5_Text_Invalid2 = QLabel(self.Page5)
        self.Page5_Text_Invalid2.setObjectName(u"Page5_Text_Invalid2")
        self.Page5_Text_Invalid2.setGeometry(QRect(90, 390, 521, 21))
        self.Page5_Text_Invalid2.setStyleSheet(u"background-color: transparent;")
        self.Page5_Text_Invalid1 = QLabel(self.Page5)
        self.Page5_Text_Invalid1.setObjectName(u"Page5_Text_Invalid1")
        self.Page5_Text_Invalid1.setGeometry(QRect(90, 390, 521, 21))
        self.Page5_Text_Invalid1.setStyleSheet(u"background-color: transparent;")
        self.StackedPages.addWidget(self.Page5)
        self.Page6 = QWidget()
        self.Page6.setObjectName(u"Page6")
        self.Page6.setStyleSheet(u"background-color: #131313;")
        self.Page6_Text = QLabel(self.Page6)
        self.Page6_Text.setObjectName(u"Page6_Text")
        self.Page6_Text.setGeometry(QRect(90, 230, 771, 51))
        self.Page6_Text.setStyleSheet(u"background-color: transparent;")
        self.Page6_Button_Back = QPushButton(self.Page6)
        self.Page6_Button_Back.setObjectName(u"Page6_Button_Back")
        self.Page6_Button_Back.setGeometry(QRect(780, 450, 71, 31))
        self.Page6_Button_Back.setStyleSheet(u"background-color: #262626; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #f5f5f5; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page6_Button_Home = QPushButton(self.Page6)
        self.Page6_Button_Home.setObjectName(u"Page6_Button_Home")
        self.Page6_Button_Home.setGeometry(QRect(700, 450, 71, 31))
        self.Page6_Button_Home.setStyleSheet(u"background-color: #808080; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #131313; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page6_Button_SH = QPushButton(self.Page6)
        self.Page6_Button_SH.setObjectName(u"Page6_Button_SH")
        self.Page6_Button_SH.setGeometry(QRect(370, 290, 190, 190))
        self.Page6_Button_SH.setStyleSheet(u"background-color: #262626; /* Background color */\n"
"border: none; /* Remove border */\n"
"border-radius: 95;\n"
"color: #808080; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"text-align: center; /* Center the text */\n"
"font-size: 32px;")
        self.Page6_Button_NH = QPushButton(self.Page6)
        self.Page6_Button_NH.setObjectName(u"Page6_Button_NH")
        self.Page6_Button_NH.setGeometry(QRect(370, 30, 190, 190))
        self.Page6_Button_NH.setStyleSheet(u"background-color: #262626; /* Background color */\n"
"border: none; /* Remove border */\n"
"border-radius: 95;\n"
"color: #808080; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"text-align: center; /* Center the text */\n"
"font-size: 32px;")
        self.StackedPages.addWidget(self.Page6)
        self.Page7 = QWidget()
        self.Page7.setObjectName(u"Page7")
        self.Page7.setStyleSheet(u"background-color: #d9d9d9;")
        self.Page6_Text_2 = QLabel(self.Page7)
        self.Page6_Text_2.setObjectName(u"Page6_Text_2")
        self.Page6_Text_2.setGeometry(QRect(90, 210, 771, 91))
        self.Page6_Text_2.setStyleSheet(u"background-color: transparent;")
        self.StackedPages.addWidget(self.Page7)
        self.Page8 = QWidget()
        self.Page8.setObjectName(u"Page8")
        self.Page8.setStyleSheet(u"background-color: #131313;")
        self.Page8_Button_Home = QPushButton(self.Page8)
        self.Page8_Button_Home.setObjectName(u"Page8_Button_Home")
        self.Page8_Button_Home.setGeometry(QRect(780, 450, 71, 31))
        self.Page8_Button_Home.setStyleSheet(u"background-color: #808080; /* Background color */\n"
"border: none; /* Remove border */\n"
"color: #131313; /* Text color */\n"
"font-family: \"Helvetica\";\n"
"font-weight: bold;\n"
"text-align: center; /* Center the text */\n"
"font-size: 18px;\n"
"border-radius: 10px;")
        self.Page8_Text = QLabel(self.Page8)
        self.Page8_Text.setObjectName(u"Page8_Text")
        self.Page8_Text.setGeometry(QRect(50, 60, 251, 51))
        self.Page8_Text.setStyleSheet(u"background-color: transparent;")
        self.Page8_Frame = QFrame(self.Page8)
        self.Page8_Frame.setObjectName(u"Page8_Frame")
        self.Page8_Frame.setGeometry(QRect(50, 110, 861, 331))
        self.Page8_Frame.setStyleSheet(u"background: transparent;")
        self.Page8_Frame.setFrameShape(QFrame.StyledPanel)
        self.Page8_Frame.setFrameShadow(QFrame.Raised)
        self.StackedPages.addWidget(self.Page8)

        MainWindow.setCentralWidget(self.CentralWidget)
        self.StatusBar = QStatusBar(MainWindow)
        self.StatusBar.setObjectName(u"StatusBar")
        MainWindow.setStatusBar(self.StatusBar)

        self.retranslateUi(MainWindow)

        self.StackedPages.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)
    
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tropical Cyclone Trajectory Mapping Simulation", None))
#if QT_CONFIG(tooltip)
        self.Page1_Text.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Page1_Text.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:75pt; font-weight:900; color:#555555;\">Tropical Cyclone</span></p>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:900; color:#555555;\">Trajectory Mapping</span></p>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:900; color:#555555;\">Simulation</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page1_Button_GetStarted.setText(QCoreApplication.translate("MainWindow", u"Get Started", None))
        self.Page2_Input.setText("")
        self.Page2_Text.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#ffffff;\">What was the speed</span></p>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#ffffff;\">of the Tropical Cyclone</span></p>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#89b7af;\">18 hours ago?</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page2_Button_Next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.Page2_Button_Back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.Page2_Button_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Page2_Text_Invalid1.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:20pt; font-weight:100; color:#c73030;\">Speed value should only be within 30kph-220kph.</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page2_Text_Invalid2.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:20pt; font-weight:100; color:#c73030;\">Invalid input. Please enter a valid number.</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page3_Button_Next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.Page3_Button_Back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.Page3_Input.setText("")
        self.Page3_Button_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Page3_Text.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#ffffff;\">What was the speed</span></p>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#ffffff;\">of the Tropical Cyclone</span></p>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#b0e67f;\">12 hours ago?</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page3_Text_Invalid2.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:20pt; font-weight:100; color:#c73030;\">Invalid input. Please enter a valid number.</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page3_Text_Invalid1.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:20pt; font-weight:100; color:#c73030;\">Speed value should only be within 30kph-220kph.</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page4_Text.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#ffffff;\">What was the speed</span></p>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#ffffff;\">of the Tropical Cyclone</span></p>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#c28edd;\">6 hours ago?</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page4_Button_Next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.Page4_Button_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Page4_Input.setText("")
        self.Page4_Button_Back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.Page4_Text_Invalid2.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:20pt; font-weight:100; color:#c73030;\">Invalid input. Please enter a valid number.</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page4_Text_Invalid1.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:20pt; font-weight:100; color:#c73030;\">Speed value should only be within 30kph-220kph.</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page5_Text.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#ffffff;\">What is the speed</span></p>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#ffffff;\">of the Tropical Cyclone</span></p>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:50pt; font-weight:100; color:#ced261;\">now?</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page5_Button_Next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.Page5_Button_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Page5_Input.setText("")
        self.Page5_Button_Back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.Page5_Text_Invalid2.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:20pt; font-weight:100; color:#c73030;\">Invalid input. Please enter a valid number.</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page5_Text_Invalid1.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin-bottom: 0px;\"><span style=\"font-family: 'Helvetica'; font-size:20pt; font-weight:100; color:#c73030;\">Speed value should only be within 30kph-220kph.</span></p>\n"
"    </body>\n"
"</html>\n"
"", None))
        self.Page6_Text.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin: 0; text-align: center;\">\n"
"            <span style=\"font-family: 'Helvetica'; font-size: 45pt; font-weight: 100; color: #ffffff;\">Where is the tropical cyclone located?</span>\n"
"        </p>\n"
"    </body>\n"
"</html>", None))
        self.Page6_Button_Back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.Page6_Button_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        
        
        self.Page6_Button_SH.setText(QCoreApplication.translate("MainWindow", u"Southern\nHemisphere", None))
        self.Page6_Button_NH.setText(QCoreApplication.translate("MainWindow", u"Northern\nHemisphere", None))
        
        
        self.Page6_Text_2.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin: 7; text-align: center;\"> <span style=\"font-family: 'Helvetica'; font-size: 25pt; font-weight: 100; color: #555555;\">Generating the forecast...</span></p>\n"
"        <p style=\"margin: 7; text-align: center;\"> <span style=\"font-family: 'Helvetica'; font-size: 25pt; font-weight: 100; color: #555555;\">Please wait.</span></p>\n"
"    </body>\n"
"</html>", None))
        self.Page8_Button_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Page8_Text.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"    <head/>\n"
"    <body>\n"
"        <p style=\"margin: 0;\">\n"
"            <span style=\"font-family: 'Helvetica'; font-size: 42pt; font-weight: 900; color: #f5f5f5;\">Forecast:</span>\n"
"        </p>\n"
"    </body>\n"
"</html>", None))



#----------------------------------------------------------------------
# BACK-END
#----------------------------------------------------------------------



# ----------------------------------------
# Defining functions
# ----------------------------------------

def DividedDifferencePart1(F2, F1, X2, X1):
    R = (F2 - F1) / (X2 - X1)
    return R

def DividedDifferencePart2(A, B, C, D, X, X1, X2, X3):
    R = ( A ) + ( B * (X-X1) ) + ( C * (X-X1) * (X-X2) ) + ( D * (X-X1) * (X-X2) * (X-X3) )
    print(A, B, C, D, X, X1, X2, X3, R)
    return R

# ----------------------------------------
# Main class
# ----------------------------------------

class MyApplication(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        
        # Setting a fixed size for the main window
        self.setFixedSize(960, 540)

        # Initializing the matrix
        self.initializeMatrix()

        # Initializing a boolean variable to choose hemispheres
        self.Northern_Hemisphere = True

        # Creating a Matplotlib widget
        self.create_matplotlib_widget()

        # Connecting buttons to functions
        self.Page1_Button_GetStarted.clicked.connect(self.showPage2)
        self.Page1_Button_GetStarted.enterEvent = lambda event: self.handleButtonHover(True)
        self.Page1_Button_GetStarted.leaveEvent = lambda event: self.handleButtonHover(False)
        self.Page2_Button_Next.clicked.connect(self.processPage2)
        self.Page2_Button_Back.clicked.connect(self.showPage1)
        self.Page2_Button_Home.clicked.connect(self.showPage1)
        self.Page3_Button_Next.clicked.connect(self.processPage3)
        self.Page3_Button_Back.clicked.connect(self.showPage2)
        self.Page3_Button_Home.clicked.connect(self.showPage1)
        self.Page4_Button_Next.clicked.connect(self.processPage4)
        self.Page4_Button_Back.clicked.connect(self.showPage3)
        self.Page4_Button_Home.clicked.connect(self.showPage1)
        self.Page5_Button_Next.clicked.connect(self.processPage5)
        self.Page5_Button_Back.clicked.connect(self.showPage4)
        self.Page5_Button_Home.clicked.connect(self.showPage1)
        self.Page6_Button_NH.clicked.connect(self.Use_Northern_Hemisphere)
        self.Page6_Button_NH.enterEvent = lambda event: self.handleButtonHover(True)
        self.Page6_Button_NH.leaveEvent = lambda event: self.handleButtonHover(False)
        self.Page6_Button_SH.clicked.connect(self.Use_Southern_Hemisphere)
        self.Page6_Button_SH.enterEvent = lambda event: self.handleButtonHover2(True)
        self.Page6_Button_SH.leaveEvent = lambda event: self.handleButtonHover2(False)
        self.Page6_Button_Back.clicked.connect(self.showPage5)
        self.Page6_Button_Home.clicked.connect(self.showPage1)
        self.Page8_Button_Home.clicked.connect(self.showPage1)

        # Hiding the QLabel widgets initially
        self.Page2_Text_Invalid1.hide()
        self.Page2_Text_Invalid2.hide()
        self.Page3_Text_Invalid1.hide()
        self.Page3_Text_Invalid2.hide()
        self.Page4_Text_Invalid1.hide()
        self.Page4_Text_Invalid2.hide()
        self.Page5_Text_Invalid1.hide()
        self.Page5_Text_Invalid2.hide()

        # Initializing Page Index
        self.currentPage = 0

        # Showing Page 1 initially
        self.showPage1()

        # Creating a subplot on the Matplotlib figure
        self.ax = self.figure.add_subplot(111)

        # Connecting the event handler to the motion_notify_event
        self.canvas.mpl_connect('motion_notify_event', self.update_coords)

        # Creating a QLabel for displaying coordinates
        self.coord_label = QLabel(self)
        self.coord_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.coord_label.hide()
    
    # ----------------------------------------
    # Making animations for mouse cursor hovers
    # ----------------------------------------

    def handleButtonHover(self, is_hovered):
        if is_hovered:
            self.Page1.setStyleSheet(u"background-color: #131313;")
            self.Page1_Button_GetStarted.setStyleSheet(u"background-color: #262626; /* Background color */\n"
                "border: none; /* Remove border */\n"
                "color: #f5f5f5; /* Text color */\n"
                "font-family: \"Helvetica\";\n"
                "font-weight: 900;\n"
                "text-align: center; /* Center the text */\n"
                "font-size: 18px;\n"
                "border-radius: 15px;")
            self.Page6_Button_NH.setStyleSheet(u"background-color: #f5f5f5; /* Background color */\n"
                "border: none; /* Remove border */\n"
                "border-radius: 95;\n"
                "color: #131313; /* Text color */\n"
                "font-family: \"Helvetica\";\n"
                "text-align: center; /* Center the text */\n"
                "font-size: 32px;")
        else:
            self.Page1.setStyleSheet(u"background-color: #d9d9d9;")
            self.Page1_Button_GetStarted.setStyleSheet(u"background-color: #f5f5f5; /* Background color */\n"
                "border: none; /* Remove border */\n"
                "color: #555555; /* Text color */\n"
                "font-family: \"Helvetica\";\n"
                "font-weight: 900;\n"
                "text-align: center; /* Center the text */\n"
                "font-size: 18px;\n"
                "border-radius: 15px;")
            self.Page6_Button_NH.setStyleSheet(u"background-color: #262626; /* Background color */\n"
                "border: none; /* Remove border */\n"
                "border-radius: 95;\n"
                "color: #808080; /* Text color */\n"
                "font-family: \"Helvetica\";\n"
                "text-align: center; /* Center the text */\n"
                "font-size: 32px;")

    def handleButtonHover2(self, is_hovered):
        if is_hovered:
            self.Page6_Button_SH.setStyleSheet(u"background-color: #f5f5f5; /* Background color */\n"
                "border: none; /* Remove border */\n"
                "border-radius: 95;\n"
                "color: #131313; /* Text color */\n"
                "font-family: \"Helvetica\";\n"
                "text-align: center; /* Center the text */\n"
                "font-size: 32px;")           
        else:
            self.Page6_Button_SH.setStyleSheet(u"background-color: #262626; /* Background color */\n"
                "border: none; /* Remove border */\n"
                "border-radius: 95;\n"
                "color: #808080; /* Text color */\n"
                "font-family: \"Helvetica\";\n"
                "text-align: center; /* Center the text */\n"
                "font-size: 32px;")

    # ----------------------------------------
    # Making the graph
    # ----------------------------------------

    def create_matplotlib_widget(self):
        
        self.figure, self.canvas = self.create_matplotlib_canvas()

        # Creating a layout for Page8_Frame
        layout = QVBoxLayout(self.Page8_Frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
    
    def create_matplotlib_canvas(self):
        
        # Creating a Matplotlib figure
        figure = Figure()

        # Creating a Matplotlib canvas
        canvas = FigureCanvas(figure)

        return figure, canvas
    
    def show_graph(self):

        self.figure.clear()

        # Getting x and y coordinates from self.matrix
        if self.Northern_Hemisphere:
            x_coordinates = self.matrix[:-1, 4]
            y_coordinates = self.matrix[:-1, 5]
        else:
            x_coordinates = self.matrix[:-1, 3]
            y_coordinates = self.matrix[:-1, 5]

        # Creating a subplot on the Matplotlib figure
        ax = self.figure.add_subplot(111)

        # Creating an array of exponentially increasing background marker sizes
        exponential_sizes = np.exp(np.linspace(0, 3.5, len(x_coordinates)))

        # Scaling the exponential sizes
        min_size = 10
        max_size = 250
        markerSizes = min_size + (max_size - min_size) * (exponential_sizes / exponential_sizes.max())
        
        # Adding a text label beside a foreground marker
        offset = 50
        font_size = 8
        font_family = 'Helvetica'
        ax.text(x_coordinates[2] + offset, y_coordinates[2] + offset, '15 hours ago', color='#b8cd07', fontsize=font_size, fontname=font_family, ha='left', va='top', zorder=4, transform=ax.transData)
        ax.text(x_coordinates[5] + offset, y_coordinates[5] + offset, '6 hours ago', color='#b8cd07', fontsize=font_size, fontname=font_family, ha='left', va='top', zorder=4, transform=ax.transData)
        ax.text(x_coordinates[7] + offset, y_coordinates[7] + offset, 'Now', color='#b8cd07', fontsize=font_size, fontname=font_family, ha='left', va='top', zorder=4, transform=ax.transData)
        if self.matrix[9,2] != 0:
            ax.text(x_coordinates[9] + offset, y_coordinates[9] + offset, '6 hours later', color='#b8cd07', fontsize=font_size, fontname=font_family, ha='left', va='top', zorder=4, transform=ax.transData)
            if self.matrix[11,2] != 0:
                ax.text(x_coordinates[11] + offset, y_coordinates[11] + offset, '12 hours later', color='#b8cd07', fontsize=font_size, fontname=font_family, ha='left', va='top', zorder=4, transform=ax.transData)
                if self.matrix[13,2] != 0:
                    ax.text(x_coordinates[13] + offset, y_coordinates[13] + offset, '18 hours later', color='#b8cd07', fontsize=font_size, fontname=font_family, ha='left', va='top', zorder=4, transform=ax.transData)
                    if self.matrix[15,2] != 0:
                        ax.text(x_coordinates[15] + offset, y_coordinates[15] + offset, '1 day later', color='#b8cd07', fontsize=font_size, fontname=font_family, ha='left', va='top', zorder=4, transform=ax.transData)

        # Plotting the graph with foreground markers
        ax.plot(x_coordinates, y_coordinates, marker='o', markersize=10, color='#0cb8d1', linestyle='', zorder=3)

        # Plotting the graph with background markers
        for x, y, size in zip(x_coordinates, y_coordinates, markerSizes):
            ax.plot(x, y, marker='o', markersize=size, color='#0cb8d1', alpha=0.1, zorder=2)

        # Connecting the foreground markers with a line
        ax.plot(x_coordinates, y_coordinates, linestyle='-', linewidth=10, color='#092428', zorder=1)

        # Seting axis labels
        ax.set_xlabel('X Axis Label', color='#f5f5f5')
        ax.set_ylabel('Y Axis Label', color='#f5f5f5')

        # Removing the border of the subplot
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # Customizing the background color of the subplot
        ax.set_facecolor('#131313')

        # Setting the facecolor of Page 8
        self.figure.set_facecolor('#131313')

        # Customizing tick color
        ax.tick_params(axis='x', colors='#f5f5f5')
        ax.tick_params(axis='y', colors='#f5f5f5')

        # Setting labels
        ax.set_xlabel('Longitude Distance (km)', color='#f5f5f5', size=12, family='Helvetica')
        ax.set_ylabel('Latitude Distance (km)', color='#f5f5f5', size=12, family='Helvetica')

        # Applying tight layout
        self.figure.tight_layout()

        # Redrawing the canvas
        self.canvas.draw()
    
    # Allowing real-time display of x-axis and y-axis values on where the mouse cursor is hovering
    def update_coords(self, event):
        
        if event.inaxes:
            x_coord, y_coord = event.xdata, event.ydata
            x_coord_str = f'X: {x_coord:.2f} km far from origin.'
            y_coord_str = f'Y: {y_coord:.2f} km far from origin.'

            # Updating QLabel text and position
            self.coord_label.setText(f'{x_coord_str}\n{y_coord_str}')

            # Setting font and color
            font = QFont('Helvetica', 10)
            font.setBold(True)
            self.coord_label.setFont(font)

            self.coord_label.setStyleSheet('color: #07cd80')

            self.coord_label.adjustSize()

            # Showing the QLabel next to the mouse cursor
            cursor_pos = self.mapFromGlobal(self.cursor().pos())
            self.coord_label.move(cursor_pos.x() + 10, cursor_pos.y() - 20)
            self.coord_label.show()
        
        else:
            self.coord_label.hide()

    def initializeMatrix(self):
        
        # Making matrix
        self.matrix = np.zeros((18, 6), dtype=float)

        # Initializing time values
        X = 0
        for i in range(17):
            self.matrix[i, 0] = X
            X += 3

        # Initializing the starting point of the positive longitude
        self.matrix[0, 3] = 0

    # ----------------------------------------
    # Showing the pages
    # ----------------------------------------

    def showPage1(self):
        self.Page1.setStyleSheet(u"background-color: #d9d9d9;")
        self.Page1_Button_GetStarted.setStyleSheet(u"background-color: #f5f5f5; /* Background color */\n"
            "border: none; /* Remove border */\n"
            "color: #555555; /* Text color */\n"
            "font-family: \"Helvetica\";\n"
            "font-weight: 900;\n"
            "text-align: center; /* Center the text */\n"
            "font-size: 18px;\n"
            "border-radius: 15px;")
        self.StackedPages.setCurrentWidget(self.Page1)
        self.currentPage = 0

    def showPage2(self):
        self.U = 1
        self.StackedPages.setCurrentWidget(self.Page2)
        self.currentPage = 1

    def showPage3(self):
        self.U = 3
        self.StackedPages.setCurrentWidget(self.Page3)
        self.currentPage = 2

    def showPage4(self):
        self.U = 5
        self.StackedPages.setCurrentWidget(self.Page4)
        self.currentPage = 3

    def showPage5(self):
        self.U = 7
        self.StackedPages.setCurrentWidget(self.Page5)
        self.currentPage = 4

    def showPage6(self):
        self.Page6_Button_NH.setStyleSheet(u"background-color: #262626; /* Background color */\n"
            "border: none; /* Remove border */\n"
            "border-radius: 95;\n"
            "color: #808080; /* Text color */\n"
            "font-family: \"Helvetica\";\n"
            "text-align: center; /* Center the text */\n"
            "font-size: 32px;")
        self.Page6_Button_SH.setStyleSheet(u"background-color: #262626; /* Background color */\n"
            "border: none; /* Remove border */\n"
            "border-radius: 95;\n"
            "color: #808080; /* Text color */\n"
            "font-family: \"Helvetica\";\n"
            "text-align: center; /* Center the text */\n"
            "font-size: 32px;")
        self.StackedPages.setCurrentWidget(self.Page6)
        self.currentPage = 5

    def showPage7(self):
        self.StackedPages.setCurrentWidget(self.Page7)
        self.currentPage = 6

        # ----------------------------------------------------------------------
        # Executing Approximation Techniques (Divided Difference Method)
        # ----------------------------------------------------------------------

        F2 = self.matrix[3,1]
        F1 = self.matrix[1,1]
        X2 = self.matrix[3,0]
        X1 = self.matrix[1,0]
        A = F1
        R1 = DividedDifferencePart1(F2, F1, X2, X1)

        F2 = self.matrix[5,1]
        F1 = self.matrix[3,1]
        X2 = self.matrix[5,0]
        X1 = self.matrix[3,0]
        R2 = DividedDifferencePart1(F2, F1, X2, X1)

        F2 = self.matrix[5,1]
        F1 = self.matrix[3,1]
        X2 = self.matrix[5,0]
        X1 = self.matrix[3,0]
        R2 = DividedDifferencePart1(F2, F1, X2, X1)

        F2 = self.matrix[7,1]
        F1 = self.matrix[5,1]
        X2 = self.matrix[7,0]
        X1 = self.matrix[5,0]
        R3 = DividedDifferencePart1(F2, F1, X2, X1)
        B = R1

        F2 = R2
        F1 = R1
        X2 = X1
        X1 = self.matrix[1,0]
        R4 = DividedDifferencePart1(F2, F1, X2, X1)

        F2 = R3
        F1 = R2
        X2 = self.matrix[7,0]
        X1 = self.matrix[3,0]
        R5 = DividedDifferencePart1(F2, F1, X2, X1)
        C = R4

        F2 = R5
        F1 = R4
        X1 = self.matrix[1,0]
        R6 = DividedDifferencePart1(F2, F1, X2, X1)
        D = R6

        X1 = self.matrix[1,0]
        X2 = self.matrix[3,0]
        X3 = self.matrix[5,0]

        U, V, W = 0, 0, 0
        for i in range(5):
            X = self.matrix[U,V]
            ForTimeX = f"ForTime{W}"
            globals()[ForTimeX] = DividedDifferencePart2(A, B, C, D, X, X1, X2, X3)
            U += 2
            W += 6

        U, V, W = 9, 0, 27
        for i in range(8):
            X = self.matrix[U,V]
            ForTimeX = f"ForTime{W}"
            globals()[ForTimeX] = DividedDifferencePart2(A, B, C, D, X, X1, X2, X3)
            U += 1
            W += 3   

        # Putting Interpolation and Extrapolation results in the matrix
        U, V, W = 0, 1, 0
        for i in range(5):
            ForTimeX = f"ForTime{W}"
            self.matrix[U,V] = globals()[ForTimeX]
            U += 2
            W += 6
        U, V, W = 9, 1, 27
        for i in range(8):
            ForTimeX = f"ForTime{W}"
            self.matrix[U,V] = globals()[ForTimeX]
            U += 1
            W += 3

        # Solving the distance values
        for i in range(17):
            self.matrix[i,2] = 3 * self.matrix[i,1]
            if self.matrix[i,2] < 0:
                self.matrix[i,2] = 0

        # Solving the positive longitude values
        for i in range(16):
            self.matrix[i+1,3] = self.matrix[i,3] + self.matrix[i+1, 2]
            self.matrix[17,3] = self.matrix[16,3] + self.matrix[16,3]

        # Solving the negative longitude values
        for i in range(17):
            self.matrix[i,4] = (-1) * self.matrix[i,3]
            self.matrix[17,4] = self.matrix[16,4] + self.matrix[16,4]

        # Solving the latitude values
        for i in range(17):
            self.matrix[i,5] = math.sqrt(self.matrix[i,3]) * 100
            self.matrix[17,5] = self.matrix[16,5] + self.matrix[16,5]

        # Printing the matrix in terminal just to test that data is stored
        np.set_printoptions(precision = 2, suppress = True)
        print(self.matrix)

    def showPage8(self):
        if self.timer is not None:
            self.timer.stop()
            self.timer.deleteLater()
            self.timer = None
        self.StackedPages.setCurrentWidget(self.Page8)
        self.currentPage = 7
        self.show_graph()

    # ----------------------------------------
    # Defining processes
    # ----------------------------------------

    def processPage2(self):
        userInputText = self.Page2_Input.text()

        try:
            userInput = float(userInputText)
            if 30 <= userInput <= 220:
                
                # Storing the data in matrix
                self.matrix[self.U, 1] = userInput
                
                # Moving to Page 3
                self.showPage3()
                
                # Printing the matrix in terminal just to test that data is stored
                print(self.matrix)
      
            else:
                # Showing an error message
                self.Page2_Text_Invalid1.show()
                self.Page2_Text_Invalid2.hide()
        
        except ValueError:
            # Showing an error message
            self.Page2_Text_Invalid1.hide()
            self.Page2_Text_Invalid2.show()

    def processPage3(self):
        userInputText = self.Page3_Input.text()

        try:
            userInput = float(userInputText)
            if 30 <= userInput <= 220:
                
                # Storing the data in matrix
                self.matrix[self.U, 1] = userInput
                
                # Moving to Page 4
                self.showPage4()
                
                # Printing the matrix in terminal just to test that data is stored
                print(self.matrix)

            else:
                
                # Showing an error message
                self.Page3_Text_Invalid1.show()
                self.Page3_Text_Invalid2.hide()

        except ValueError:
            # Showing an error message
            self.Page3_Text_Invalid1.hide()
            self.Page3_Text_Invalid2.show()

    def processPage4(self):
        userInputText = self.Page4_Input.text()

        try:
            userInput = float(userInputText)
            if 30 <= userInput <= 220:
                
                # Storing the data in matrix
                self.matrix[self.U, 1] = userInput
                
                # Moving to Page 5
                self.showPage5()
                
                # Printing the matrix in terminal just to test that data is stored
                print(self.matrix)

            else:
                
                # Showing an error message
                self.Page4_Text_Invalid1.show()
                self.Page4_Text_Invalid2.hide()
        
        except ValueError:
            
            # Showing an error message
            self.Page4_Text_Invalid1.hide()
            self.Page4_Text_Invalid2.show()

    def processPage5(self):
        
        userInputText = self.Page5_Input.text()

        try:
            userInput = float(userInputText)
            if 30 <= userInput <= 220:
                
                # Storing the data in matrix
                self.matrix[self.U, 1] = userInput
                
                # Moving to Page 6
                self.showPage6()
                
                # Printing the matrix in terminal just to test that data is stored
                print(self.matrix)

            else:
                
                # Showing an error message
                self.Page5_Text_Invalid1.show()
                self.Page5_Text_Invalid2.hide()
        
        except ValueError:
            
            # Showing an error message
            self.Page5_Text_Invalid1.hide()
            self.Page5_Text_Invalid2.show()

    # ----------------------------------------
    # Selecting which hemisphere the user chose
    # ----------------------------------------

    def Use_Northern_Hemisphere(self):
        self.Northern_Hemisphere = True
        
        # Moving to Page 7
        self.showPage7()

        # Printing boolean variable in terminal just to test that data is stored
        print(self.Northern_Hemisphere)

        # Setting up a timer to move to Page 8 after 3 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showPage8)
        self.timer.start(3000)  # 3000 milliseconds (3 seconds)

    def Use_Southern_Hemisphere(self):
        self.Northern_Hemisphere = False
        
        # Moving to Page 7
        self.showPage7()

        # Printing boolean variable in terminal just to test that data is stored
        print(self.Northern_Hemisphere)
        
        # Setting up a timer to move to Page 8 after 3 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showPage8)
        self.timer.start(3000)  # 3000 milliseconds (3 seconds)

# ----------------------------------------
# Main function
# ----------------------------------------

def main():
    app = QApplication([])
    window = MyApplication()

    window.show()  # Show the first page initially

    app.exec_()

if __name__ == "__main__":
    main()