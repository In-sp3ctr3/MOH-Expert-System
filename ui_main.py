# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainzEaLFI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QCommandLinkButton, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"# BY: WANDERSON M.PIMENTA\n"
"# PROJECT MADE WITH: Qt Designer and PySide6\n"
"# V: 1.0.0\n"
"#\n"
"# This project can be used freely for all uses, as long as they maintain the\n"
"# respective credits only in the Python scripts, any information in the visual\n"
"# interface (GUI) can be modified without any implication.\n"
"#\n"
"# There are limitations on Qt licenses if you want to use your products\n"
"# commercially, I recommend reading them on the official website:\n"
"# https://doc.qt.io/qtforpython/licenses.html\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: #333;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */"
                        "\n"
"QToolTip {\n"
"	color: #333;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(244, 245, 248);\n"
"	border: 1px solid #CCC;\n"
"    color: #44475a;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(0, 179, 204);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(0, 179, 204);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\""
                        "; color: #f8f8f2; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #bd93f9; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255"
                        ", 255);\n"
"}\n"
"#leftMenuFrame{\n"
"\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #5b6996;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: #f8f8f2;\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#toggleButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: #495474;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png)"
                        ";\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid #6272a4;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(25"
                        "5, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(0, 179, 204);\n"
"}\n"
"#contentBottom{\n"
"\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #bd93f9; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #ff79c6; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #495474; }\n"
"#themeSettingsTopDetail { background-color: rgb(0, 179, 204); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #495474 }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS"
                        " */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    col"
                        "or: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(0, 179, 204);\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(0, 179, 204);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(0, 179, 204);\n"
"	background-color: rgb(0, 179, 204);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(0, 179, 204);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(0, 179, 204);\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"	color: rgb(189, 189, 189);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);"
                        "\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(0, 179, 204);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(0, 179, 204);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:"
                        ":handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background-color: #6272a4;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
""
                        " QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"  "
                        "  border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QCombo"
                        "Box{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	"
                        "background-color: #6272a4;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed"
                        " {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"#pagesContainer QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"    border: 2px solid #ff79c6;\n"
"    color: #ff79c6;\n"
"}\n"
"#pagesContainer QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: #6272a4;\n"
"}\n"
"#pagesContainer QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: #586796;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushB"
                        "utton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2 = QLabel(self.topLogoInfo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 61, 51))
        self.label_2.setStyleSheet(u"background-image: url(:/images/images/images/Logo.png);")
        self.label_2.setPixmap(QPixmap(u":/images/images/images/Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(7)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);\n"
"background-color: rgb(0, 179, 204);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-medical-cross.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-pencil.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(1178, 603))
        self.home.setMaximumSize(QSize(1178, 16777215))
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet(u"")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 20, 811, 121))
        self.frame.setStyleSheet(u"QObject{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(40, 76, 255, 255), stop:1 rgba(11, 156, 255, 255));\n"
"border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_39 = QLabel(self.frame)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(136, 13, 81, 31))
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 400 11pt \"Lato\";\n"
"background-color: none;")
        self.label_40 = QLabel(self.frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(172, 10, 91, 41))
        self.label_40.setStyleSheet(u"font: 800 22pt \"Lato\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_41 = QLabel(self.frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(140, 80, 601, 18))
        self.label_41.setStyleSheet(u"font: 11pt \"Lato\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_42 = QLabel(self.frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(20, 20, 91, 81))
        self.label_42.setStyleSheet(u"background-color: none;")
        self.label_42.setPixmap(QPixmap(u":/images/Convalescent_Care.png"))
        self.label_42.setScaledContents(True)
        self.frame_2 = QFrame(self.home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 194, 811, 231))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.progressBar_mild = QProgressBar(self.frame_2)
        self.progressBar_mild.setObjectName(u"progressBar_mild")
        self.progressBar_mild.setGeometry(QRect(107, 30, 5, 161))
        self.progressBar_mild.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.492611 rgba(87, 227, 137, 255), stop:0.512315 rgba(11, 156, 255, 255));\n"
"}\n"
"\n"
"QProgressBar{\n"
"	background-color: rgb(246, 245, 244);\n"
"}")
        self.progressBar_mild.setValue(50)
        self.progressBar_mild.setTextVisible(False)
        self.progressBar_mild.setOrientation(Qt.Vertical)
        self.label_65 = QLabel(self.frame_2)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(40, 25, 31, 18))
        self.label_65.setStyleSheet(u"color:rgb(192, 191, 188) ;\n"
"")
        self.label_66 = QLabel(self.frame_2)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(40, 104, 31, 18))
        self.label_66.setStyleSheet(u"color:rgb(192, 191, 188) ;\n"
"")
        self.label_67 = QLabel(self.frame_2)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(46, 181, 31, 18))
        self.label_67.setStyleSheet(u"color:rgb(192, 191, 188) ;\n"
"")
        self.label_68 = QLabel(self.frame_2)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(70, 198, 81, 31))
        self.label_68.setFont(font)
        self.label_68.setStyleSheet(u"color: rgb(192, 191, 188);")
        self.label_68.setAlignment(Qt.AlignCenter)
        self.label_68.setWordWrap(True)
        self.progressBar_severe = QProgressBar(self.frame_2)
        self.progressBar_severe.setObjectName(u"progressBar_severe")
        self.progressBar_severe.setGeometry(QRect(220, 30, 5, 161))
        self.progressBar_severe.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.492611 rgb(192, 97, 203), stop:0.512315 rgba(11, 156, 255, 255));\n"
"}\n"
"\n"
"QProgressBar{\n"
"	background-color: rgb(246, 245, 244);\n"
"}")
        self.progressBar_severe.setValue(50)
        self.progressBar_severe.setTextVisible(False)
        self.progressBar_severe.setOrientation(Qt.Vertical)
        self.label_69 = QLabel(self.frame_2)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(183, 198, 81, 31))
        self.label_69.setFont(font)
        self.label_69.setStyleSheet(u"color: rgb(192, 191, 188);")
        self.label_69.setAlignment(Qt.AlignCenter)
        self.label_69.setWordWrap(True)
        self.progressBar_male_positives = QProgressBar(self.frame_2)
        self.progressBar_male_positives.setObjectName(u"progressBar_male_positives")
        self.progressBar_male_positives.setGeometry(QRect(337, 32, 5, 161))
        self.progressBar_male_positives.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.492611 rgb(255, 163, 72), stop:0.512315 rgba(11, 156, 255, 255));\n"
"}\n"
"\n"
"QProgressBar{\n"
"	background-color: rgb(246, 245, 244);\n"
"}")
        self.progressBar_male_positives.setValue(50)
        self.progressBar_male_positives.setTextVisible(False)
        self.progressBar_male_positives.setOrientation(Qt.Vertical)
        self.label_70 = QLabel(self.frame_2)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(300, 200, 81, 31))
        self.label_70.setFont(font)
        self.label_70.setStyleSheet(u"color: rgb(192, 191, 188);")
        self.label_70.setAlignment(Qt.AlignCenter)
        self.label_70.setWordWrap(True)
        self.progressBar_female_positives = QProgressBar(self.frame_2)
        self.progressBar_female_positives.setObjectName(u"progressBar_female_positives")
        self.progressBar_female_positives.setGeometry(QRect(457, 32, 5, 161))
        self.progressBar_female_positives.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.492611 rgba(87, 227, 137, 255), stop:0.512315 rgba(11, 156, 255, 255));\n"
"}\n"
"\n"
"QProgressBar{\n"
"	background-color: rgb(246, 245, 244);\n"
"}")
        self.progressBar_female_positives.setValue(50)
        self.progressBar_female_positives.setTextVisible(False)
        self.progressBar_female_positives.setOrientation(Qt.Vertical)
        self.label_71 = QLabel(self.frame_2)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(420, 200, 81, 31))
        self.label_71.setFont(font)
        self.label_71.setStyleSheet(u"color: rgb(192, 191, 188);")
        self.label_71.setAlignment(Qt.AlignCenter)
        self.label_71.setWordWrap(True)
        self.progressBar_blood_pressure = QProgressBar(self.frame_2)
        self.progressBar_blood_pressure.setObjectName(u"progressBar_blood_pressure")
        self.progressBar_blood_pressure.setGeometry(QRect(577, 32, 5, 161))
        self.progressBar_blood_pressure.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.492611 rgb(192, 97, 203), stop:0.512315 rgba(11, 156, 255, 255));\n"
"}\n"
"\n"
"QProgressBar{\n"
"	background-color: rgb(246, 245, 244);\n"
"}")
        self.progressBar_blood_pressure.setValue(50)
        self.progressBar_blood_pressure.setTextVisible(False)
        self.progressBar_blood_pressure.setOrientation(Qt.Vertical)
        self.label_72 = QLabel(self.frame_2)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(534, 200, 91, 31))
        self.label_72.setFont(font)
        self.label_72.setStyleSheet(u"color: rgb(192, 191, 188);")
        self.label_72.setAlignment(Qt.AlignCenter)
        self.label_72.setWordWrap(True)
        self.label_73 = QLabel(self.frame_2)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(670, 90, 111, 18))
        self.label_73.setStyleSheet(u"font: 700 11pt \"Cantarell\";\n"
"color: rgb(26, 95, 180);")
        self.total_diagnosed = QLabel(self.frame_2)
        self.total_diagnosed.setObjectName(u"total_diagnosed")
        self.total_diagnosed.setGeometry(QRect(692, 110, 61, 31))
        self.total_diagnosed.setStyleSheet(u"font: 900 18pt \"Cantarell\";")
        self.total_diagnosed.setAlignment(Qt.AlignCenter)
        self.percentage_mild = QLabel(self.frame_2)
        self.percentage_mild.setObjectName(u"percentage_mild")
        self.percentage_mild.setGeometry(QRect(121, 30, 66, 18))
        self.percentage_severe = QLabel(self.frame_2)
        self.percentage_severe.setObjectName(u"percentage_severe")
        self.percentage_severe.setGeometry(QRect(235, 31, 66, 18))
        self.percentage_male_positives = QLabel(self.frame_2)
        self.percentage_male_positives.setObjectName(u"percentage_male_positives")
        self.percentage_male_positives.setGeometry(QRect(354, 32, 66, 18))
        self.percentage_female_positives = QLabel(self.frame_2)
        self.percentage_female_positives.setObjectName(u"percentage_female_positives")
        self.percentage_female_positives.setGeometry(QRect(475, 33, 66, 18))
        self.percentage_blood_pressure = QLabel(self.frame_2)
        self.percentage_blood_pressure.setObjectName(u"percentage_blood_pressure")
        self.percentage_blood_pressure.setGeometry(QRect(591, 31, 66, 18))
        self.frame_3 = QFrame(self.home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(879, 19, 271, 101))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(20, 0, 41, 61))
        self.label_34.setStyleSheet(u"border: none;")
        self.label_34.setPixmap(QPixmap(u":/images/icons8-user-32.png"))
        self.label_34.setScaledContents(False)
        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(75, 7, 131, 41))
        self.label_35.setStyleSheet(u"border:none;\n"
"font: 700 11pt \"Droid Sans Fallback\";\n"
"color: rgb(26, 95, 180);")
        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(230, 17, 21, 21))
        self.label_36.setStyleSheet(u"border: none;")
        self.label_36.setPixmap(QPixmap(u":/images/icons8-notification-64.png"))
        self.label_36.setScaledContents(True)
        self.label_37 = QLabel(self.frame_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(77, 40, 70, 18))
        self.label_37.setStyleSheet(u"border: none;\n"
"color: rgb(189, 189, 189);")
        self.label_38 = QLabel(self.frame_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(78, 68, 111, 18))
        self.label_38.setStyleSheet(u"border:none;\n"
"")
        self.frame_4 = QFrame(self.home)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(41, 470, 241, 111))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_46 = QLabel(self.frame_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(25, 13, 31, 31))
        self.label_46.setStyleSheet(u"")
        self.label_46.setPixmap(QPixmap(u":/images/icons8-virus-48.png"))
        self.label_46.setScaledContents(True)
        self.label_49 = QLabel(self.frame_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(0, 50, 151, 51))
        self.label_49.setPixmap(QPixmap(u":/images/line1.png"))
        self.label_49.setScaledContents(True)
        self.label_52 = QLabel(self.frame_4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(175, 51, 61, 31))
        self.label_52.setStyleSheet(u"font: 900 18pt \"Cantarell\";")
        self.label_55 = QLabel(self.frame_4)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(72, 17, 66, 18))
        self.label_55.setStyleSheet(u"font: 700 11pt \"Cantarell\";")
        self.frame_5 = QFrame(self.home)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(320, 470, 241, 111))
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_47 = QLabel(self.frame_5)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(22, 9, 31, 31))
        self.label_47.setStyleSheet(u"")
        self.label_47.setPixmap(QPixmap(u":/images/icons8-virus-48.png"))
        self.label_47.setScaledContents(True)
        self.label_50 = QLabel(self.frame_5)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(-3, 49, 141, 51))
        self.label_50.setPixmap(QPixmap(u":/images/line2.png"))
        self.label_50.setScaledContents(True)
        self.label_53 = QLabel(self.frame_5)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(172, 50, 61, 31))
        self.label_53.setStyleSheet(u"font: 900 18pt \"Cantarell\";")
        self.label_56 = QLabel(self.frame_5)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(71, 14, 66, 18))
        self.label_56.setStyleSheet(u"font: 700 11pt \"Cantarell\";")
        self.frame_6 = QFrame(self.home)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(590, 470, 261, 111))
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_48 = QLabel(self.frame_6)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(21, 8, 31, 31))
        self.label_48.setStyleSheet(u"")
        self.label_48.setPixmap(QPixmap(u":/images/icons8-virus-48.png"))
        self.label_48.setScaledContents(True)
        self.label_51 = QLabel(self.frame_6)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(-1, 51, 121, 51))
        self.label_51.setPixmap(QPixmap(u":/images/list3.png"))
        self.label_51.setScaledContents(True)
        self.label_54 = QLabel(self.frame_6)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(191, 50, 61, 31))
        self.label_54.setStyleSheet(u"font: 900 18pt \"Cantarell\";")
        self.label_57 = QLabel(self.frame_6)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(71, 12, 66, 18))
        self.label_57.setStyleSheet(u"font: 700 11pt \"Cantarell\";")
        self.frame_7 = QFrame(self.home)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(890, 176, 251, 401))
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(36, 18, 180, 180))
        self.frame_11.setStyleSheet(u"border-style: none;\n"
"border-radius: 0px;")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 0, 180, 180))
        self.frame_13.setStyleSheet(u"border-style:none;\n"
"border-radius:90px;\n"
"background-color: rgba(161, 222, 241, 15);")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, 0, 180, 180))
        self.frame_14.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(129, 61, 156, 0), stop:0.750 rgba(53, 132, 228, 255));")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(20, 20, 140, 140))
        self.frame_15.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:70px;")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_30 = QLabel(self.frame_15)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(23, 51, 101, 18))
        self.label_30.setStyleSheet(u"background-color: rgba(191, 64, 64, 0);")
        self.label_31 = QLabel(self.frame_15)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(55, 71, 66, 18))
        self.label_31.setStyleSheet(u"\n"
"font: 700 11pt \"Bitstream Vera Sans\";")
        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(38, 210, 180, 180))
        self.frame_16.setStyleSheet(u"border-style:none;\n"
"border-radius:90px;\n"
"background-color: ;\n"
"background-color: ;\n"
"background-color: rgba(221, 179, 255, 20);")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(0, 0, 180, 180))
        self.frame_17.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.799 rgba(129, 61, 156, 0), stop:0.800 rgb(129, 61, 156));")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(20, 20, 140, 140))
        self.frame_18.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:70px;")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_32 = QLabel(self.frame_18)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(16, 41, 111, 16))
        self.label_32.setStyleSheet(u"background-color: rgba(191, 64, 64, 0);")
        self.label_33 = QLabel(self.frame_18)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(56, 75, 66, 18))
        self.label_33.setStyleSheet(u"\n"
"font: 700 11pt \"Bitstream Vera Sans\";")
        self.label_64 = QLabel(self.frame_18)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(22, 54, 111, 18))
        self.label_43 = QLabel(self.home)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(46, 150, 91, 31))
        self.label_43.setStyleSheet(u"font: 900 12pt \"Lato\";")
        self.widget = QWidget(self.home)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(47, 176, 24, 5))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(38, 162, 105, 255), stop:1 rgba(0, 177, 255, 255));\n"
"border-radius: 2px;")
        self.label_44 = QLabel(self.home)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(43, 429, 91, 31))
        self.label_44.setStyleSheet(u"font: 900 12pt \"Lato\";")
        self.widget_2 = QWidget(self.home)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(45, 455, 24, 5))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(38, 162, 105, 255), stop:1 rgba(0, 177, 255, 255));\n"
"border-radius: 2px;")
        self.label_45 = QLabel(self.home)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(892, 135, 91, 31))
        self.label_45.setStyleSheet(u"font: 900 12pt \"Lato\";")
        self.widget_3 = QWidget(self.home)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(893, 160, 24, 5))
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(38, 162, 105, 255), stop:1 rgba(0, 177, 255, 255));\n"
"border-radius: 2px;")
        self.popout_box = QWidget(self.home)
        self.popout_box.setObjectName(u"popout_box")
        self.popout_box.setGeometry(QRect(370, 270, 381, 191))
        self.popout_box.setStyleSheet(u"#popout_box{\n"
"background-color: rgb(246, 245, 244);\n"
"border-radius: 10px;\n"
"}")
        self.dialog_button = QPushButton(self.popout_box)
        self.dialog_button.setObjectName(u"dialog_button")
        self.dialog_button.setGeometry(QRect(150, 150, 87, 26))
        self.dialog_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(224, 27, 36);")
        self.label_74 = QLabel(self.popout_box)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(160, 20, 66, 18))
        self.label_74.setStyleSheet(u"font: 800 11pt \"Cantarell\";\n"
"color:rgb(255, 34, 34);")
        self.label_75 = QLabel(self.popout_box)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(120, 60, 261, 18))
        self.label_76 = QLabel(self.popout_box)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(20, 100, 341, 41))
        self.label_76.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"color: rgb(40, 76, 255);\n"
"font: 700 11pt \"Cantarell\";")
        self.label_76.setWordWrap(True)
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_8 = QFrame(self.widgets)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 80, 511, 81))
        self.label.setPixmap(QPixmap(u":/images/button.png"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 150, 511, 91))
        self.label_3.setPixmap(QPixmap(u":/images/button.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 261, 511, 91))
        self.label_4.setPixmap(QPixmap(u":/images/button.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 338, 511, 91))
        self.label_5.setPixmap(QPixmap(u":/images/button.png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(72, 491, 511, 91))
        self.label_6.setPixmap(QPixmap(u":/images/button.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 94, 51, 51))
        self.label_7.setPixmap(QPixmap(u":/images/icons8-person-64.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 167, 51, 51))
        self.label_8.setPixmap(QPixmap(u":/images/icons8-age-50.png"))
        self.label_8.setScaledContents(True)
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(98, 507, 51, 51))
        self.label_9.setPixmap(QPixmap(u":/images/icons8-weight-64.png"))
        self.label_9.setScaledContents(True)
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(94, 278, 51, 51))
        self.label_11.setPixmap(QPixmap(u":/images/icons8-height-50.png"))
        self.label_11.setScaledContents(True)
        self.form_name = QLineEdit(self.frame_8)
        self.form_name.setObjectName(u"form_name")
        self.form_name.setGeometry(QRect(150, 103, 381, 31))
        self.form_name.setStyleSheet(u"border-style: none;")
        self.form_name.setMaxLength(50)
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(94, 357, 51, 51))
        self.label_12.setPixmap(QPixmap(u":/images/icons8-height-50.png"))
        self.label_12.setScaledContents(True)
        self.male_radio = QRadioButton(self.frame_8)
        self.male_radio.setObjectName(u"male_radio")
        self.male_radio.setGeometry(QRect(163, 238, 109, 24))
        self.male_radio.setChecked(True)
        self.female_radio = QRadioButton(self.frame_8)
        self.female_radio.setObjectName(u"female_radio")
        self.female_radio.setGeometry(QRect(302, 238, 109, 24))
        self.diagnosis_submit = QCommandLinkButton(self.frame_8)
        self.diagnosis_submit.setObjectName(u"diagnosis_submit")
        self.diagnosis_submit.setGeometry(QRect(660, 530, 111, 41))
        self.diagnosis_submit.setStyleSheet(u"QObject{\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Cantarell\";\n"
"background-color: rgb(46, 194, 126);\n"
"border: none\n"
"}\n"
"\n"
"QObject:hover{\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Cantarell\";\n"
"background-color: rgb(43, 194, 44);\n"
"}\n"
"\n"
"QObject:pressed{\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Cantarell\";\n"
"background-color: rgb(143, 240, 164);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.diagnosis_submit.setCheckable(False)
        self.symptom_dropdown = QComboBox(self.frame_8)
        self.symptom_dropdown.setObjectName(u"symptom_dropdown")
        self.symptom_dropdown.setGeometry(QRect(630, 92, 451, 41))
        self.symptom_dropdown.setStyleSheet(u"color: rgb(94, 92, 100);\n"
"border-color: rgb(46, 194, 126);")
        self.symptom_display = QLabel(self.frame_8)
        self.symptom_display.setObjectName(u"symptom_display")
        self.symptom_display.setGeometry(QRect(643, 170, 461, 61))
        self.symptom_display.setFont(font)
        self.symptom_display.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(640, 138, 161, 21))
        self.label_13.setStyleSheet(u"font: 700 11pt \"Cantarell\";\n"
"color: rgb(94, 92, 100);")
        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(70, 415, 511, 91))
        self.label_14.setPixmap(QPixmap(u":/images/button.png"))
        self.label_14.setScaledContents(True)
        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(96, 432, 51, 51))
        self.label_15.setPixmap(QPixmap(u":/images/icons8-temperature-50.png"))
        self.label_15.setScaledContents(True)
        self.label_28 = QLabel(self.frame_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(466, 16, 51, 51))
        self.label_28.setPixmap(QPixmap(u":/images/icons8-add-user-male-48.png"))
        self.label_28.setScaledContents(True)
        self.line_5 = QFrame(self.frame_8)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(540, 30, 1, 30))
        self.line_5.setStyleSheet(u"background-color: rgb(189, 189, 189);")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(568, 30, 181, 31))
        self.label_29.setStyleSheet(u"color: rgb(94, 92, 100);\n"
"font: 700 11pt \"FontAwesome\";")
        self.hypertension = QWidget(self.frame_8)
        self.hypertension.setObjectName(u"hypertension")
        self.hypertension.setGeometry(QRect(650, 427, 461, 101))
        self.label_26 = QLabel(self.hypertension)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(4, 0, 161, 21))
        self.label_26.setStyleSheet(u"font: 700 11pt \"Cantarell\";\n"
"color: rgb(94, 92, 100);")
        self.label_27 = QLabel(self.hypertension)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(8, 35, 51, 18))
        self.label_58 = QLabel(self.hypertension)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(200, 36, 61, 18))
        self.no_Bp = QPushButton(self.hypertension)
        self.no_Bp.setObjectName(u"no_Bp")
        self.no_Bp.setGeometry(QRect(347, 79, 101, 15))
        font4 = QFont()
        font4.setFamilies([u"Cantarell"])
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(False)
        self.no_Bp.setFont(font4)
        self.no_Bp.setStyleSheet(u"QObject\n"
"{\n"
"		border: none;\n"
"		background-color: rgb(224, 27, 36);\n"
"		font: 700 9pt \"Cantarell\";\n"
"		border-radius: 5px;\n"
"}\n"
"\n"
"QObject:pressed\n"
"{\n"
"		border: none;\n"
"	    background-color: rgb(237, 51, 59);\n"
"		font: 700 9pt \"Cantarell\";\n"
"		border-radius: 5px;\n"
"}\n"
"")
        self.form_systolic = QSpinBox(self.hypertension)
        self.form_systolic.setObjectName(u"form_systolic")
        self.form_systolic.setGeometry(QRect(70, 30, 111, 31))
        self.form_systolic.setStyleSheet(u"QSpinBox::up-arrow{\n"
"	image: url(:/icons/images/icons/cil-caret-top.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"QSpinBox::down-arrow {\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button{\n"
"	background-color: rgb(94, 92, 100);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed{\n"
"	background-color: rgb(192, 191, 188);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"   color: rgb(154, 153, 150);\n"
"padding-right:15px;\n"
"border-style: solid;\n"
"border-color:rgb(38, 162, 105);\n"
"}\n"
"")
        self.form_systolic.setMinimum(0)
        self.form_systolic.setMaximum(200)
        self.form_systolic.setValue(0)
        self.form_diastolic = QSpinBox(self.hypertension)
        self.form_diastolic.setObjectName(u"form_diastolic")
        self.form_diastolic.setGeometry(QRect(280, 30, 111, 31))
        self.form_diastolic.setStyleSheet(u"QSpinBox::up-arrow{\n"
"	image: url(:/icons/images/icons/cil-caret-top.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"QSpinBox::down-arrow {\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button{\n"
"	background-color: rgb(94, 92, 100);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed{\n"
"	background-color: rgb(192, 191, 188);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"   color: rgb(154, 153, 150);\n"
"padding-right:15px;\n"
"border-style: solid;\n"
"border-color:rgb(38, 162, 105);\n"
"}\n"
"")
        self.form_diastolic.setMinimum(0)
        self.form_diastolic.setMaximum(200)
        self.form_diastolic.setValue(0)
        self.clear_button = QPushButton(self.frame_8)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(1040, 140, 45, 15))
        self.clear_button.setStyleSheet(u"QObject\n"
"{\n"
"		border: none;\n"
"		background-color: rgb(224, 27, 36);\n"
"		font: 700 9pt \"Cantarell\";\n"
"		border-radius: 5px;\n"
"}\n"
"\n"
"QObject:pressed\n"
"{\n"
"		border: none;\n"
"	    background-color: rgb(237, 51, 59);\n"
"		font: 700 9pt \"Cantarell\";\n"
"		border-radius: 5px;\n"
"}\n"
"")
        self.form_age = QSpinBox(self.frame_8)
        self.form_age.setObjectName(u"form_age")
        self.form_age.setGeometry(QRect(174, 178, 151, 31))
        self.form_age.setStyleSheet(u"QSpinBox::up-arrow{\n"
"	image: url(:/icons/images/icons/cil-caret-top.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"QSpinBox::down-arrow {\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button{\n"
"	background-color: rgb(94, 92, 100);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed{\n"
"	background-color: rgb(192, 191, 188);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    color: rgb(154, 153, 150);\n"
"padding-right:15px;\n"
"}\n"
"")
        self.form_age.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.form_age.setKeyboardTracking(True)
        self.form_age.setMinimum(1)
        self.form_age.setMaximum(200)
        self.error_message = QWidget(self.frame_8)
        self.error_message.setObjectName(u"error_message")
        self.error_message.setGeometry(QRect(810, 536, 181, 31))
        self.error_message.setStyleSheet(u"background-color: rgb(255, 120, 120);")
        self.label_59 = QLabel(self.error_message)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(17, 7, 151, 18))
        self.label_59.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.form_height_feet = QSpinBox(self.frame_8)
        self.form_height_feet.setObjectName(u"form_height_feet")
        self.form_height_feet.setGeometry(QRect(175, 286, 151, 31))
        self.form_height_feet.setStyleSheet(u"QSpinBox::up-arrow{\n"
"	image: url(:/icons/images/icons/cil-caret-top.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"QSpinBox::down-arrow {\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button{\n"
"	background-color: rgb(94, 92, 100);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed{\n"
"	background-color: rgb(192, 191, 188);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    color: rgb(154, 153, 150);\n"
"padding-right:15px;\n"
"}\n"
"")
        self.form_height_feet.setMinimum(1)
        self.form_height_feet.setMaximum(8)
        self.form_height_feet.setValue(1)
        self.form_height_inches = QSpinBox(self.frame_8)
        self.form_height_inches.setObjectName(u"form_height_inches")
        self.form_height_inches.setGeometry(QRect(176, 364, 151, 31))
        self.form_height_inches.setStyleSheet(u"QSpinBox::up-arrow{\n"
"	image: url(:/icons/images/icons/cil-caret-top.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"QSpinBox::down-arrow {\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button{\n"
"	background-color: rgb(94, 92, 100);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed{\n"
"	background-color: rgb(192, 191, 188);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    color: rgb(154, 153, 150);\n"
"padding-right:15px;\n"
"}\n"
"")
        self.form_height_inches.setMinimum(0)
        self.form_height_inches.setMaximum(11)
        self.form_height_inches.setValue(0)
        self.form_temperature = QSpinBox(self.frame_8)
        self.form_temperature.setObjectName(u"form_temperature")
        self.form_temperature.setGeometry(QRect(175, 441, 151, 31))
        self.form_temperature.setStyleSheet(u"QSpinBox::up-arrow{\n"
"	image: url(:/icons/images/icons/cil-caret-top.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"QSpinBox::down-arrow {\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button{\n"
"	background-color: rgb(94, 92, 100);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed{\n"
"	background-color: rgb(192, 191, 188);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    color: rgb(154, 153, 150);\n"
"padding-right:15px;\n"
"}\n"
"")
        self.form_temperature.setMinimum(0)
        self.form_temperature.setMaximum(100)
        self.form_temperature.setValue(0)
        self.form_weight = QSpinBox(self.frame_8)
        self.form_weight.setObjectName(u"form_weight")
        self.form_weight.setGeometry(QRect(177, 518, 151, 31))
        self.form_weight.setStyleSheet(u"QSpinBox::up-arrow{\n"
"	image: url(:/icons/images/icons/cil-caret-top.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"QSpinBox::down-arrow {\n"
"	image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"   width:10px;\n"
"   height:15px;\n"
"   \n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button{\n"
"	background-color: rgb(94, 92, 100);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed{\n"
"	background-color: rgb(192, 191, 188);\n"
"    top:1px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    color: rgb(154, 153, 150);\n"
"padding-right:15px;\n"
"}\n"
"")
        self.form_weight.setMinimum(1)
        self.form_weight.setMaximum(1000)
        self.form_weight.setValue(1)
        self.label_60 = QLabel(self.frame_8)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(642, 338, 161, 21))
        self.label_60.setStyleSheet(u"font: 700 11pt \"Cantarell\";\n"
"color: rgb(94, 92, 100);")
        self.conditions_dropdown = QComboBox(self.frame_8)
        self.conditions_dropdown.setObjectName(u"conditions_dropdown")
        self.conditions_dropdown.setGeometry(QRect(630, 290, 451, 41))
        self.conditions_dropdown.setStyleSheet(u"color: rgb(94, 92, 100);\n"
"border-color: rgb(46, 194, 126);")
        self.conditions_display = QLabel(self.frame_8)
        self.conditions_display.setObjectName(u"conditions_display")
        self.conditions_display.setGeometry(QRect(646, 370, 461, 51))
        self.conditions_display.setFont(font)
        self.conditions_display.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.clear_conditions_button = QPushButton(self.frame_8)
        self.clear_conditions_button.setObjectName(u"clear_conditions_button")
        self.clear_conditions_button.setGeometry(QRect(1049, 340, 43, 15))
        self.clear_conditions_button.setStyleSheet(u"QObject\n"
"{\n"
"		border: none;\n"
"		background-color: rgb(224, 27, 36);\n"
"		font: 700 9pt \"Cantarell\";\n"
"		border-radius: 7px;\n"
"}\n"
"\n"
"QObject:pressed\n"
"{\n"
"		border: none;\n"
"	    background-color: rgb(237, 51, 59);\n"
"		font: 700 9pt \"Cantarell\";\n"
"		border-radius: 7px;\n"
"}\n"
"")
        self.widget_4 = QWidget(self.frame_8)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(650, 240, 421, 41))
        self.mild_symptoms = QRadioButton(self.widget_4)
        self.mild_symptoms.setObjectName(u"mild_symptoms")
        self.mild_symptoms.setGeometry(QRect(20, 10, 141, 24))
        self.mild_symptoms.setChecked(True)
        self.severe_symptoms = QRadioButton(self.widget_4)
        self.severe_symptoms.setObjectName(u"severe_symptoms")
        self.severe_symptoms.setGeometry(QRect(220, 10, 151, 24))

        self.verticalLayout.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.frame_9 = QFrame(self.new_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 2, 1171, 601))
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(120, 210, 131, 18))
        self.label_16.setStyleSheet(u"font: 600 11pt \"URW Gothic\";")
        self.add_covid = QLineEdit(self.frame_9)
        self.add_covid.setObjectName(u"add_covid")
        self.add_covid.setGeometry(QRect(70, 260, 211, 31))
        self.add_covid.setStyleSheet(u"border-color: rgb(94, 92, 100);")
        self.bp_check_covid = QCheckBox(self.frame_9)
        self.bp_check_covid.setObjectName(u"bp_check_covid")
        self.bp_check_covid.setGeometry(QRect(110, 320, 151, 21))
        self.line = QFrame(self.frame_9)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(310, 190, 1, 221))
        self.line.setStyleSheet(u"background-color: rgb(189, 189, 189)")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.add_button_covid = QPushButton(self.frame_9)
        self.add_button_covid.setObjectName(u"add_button_covid")
        self.add_button_covid.setGeometry(QRect(130, 390, 111, 31))
        self.add_button_covid.setStyleSheet(u"background-color: rgb(28, 113, 216);")
        self.line_2 = QFrame(self.frame_9)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(580, 190, 1, 221))
        self.line_2.setStyleSheet(u"background-color: rgb(189, 189, 189)")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.frame_9)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(850, 190, 1, 221))
        self.line_3.setStyleSheet(u"background-color: rgb(189, 189, 189)")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_17 = QLabel(self.frame_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(390, 210, 131, 18))
        self.label_17.setStyleSheet(u"font: 600 11pt \"URW Gothic\";")
        self.bp_check_delta = QCheckBox(self.frame_9)
        self.bp_check_delta.setObjectName(u"bp_check_delta")
        self.bp_check_delta.setGeometry(QRect(380, 320, 151, 24))
        self.add_delta = QLineEdit(self.frame_9)
        self.add_delta.setObjectName(u"add_delta")
        self.add_delta.setGeometry(QRect(340, 260, 211, 31))
        self.add_delta.setStyleSheet(u"border-color: rgb(94, 92, 100);")
        self.add_button_delta = QPushButton(self.frame_9)
        self.add_button_delta.setObjectName(u"add_button_delta")
        self.add_button_delta.setGeometry(QRect(400, 390, 111, 31))
        self.add_button_delta.setStyleSheet(u"background-color: rgb(28, 113, 216);")
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(650, 210, 141, 18))
        self.label_18.setStyleSheet(u"font: 600 11pt \"URW Gothic\";")
        self.label_19 = QLabel(self.frame_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(890, 210, 191, 18))
        self.label_19.setStyleSheet(u"font: 600 11pt \"URW Gothic\";")
        self.add_omicron = QLineEdit(self.frame_9)
        self.add_omicron.setObjectName(u"add_omicron")
        self.add_omicron.setGeometry(QRect(610, 260, 211, 31))
        self.add_omicron.setStyleSheet(u"border-color: rgb(94, 92, 100);")
        self.bp_check_omicron = QCheckBox(self.frame_9)
        self.bp_check_omicron.setObjectName(u"bp_check_omicron")
        self.bp_check_omicron.setGeometry(QRect(640, 320, 151, 24))
        self.add_button_omicron = QPushButton(self.frame_9)
        self.add_button_omicron.setObjectName(u"add_button_omicron")
        self.add_button_omicron.setGeometry(QRect(670, 390, 111, 31))
        self.add_button_omicron.setStyleSheet(u"background-color: rgb(28, 113, 216);")
        self.add_button_conditions = QPushButton(self.frame_9)
        self.add_button_conditions.setObjectName(u"add_button_conditions")
        self.add_button_conditions.setGeometry(QRect(930, 390, 111, 31))
        self.add_button_conditions.setStyleSheet(u"background-color: rgb(28, 113, 216);")
        self.bp_check_conditions = QCheckBox(self.frame_9)
        self.bp_check_conditions.setObjectName(u"bp_check_conditions")
        self.bp_check_conditions.setGeometry(QRect(910, 320, 151, 24))
        self.add_conditions = QLineEdit(self.frame_9)
        self.add_conditions.setObjectName(u"add_conditions")
        self.add_conditions.setGeometry(QRect(880, 260, 211, 31))
        self.add_conditions.setStyleSheet(u"border-color: rgb(94, 92, 100);\n"
"border-style: solid;")
        self.label_20 = QLabel(self.frame_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(440, 40, 91, 81))
        self.label_20.setPixmap(QPixmap(u":/images/icons8-add-64.png"))
        self.label_20.setScaledContents(True)
        self.line_4 = QFrame(self.frame_9)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(550, 61, 1, 50))
        self.line_4.setStyleSheet(u"background-color: rgb(189, 189, 189)")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(580, 60, 201, 61))
        self.label_21.setStyleSheet(u"font: 700 11pt \"FontAwesome\";\n"
"color: rgb(94, 92, 100);")
        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(160, 170, 31, 31))
        self.label_22.setPixmap(QPixmap(u":/images/icons8-add-48.png"))
        self.label_22.setScaledContents(True)
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(430, 170, 31, 31))
        self.label_23.setPixmap(QPixmap(u":/images/icons8-add-48.png"))
        self.label_23.setScaledContents(True)
        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(696, 170, 31, 31))
        self.label_24.setPixmap(QPixmap(u":/images/icons8-add-48.png"))
        self.label_24.setScaledContents(True)
        self.label_25 = QLabel(self.frame_9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(970, 170, 31, 31))
        self.label_25.setPixmap(QPixmap(u":/images/icons8-add-48.png"))
        self.label_25.setScaledContents(True)
        self.success_message = QWidget(self.frame_9)
        self.success_message.setObjectName(u"success_message")
        self.success_message.setGeometry(QRect(900, 20, 251, 31))
        self.label_10 = QLabel(self.success_message)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(90, 8, 131, 18))
        self.label_61 = QLabel(self.success_message)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(60, 6, 21, 21))
        self.label_61.setPixmap(QPixmap(u":/images/icons8-ok.gif"))
        self.label_61.setScaledContents(True)
        self.error_message_2 = QWidget(self.frame_9)
        self.error_message_2.setObjectName(u"error_message_2")
        self.error_message_2.setGeometry(QRect(900, 60, 251, 31))
        self.label_62 = QLabel(self.error_message_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(54, 0, 31, 31))
        self.label_62.setPixmap(QPixmap(u":/images/icons8-error-48.png"))
        self.label_62.setScaledContents(True)
        self.label_63 = QLabel(self.error_message_2)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(110, 10, 111, 18))
        self.stackedWidget.addWidget(self.new_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 0, 1151, 601))
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.diagnosis_main = QLabel(self.frame_10)
        self.diagnosis_main.setObjectName(u"diagnosis_main")
        self.diagnosis_main.setGeometry(QRect(260, 30, 671, 201))
        self.diagnosis_main.setStyleSheet(u"font: 700 14pt \"Cantarell\";\n"
"color: rgb(28, 113, 216);")
        self.diagnosis_main.setAlignment(Qt.AlignCenter)
        self.diagnosis_main.setWordWrap(True)
        self.diagnosis_suggestion = QLabel(self.frame_10)
        self.diagnosis_suggestion.setObjectName(u"diagnosis_suggestion")
        self.diagnosis_suggestion.setGeometry(QRect(330, 260, 541, 151))
        self.diagnosis_suggestion.setStyleSheet(u"color: rgb(49, 50, 60);")
        self.diagnosis_suggestion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.pushButton_5 = QPushButton(self.frame_10)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(450, 440, 271, 41))
        self.pushButton_5.setStyleSheet(u"QObject\n"
"{\n"
"		border: none;\n"
"		font: 700 11pt \"Cantarell\";\n"
"		background-color: rgb(26, 95, 180);\n"
"		border-radius: 8px;\n"
"}\n"
"\n"
"QObject:hover\n"
"{\n"
"	background-color: rgb(53, 132, 228);\n"
"	border: none;\n"
"}\n"
"\n"
"QObject:pressed\n"
"{\n"
"	background-color: rgb(28, 113, 216);\n"
"	border: none\n"
"}")
        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText("")
        self.label_2.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Diagnose", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"Add Facts", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Covidex", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Hi</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>User.</p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Remember to check the latest COVID-19 updates at the Ministry Website</p></body></html>", None))
        self.label_42.setText("")
        self.progressBar_mild.setFormat("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>100</p></body></html>", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>50</p></body></html>", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0</p></body></html>", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Mild Symptoms</span></p></body></html>", None))
        self.progressBar_severe.setFormat("")
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Severe Symptoms</span></p></body></html>", None))
        self.progressBar_male_positives.setFormat("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Male Positives</span></p></body></html>", None))
        self.progressBar_female_positives.setFormat("")
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Female Positives</span></p></body></html>", None))
        self.progressBar_blood_pressure.setFormat("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">High/Low Blood Pressure</span></p></body></html>", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Total Diagnosed</p></body></html>", None))
        self.total_diagnosed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0</p></body></html>", None))
        self.percentage_mild.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0 %</p></body></html>", None))
        self.percentage_severe.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0 %</p></body></html>", None))
        self.percentage_male_positives.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0 %</p></body></html>", None))
        self.percentage_female_positives.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0 %</p></body></html>", None))
        self.percentage_blood_pressure.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0 %</p></body></html>", None))
        self.label_34.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">John Doe</span></p></body></html>", None))
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Health Expert", None))
        self.label_46.setText("")
        self.label_49.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0%</p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Covid</p></body></html>", None))
        self.label_47.setText("")
        self.label_50.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0%</p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Delta</p></body></html>", None))
        self.label_48.setText("")
        self.label_51.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0%</p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Omicron</p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Positive Cases", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Omicron Variant</p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"20%", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>with conditions</p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Cases", None))
        self.dialog_button.setText(QCoreApplication.translate("MainWindow", u"Okay", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"ALERT!", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"There is a surge in cases", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Recommendation: Issue an all island Quarantine.", None))
        self.label.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_11.setText("")
        self.form_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_12.setText("")
        self.male_radio.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.female_radio.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.diagnosis_submit.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.symptom_dropdown.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Symptom(s)", None))
        self.symptom_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Selected Symptoms:</span></p></body></html>", None))
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Diagnosis</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Blood Pressure</p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Systolic", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Diastolic</p></body></html>", None))
        self.no_Bp.setText(QCoreApplication.translate("MainWindow", u"Dont Require", None))
        self.form_systolic.setSpecialValueText(QCoreApplication.translate("MainWindow", u"mm Hg", None))
        self.form_systolic.setSuffix(QCoreApplication.translate("MainWindow", u" mm Hg", None))
        self.form_diastolic.setSpecialValueText(QCoreApplication.translate("MainWindow", u"mm Hg", None))
        self.form_diastolic.setSuffix(QCoreApplication.translate("MainWindow", u" mm Hg", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.form_age.setSpecialValueText("")
        self.form_age.setPrefix(QCoreApplication.translate("MainWindow", u"Age:  ", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Please fill out all fields", None))
        self.form_height_feet.setSpecialValueText("")
        self.form_height_feet.setSuffix(QCoreApplication.translate("MainWindow", u" ft", None))
        self.form_height_feet.setPrefix(QCoreApplication.translate("MainWindow", u"Height (Ft): ", None))
        self.form_height_inches.setSpecialValueText("")
        self.form_height_inches.setSuffix(QCoreApplication.translate("MainWindow", u" in", None))
        self.form_height_inches.setPrefix(QCoreApplication.translate("MainWindow", u"Height (In): ", None))
        self.form_temperature.setSpecialValueText("")
        self.form_temperature.setSuffix(QCoreApplication.translate("MainWindow", u" \u00b0C", None))
        self.form_temperature.setPrefix(QCoreApplication.translate("MainWindow", u"Temperature : ", None))
        self.form_weight.setSpecialValueText("")
        self.form_weight.setSuffix(QCoreApplication.translate("MainWindow", u" Kgs", None))
        self.form_weight.setPrefix(QCoreApplication.translate("MainWindow", u"Weight (Kg):  ", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Selected Symptoms:</span></p></body></html>", None))
        self.conditions_dropdown.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Underlying Condition(s)", None))
        self.conditions_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.clear_conditions_button.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.mild_symptoms.setText(QCoreApplication.translate("MainWindow", u"Mild Symptoms", None))
        self.severe_symptoms.setText(QCoreApplication.translate("MainWindow", u"Severe Symptoms", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Add Covid Fact", None))
        self.add_covid.setText("")
        self.add_covid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add Symptom", None))
        self.bp_check_covid.setText(QCoreApplication.translate("MainWindow", u"Require BP check", None))
        self.add_button_covid.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add Delta Fact</p></body></html>", None))
        self.bp_check_delta.setText(QCoreApplication.translate("MainWindow", u"Require BP check", None))
        self.add_delta.setText("")
        self.add_delta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add Symptom", None))
        self.add_button_delta.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add Omicron Fact</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add Underlying Condition</p></body></html>", None))
        self.add_omicron.setText("")
        self.add_omicron.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add Symptom", None))
        self.bp_check_omicron.setText(QCoreApplication.translate("MainWindow", u"Require BP check", None))
        self.add_button_omicron.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.add_button_conditions.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.bp_check_conditions.setText(QCoreApplication.translate("MainWindow", u"Require BP check", None))
        self.add_conditions.setText("")
        self.add_conditions.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add Condition", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">Add Facts</span></p></body></html>", None))
        self.label_22.setText("")
        self.label_23.setText("")
        self.label_24.setText("")
        self.label_25.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sucessfully Added", None))
        self.label_61.setText("")
        self.label_62.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Check Fields", None))
        self.diagnosis_main.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Diagnosis</span></p></body></html>", None))
        self.diagnosis_suggestion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Suggestion</span></p></body></html>", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Stay up to date about COVID-19", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: J.Jones | S.Porter | R.Alberts", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.5", None))
    # retranslateUi

