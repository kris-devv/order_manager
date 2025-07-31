# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1196, 704)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"* {\n"
"	color: black;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	padding-left: 6px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 20px;\n"
"    height: 20px;\n"
"    border: 2px solid #10B981;\n"
"    border-radius: 4px;\n"
"    background-color: white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #34D399; \n"
"    border: 2px solid #34D399;\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"	background-color: #f0f0f0;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: #E5E5E5;\n"
"	border: none;\n"
"	border-bottom-right-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"QListWidget::item {\n"
"    padding: 6px;\n"
"	padding-left: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QListWidget::item:hover {\n"
"    background-color: #3B82F6;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: #F0F0F0;\n"
"	color: #3B82F6;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border-left: 4px solid #3B82F6;\n"
"}\n"
"#styleSheet {\n"
"	background-color"
                        ": #F0F0F0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* Left Section (List)\n"
"//////////////////////////////////////////////////////////////////////*/\n"
"#searchBar {\n"
"	background-color: #E5E5E5;\n"
"	border: none;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom: 2px solid #3B82F6;\n"
"}\n"
"#addOrderButton {\n"
"	background-color: #3B82F6;\n"
"	border: none;\n"
"	border-top-right-radius: 5px;\n"
"	border-top-left-radius: 5px;\n"
"}\n"
"\n"
"/* Right Section (Pages)\n"
"//////////////////////////////////////////////////////////////////////*/\n"
"#rightContentSection QLineEdit {\n"
"	border: 1px solid #3B82F6;\n"
"	border-radius: 5px;\n"
"}\n"
"#rightContentSection QPlainTextEdit {\n"
"	border: 1px solid #3B82F6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* Top Menu\n"
"//////////////////////////////////////////////////////////////////////*/\n"
"#topMenu {\n"
"	background-color:	#E5E5E5;\n"
"	border-radius: 5px;\n"
"}\n"
"#topMenu QPushButton {\n"
"	border: none;\n"
"}\n"
"#topMenuLogo {\n"
"	background-"
                        "image: url(:/images/resources/images/mfcomp-small.png);\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* Settings Frame\n"
"//////////////////////////////////////////////////////////////////////*/\n"
"#settingsFrame {\n"
"	background-color: #E5E5E5;\n"
"	border: none;\n"
"}\n"
"#settingsFrame QPushButton{\n"
"	background-color: #3B82F6;\n"
"	border: none;\n"
"	color: white;\n"
"}\n"
"\n"
"/* Credits Frame\n"
"//////////////////////////////////////////////////////////////////////*/\n"
"#creditsFrame {\n"
"	background-color:	#E5E5E5;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* Add Order Page\n"
"//////////////////////////////////////////////////////////////////////*/\n"
"#rightStackedWidget QLineEdit {\n"
"	background-color:	#E5E5E5;\n"
"}\n"
"#rightStackedWidget QPlainTextEdit {\n"
"	background-color:	#E5E5E5;\n"
"}\n"
"#rightStackedWidget QPushButton{\n"
"	background-color: #3B82F6;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* Home Page\n"
"///////////////////////////////"
                        "///////////////////////////////////////*/\n"
"#homePage {\n"
"	background-image: url(:/images/resources/images/mfcomp.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.styleSheet)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.styleSheet)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(150, 300))
        self.leftMenu.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 0, 4)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchBar = QLineEdit(self.leftMenu)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(9)
        self.searchBar.setFont(font)
        self.searchBar.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.searchBar, 0, Qt.AlignmentFlag.AlignBottom)

        self.addOrderButton = QPushButton(self.leftMenu)
        self.addOrderButton.setObjectName(u"addOrderButton")
        self.addOrderButton.setMinimumSize(QSize(40, 40))
        self.addOrderButton.setMaximumSize(QSize(40, 40))
        self.addOrderButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/cil-library-add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addOrderButton.setIcon(icon)
        self.addOrderButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.addOrderButton, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.listWidget = QListWidget(self.leftMenu)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        font1 = QFont()
        font1.setPointSize(12)
        self.listWidget.setFont(font1)
        self.listWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.rightContentSection = QWidget(self.styleSheet)
        self.rightContentSection.setObjectName(u"rightContentSection")
        self.verticalLayout = QVBoxLayout(self.rightContentSection)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 4, 4, 4)
        self.topMenu = QFrame(self.rightContentSection)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 40))
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.topMenu)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(8, 0, 0, 0)
        self.btnHome = QPushButton(self.topMenu)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(40, 40))
        self.btnHome.setMaximumSize(QSize(40, 40))
        self.btnHome.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/icon_home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHome.setIcon(icon1)
        self.btnHome.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.btnHome)

        self.topMenuVLine2 = QFrame(self.topMenu)
        self.topMenuVLine2.setObjectName(u"topMenuVLine2")
        self.topMenuVLine2.setMinimumSize(QSize(0, 25))
        self.topMenuVLine2.setMaximumSize(QSize(1, 25))
        self.topMenuVLine2.setStyleSheet(u"background-color: #F0F0F0;")
        self.topMenuVLine2.setFrameShadow(QFrame.Shadow.Sunken)
        self.topMenuVLine2.setLineWidth(0)
        self.topMenuVLine2.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_5.addWidget(self.topMenuVLine2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.topMenuLogo = QLabel(self.topMenu)
        self.topMenuLogo.setObjectName(u"topMenuLogo")
        self.topMenuLogo.setMinimumSize(QSize(120, 35))
        self.topMenuLogo.setMaximumSize(QSize(120, 35))

        self.horizontalLayout_5.addWidget(self.topMenuLogo, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.topMenuLabel = QLabel(self.topMenu)
        self.topMenuLabel.setObjectName(u"topMenuLabel")
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.topMenuLabel.setFont(font2)

        self.horizontalLayout_5.addWidget(self.topMenuLabel)

        self.topMenuHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.topMenuHSpacer)

        self.settingsButton = QPushButton(self.topMenu)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(40, 40))
        self.settingsButton.setMaximumSize(QSize(40, 40))
        self.settingsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsButton.setIcon(icon2)
        self.settingsButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.settingsButton)

        self.topMenuVLine1 = QFrame(self.topMenu)
        self.topMenuVLine1.setObjectName(u"topMenuVLine1")
        self.topMenuVLine1.setMinimumSize(QSize(0, 25))
        self.topMenuVLine1.setMaximumSize(QSize(1, 25))
        self.topMenuVLine1.setStyleSheet(u"background-color: #F0F0F0;")
        self.topMenuVLine1.setFrameShadow(QFrame.Shadow.Sunken)
        self.topMenuVLine1.setLineWidth(0)
        self.topMenuVLine1.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_5.addWidget(self.topMenuVLine1, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnMin = QPushButton(self.topMenu)
        self.btnMin.setObjectName(u"btnMin")
        self.btnMin.setMinimumSize(QSize(40, 40))
        self.btnMin.setMaximumSize(QSize(40, 40))
        self.btnMin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMin.setIcon(icon3)
        self.btnMin.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.btnMin)

        self.btnMax = QPushButton(self.topMenu)
        self.btnMax.setObjectName(u"btnMax")
        self.btnMax.setMinimumSize(QSize(40, 40))
        self.btnMax.setMaximumSize(QSize(40, 40))
        self.btnMax.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/resources/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMax.setIcon(icon4)
        self.btnMax.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.btnMax)

        self.btnClose = QPushButton(self.topMenu)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(40, 40))
        self.btnClose.setMaximumSize(QSize(40, 40))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/resources/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon5)
        self.btnClose.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.btnClose)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.topMenu)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.rightStackedWidget = QStackedWidget(self.rightContentSection)
        self.rightStackedWidget.setObjectName(u"rightStackedWidget")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.rightStackedWidget.addWidget(self.homePage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.verticalLayout_6 = QVBoxLayout(self.infoPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.editPageVSpacer1_2 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.editPageVSpacer1_2)

        self.infoPageLabel = QLabel(self.infoPage)
        self.infoPageLabel.setObjectName(u"infoPageLabel")
        font3 = QFont()
        font3.setPointSize(24)
        self.infoPageLabel.setFont(font3)
        self.infoPageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.infoPageLabel)

        self.editPageVSpacer2_2 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.editPageVSpacer2_2)

        self.infoPageInputGrid = QGridLayout()
        self.infoPageInputGrid.setObjectName(u"infoPageInputGrid")
        self.infoPageInputGrid.setHorizontalSpacing(32)
        self.infoPageInputGrid.setVerticalSpacing(16)
        self.infoPagePhoneLayout = QVBoxLayout()
        self.infoPagePhoneLayout.setSpacing(4)
        self.infoPagePhoneLayout.setObjectName(u"infoPagePhoneLayout")
        self.infoPagePhoneLabel = QLabel(self.infoPage)
        self.infoPagePhoneLabel.setObjectName(u"infoPagePhoneLabel")
        self.infoPagePhoneLabel.setFont(font1)

        self.infoPagePhoneLayout.addWidget(self.infoPagePhoneLabel)

        self.infoPagePhoneLineEdit = QLineEdit(self.infoPage)
        self.infoPagePhoneLineEdit.setObjectName(u"infoPagePhoneLineEdit")
        self.infoPagePhoneLineEdit.setMinimumSize(QSize(0, 30))
        self.infoPagePhoneLineEdit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.infoPagePhoneLineEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.infoPagePhoneLineEdit.setReadOnly(True)

        self.infoPagePhoneLayout.addWidget(self.infoPagePhoneLineEdit)


        self.infoPageInputGrid.addLayout(self.infoPagePhoneLayout, 0, 0, 1, 1)

        self.infoPageModelLayout = QVBoxLayout()
        self.infoPageModelLayout.setSpacing(4)
        self.infoPageModelLayout.setObjectName(u"infoPageModelLayout")
        self.infoPageModelLabel = QLabel(self.infoPage)
        self.infoPageModelLabel.setObjectName(u"infoPageModelLabel")
        self.infoPageModelLabel.setFont(font1)

        self.infoPageModelLayout.addWidget(self.infoPageModelLabel)

        self.infoPageModelLineEdit = QLineEdit(self.infoPage)
        self.infoPageModelLineEdit.setObjectName(u"infoPageModelLineEdit")
        self.infoPageModelLineEdit.setMinimumSize(QSize(0, 30))
        self.infoPageModelLineEdit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.infoPageModelLineEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.infoPageModelLineEdit.setFrame(True)
        self.infoPageModelLineEdit.setReadOnly(True)

        self.infoPageModelLayout.addWidget(self.infoPageModelLineEdit)


        self.infoPageInputGrid.addLayout(self.infoPageModelLayout, 0, 1, 1, 1)

        self.infoPageForUsLayout = QVBoxLayout()
        self.infoPageForUsLayout.setSpacing(4)
        self.infoPageForUsLayout.setObjectName(u"infoPageForUsLayout")
        self.infoPageForUsLabel = QLabel(self.infoPage)
        self.infoPageForUsLabel.setObjectName(u"infoPageForUsLabel")
        self.infoPageForUsLabel.setFont(font1)

        self.infoPageForUsLayout.addWidget(self.infoPageForUsLabel)

        self.infoPageForUsPlainTextEdit = QPlainTextEdit(self.infoPage)
        self.infoPageForUsPlainTextEdit.setObjectName(u"infoPageForUsPlainTextEdit")
        self.infoPageForUsPlainTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.infoPageForUsPlainTextEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.infoPageForUsPlainTextEdit.setReadOnly(True)

        self.infoPageForUsLayout.addWidget(self.infoPageForUsPlainTextEdit)


        self.infoPageInputGrid.addLayout(self.infoPageForUsLayout, 1, 1, 1, 1)

        self.infoPageDescLayout = QVBoxLayout()
        self.infoPageDescLayout.setSpacing(4)
        self.infoPageDescLayout.setObjectName(u"infoPageDescLayout")
        self.infoPageDescLabel = QLabel(self.infoPage)
        self.infoPageDescLabel.setObjectName(u"infoPageDescLabel")
        self.infoPageDescLabel.setFont(font1)

        self.infoPageDescLayout.addWidget(self.infoPageDescLabel)

        self.infoPageDescPlainTextEdit = QPlainTextEdit(self.infoPage)
        self.infoPageDescPlainTextEdit.setObjectName(u"infoPageDescPlainTextEdit")
        self.infoPageDescPlainTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.infoPageDescPlainTextEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.infoPageDescPlainTextEdit.setReadOnly(True)

        self.infoPageDescLayout.addWidget(self.infoPageDescPlainTextEdit)


        self.infoPageInputGrid.addLayout(self.infoPageDescLayout, 1, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.infoPageInputGrid)

        self.editPageVSpacer3_2 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.editPageVSpacer3_2)

        self.infoPageButtonsLayout = QHBoxLayout()
        self.infoPageButtonsLayout.setSpacing(16)
        self.infoPageButtonsLayout.setObjectName(u"infoPageButtonsLayout")
        self.infoPageHSpacer1 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.infoPageButtonsLayout.addItem(self.infoPageHSpacer1)

        self.infoPageReadyCheckBox = QCheckBox(self.infoPage)
        self.infoPageReadyCheckBox.setObjectName(u"infoPageReadyCheckBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoPageReadyCheckBox.sizePolicy().hasHeightForWidth())
        self.infoPageReadyCheckBox.setSizePolicy(sizePolicy)
        self.infoPageReadyCheckBox.setMinimumSize(QSize(100, 40))
        self.infoPageReadyCheckBox.setFont(font1)
        self.infoPageReadyCheckBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.infoPageButtonsLayout.addWidget(self.infoPageReadyCheckBox)

        self.infoPageHSpacer2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.infoPageButtonsLayout.addItem(self.infoPageHSpacer2)

        self.infoPageConfirmButton = QPushButton(self.infoPage)
        self.infoPageConfirmButton.setObjectName(u"infoPageConfirmButton")
        self.infoPageConfirmButton.setMinimumSize(QSize(150, 40))
        self.infoPageConfirmButton.setFont(font1)
        self.infoPageConfirmButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.infoPageButtonsLayout.addWidget(self.infoPageConfirmButton)

        self.infoPageEditButton = QPushButton(self.infoPage)
        self.infoPageEditButton.setObjectName(u"infoPageEditButton")
        self.infoPageEditButton.setMinimumSize(QSize(150, 40))
        self.infoPageEditButton.setFont(font1)
        self.infoPageEditButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.infoPageButtonsLayout.addWidget(self.infoPageEditButton)

        self.infoPageCancelButton = QPushButton(self.infoPage)
        self.infoPageCancelButton.setObjectName(u"infoPageCancelButton")
        self.infoPageCancelButton.setMinimumSize(QSize(150, 40))
        self.infoPageCancelButton.setFont(font1)
        self.infoPageCancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.infoPageButtonsLayout.addWidget(self.infoPageCancelButton)

        self.infoPageHSpacer3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.infoPageButtonsLayout.addItem(self.infoPageHSpacer3)

        self.infoPageHSpacer4 = QSpacerItem(130, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.infoPageButtonsLayout.addItem(self.infoPageHSpacer4)


        self.verticalLayout_6.addLayout(self.infoPageButtonsLayout)

        self.editPageVSpacer4_2 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.editPageVSpacer4_2)

        self.rightStackedWidget.addWidget(self.infoPage)
        self.addPage = QWidget()
        self.addPage.setObjectName(u"addPage")
        self.verticalLayout_9 = QVBoxLayout(self.addPage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(64, 0, 64, 0)
        self.addPageVSpacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.addPageVSpacer1)

        self.addPageLabel = QLabel(self.addPage)
        self.addPageLabel.setObjectName(u"addPageLabel")
        self.addPageLabel.setFont(font3)
        self.addPageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.addPageLabel)

        self.addPageVSpacer2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.addPageVSpacer2)

        self.addPageInputGrid = QGridLayout()
        self.addPageInputGrid.setObjectName(u"addPageInputGrid")
        self.addPageInputGrid.setHorizontalSpacing(32)
        self.addPageInputGrid.setVerticalSpacing(16)
        self.addPagePhoneLayout = QVBoxLayout()
        self.addPagePhoneLayout.setSpacing(4)
        self.addPagePhoneLayout.setObjectName(u"addPagePhoneLayout")
        self.addPagePhoneLabel = QLabel(self.addPage)
        self.addPagePhoneLabel.setObjectName(u"addPagePhoneLabel")
        self.addPagePhoneLabel.setFont(font1)

        self.addPagePhoneLayout.addWidget(self.addPagePhoneLabel)

        self.addPagePhoneLineEdit = QLineEdit(self.addPage)
        self.addPagePhoneLineEdit.setObjectName(u"addPagePhoneLineEdit")
        self.addPagePhoneLineEdit.setMinimumSize(QSize(0, 30))
        self.addPagePhoneLineEdit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.addPagePhoneLayout.addWidget(self.addPagePhoneLineEdit)


        self.addPageInputGrid.addLayout(self.addPagePhoneLayout, 0, 0, 1, 1)

        self.addPageModelLayout = QVBoxLayout()
        self.addPageModelLayout.setSpacing(4)
        self.addPageModelLayout.setObjectName(u"addPageModelLayout")
        self.addPageModelLabel = QLabel(self.addPage)
        self.addPageModelLabel.setObjectName(u"addPageModelLabel")
        self.addPageModelLabel.setFont(font1)

        self.addPageModelLayout.addWidget(self.addPageModelLabel)

        self.addPageModelLineEdit = QLineEdit(self.addPage)
        self.addPageModelLineEdit.setObjectName(u"addPageModelLineEdit")
        self.addPageModelLineEdit.setMinimumSize(QSize(0, 30))
        self.addPageModelLineEdit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.addPageModelLayout.addWidget(self.addPageModelLineEdit)


        self.addPageInputGrid.addLayout(self.addPageModelLayout, 0, 1, 1, 1)

        self.addPageForUsLayout = QVBoxLayout()
        self.addPageForUsLayout.setSpacing(4)
        self.addPageForUsLayout.setObjectName(u"addPageForUsLayout")
        self.addPageForUsLabel = QLabel(self.addPage)
        self.addPageForUsLabel.setObjectName(u"addPageForUsLabel")
        self.addPageForUsLabel.setFont(font1)

        self.addPageForUsLayout.addWidget(self.addPageForUsLabel)

        self.addPageForUsPlainTextEdit = QPlainTextEdit(self.addPage)
        self.addPageForUsPlainTextEdit.setObjectName(u"addPageForUsPlainTextEdit")
        self.addPageForUsPlainTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.addPageForUsLayout.addWidget(self.addPageForUsPlainTextEdit)


        self.addPageInputGrid.addLayout(self.addPageForUsLayout, 1, 1, 1, 1)

        self.addPageDescLayout = QVBoxLayout()
        self.addPageDescLayout.setSpacing(4)
        self.addPageDescLayout.setObjectName(u"addPageDescLayout")
        self.addPageDescLabel = QLabel(self.addPage)
        self.addPageDescLabel.setObjectName(u"addPageDescLabel")
        self.addPageDescLabel.setFont(font1)

        self.addPageDescLayout.addWidget(self.addPageDescLabel)

        self.addPageDescPlainTextEdit = QPlainTextEdit(self.addPage)
        self.addPageDescPlainTextEdit.setObjectName(u"addPageDescPlainTextEdit")
        self.addPageDescPlainTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.addPageDescLayout.addWidget(self.addPageDescPlainTextEdit)


        self.addPageInputGrid.addLayout(self.addPageDescLayout, 1, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.addPageInputGrid)

        self.addPageVSpacer3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.addPageVSpacer3)

        self.addPageButtonsLayout = QHBoxLayout()
        self.addPageButtonsLayout.setSpacing(16)
        self.addPageButtonsLayout.setObjectName(u"addPageButtonsLayout")
        self.addPageConfirmButton = QPushButton(self.addPage)
        self.addPageConfirmButton.setObjectName(u"addPageConfirmButton")
        self.addPageConfirmButton.setMinimumSize(QSize(150, 40))
        self.addPageConfirmButton.setFont(font1)
        self.addPageConfirmButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.addPageButtonsLayout.addWidget(self.addPageConfirmButton, 0, Qt.AlignmentFlag.AlignRight)

        self.addPageCancelButton = QPushButton(self.addPage)
        self.addPageCancelButton.setObjectName(u"addPageCancelButton")
        self.addPageCancelButton.setMinimumSize(QSize(150, 40))
        self.addPageCancelButton.setFont(font1)
        self.addPageCancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.addPageButtonsLayout.addWidget(self.addPageCancelButton, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_9.addLayout(self.addPageButtonsLayout)

        self.addPageVSpacer4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.addPageVSpacer4)

        self.rightStackedWidget.addWidget(self.addPage)
        self.editPage = QWidget()
        self.editPage.setObjectName(u"editPage")
        self.verticalLayout_5 = QVBoxLayout(self.editPage)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(64, 0, 64, 0)
        self.editPageVSpacer1 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.editPageVSpacer1)

        self.editPageLabel = QLabel(self.editPage)
        self.editPageLabel.setObjectName(u"editPageLabel")
        self.editPageLabel.setFont(font3)
        self.editPageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.editPageLabel)

        self.editPageVSpacer2 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.editPageVSpacer2)

        self.editPageInputGrid = QGridLayout()
        self.editPageInputGrid.setObjectName(u"editPageInputGrid")
        self.editPageInputGrid.setHorizontalSpacing(32)
        self.editPageInputGrid.setVerticalSpacing(16)
        self.editPagePhoneLayout = QVBoxLayout()
        self.editPagePhoneLayout.setSpacing(4)
        self.editPagePhoneLayout.setObjectName(u"editPagePhoneLayout")
        self.editPagePhoneLabel = QLabel(self.editPage)
        self.editPagePhoneLabel.setObjectName(u"editPagePhoneLabel")
        self.editPagePhoneLabel.setFont(font1)

        self.editPagePhoneLayout.addWidget(self.editPagePhoneLabel)

        self.editPagePhoneLineEdit = QLineEdit(self.editPage)
        self.editPagePhoneLineEdit.setObjectName(u"editPagePhoneLineEdit")
        self.editPagePhoneLineEdit.setMinimumSize(QSize(0, 30))
        self.editPagePhoneLineEdit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.editPagePhoneLayout.addWidget(self.editPagePhoneLineEdit)


        self.editPageInputGrid.addLayout(self.editPagePhoneLayout, 0, 0, 1, 1)

        self.editPageModelLayout = QVBoxLayout()
        self.editPageModelLayout.setSpacing(4)
        self.editPageModelLayout.setObjectName(u"editPageModelLayout")
        self.editPageModelLabel = QLabel(self.editPage)
        self.editPageModelLabel.setObjectName(u"editPageModelLabel")
        self.editPageModelLabel.setFont(font1)

        self.editPageModelLayout.addWidget(self.editPageModelLabel)

        self.editPageModelLineEdit = QLineEdit(self.editPage)
        self.editPageModelLineEdit.setObjectName(u"editPageModelLineEdit")
        self.editPageModelLineEdit.setMinimumSize(QSize(0, 30))
        self.editPageModelLineEdit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.editPageModelLayout.addWidget(self.editPageModelLineEdit)


        self.editPageInputGrid.addLayout(self.editPageModelLayout, 0, 1, 1, 1)

        self.editPageForUsLayout = QVBoxLayout()
        self.editPageForUsLayout.setSpacing(4)
        self.editPageForUsLayout.setObjectName(u"editPageForUsLayout")
        self.editPageForUsLabel = QLabel(self.editPage)
        self.editPageForUsLabel.setObjectName(u"editPageForUsLabel")
        self.editPageForUsLabel.setFont(font1)

        self.editPageForUsLayout.addWidget(self.editPageForUsLabel)

        self.editPageForUsPlainTextEdit = QPlainTextEdit(self.editPage)
        self.editPageForUsPlainTextEdit.setObjectName(u"editPageForUsPlainTextEdit")
        self.editPageForUsPlainTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.editPageForUsLayout.addWidget(self.editPageForUsPlainTextEdit)


        self.editPageInputGrid.addLayout(self.editPageForUsLayout, 1, 1, 1, 1)

        self.editPageDescLayout = QVBoxLayout()
        self.editPageDescLayout.setSpacing(4)
        self.editPageDescLayout.setObjectName(u"editPageDescLayout")
        self.editPageDescLabel = QLabel(self.editPage)
        self.editPageDescLabel.setObjectName(u"editPageDescLabel")
        self.editPageDescLabel.setFont(font1)

        self.editPageDescLayout.addWidget(self.editPageDescLabel)

        self.editPageDescPlainTextEdit = QPlainTextEdit(self.editPage)
        self.editPageDescPlainTextEdit.setObjectName(u"editPageDescPlainTextEdit")
        self.editPageDescPlainTextEdit.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))

        self.editPageDescLayout.addWidget(self.editPageDescPlainTextEdit)


        self.editPageInputGrid.addLayout(self.editPageDescLayout, 1, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.editPageInputGrid)

        self.editPageVSpacer3 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.editPageVSpacer3)

        self.editPageButtonsLayout = QHBoxLayout()
        self.editPageButtonsLayout.setSpacing(16)
        self.editPageButtonsLayout.setObjectName(u"editPageButtonsLayout")
        self.editPageHSpacer1 = QSpacerItem(70, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.editPageButtonsLayout.addItem(self.editPageHSpacer1)

        self.editPageReadyCheckBox = QCheckBox(self.editPage)
        self.editPageReadyCheckBox.setObjectName(u"editPageReadyCheckBox")
        sizePolicy.setHeightForWidth(self.editPageReadyCheckBox.sizePolicy().hasHeightForWidth())
        self.editPageReadyCheckBox.setSizePolicy(sizePolicy)
        self.editPageReadyCheckBox.setMinimumSize(QSize(100, 40))
        self.editPageReadyCheckBox.setFont(font1)

        self.editPageButtonsLayout.addWidget(self.editPageReadyCheckBox)

        self.editPageHSpacer2 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.editPageButtonsLayout.addItem(self.editPageHSpacer2)

        self.editPageConfirmButton = QPushButton(self.editPage)
        self.editPageConfirmButton.setObjectName(u"editPageConfirmButton")
        self.editPageConfirmButton.setMinimumSize(QSize(150, 40))
        self.editPageConfirmButton.setFont(font1)
        self.editPageConfirmButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.editPageButtonsLayout.addWidget(self.editPageConfirmButton)

        self.editPageCancelButton = QPushButton(self.editPage)
        self.editPageCancelButton.setObjectName(u"editPageCancelButton")
        self.editPageCancelButton.setMinimumSize(QSize(150, 40))
        self.editPageCancelButton.setFont(font1)
        self.editPageCancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.editPageButtonsLayout.addWidget(self.editPageCancelButton)

        self.editPageHSpacer3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.editPageButtonsLayout.addItem(self.editPageHSpacer3)

        self.editPageHSpacer4 = QSpacerItem(186, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.editPageButtonsLayout.addItem(self.editPageHSpacer4)


        self.verticalLayout_5.addLayout(self.editPageButtonsLayout)

        self.editPageVSpacer4 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.editPageVSpacer4)

        self.rightStackedWidget.addWidget(self.editPage)

        self.horizontalLayout_7.addWidget(self.rightStackedWidget)

        self.settingsFrame = QFrame(self.rightContentSection)
        self.settingsFrame.setObjectName(u"settingsFrame")
        self.settingsFrame.setMinimumSize(QSize(0, 0))
        self.settingsFrame.setMaximumSize(QSize(0, 16777215))
        self.settingsFrame.setFont(font1)
        self.settingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.settingsFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.excelPreviewButton = QPushButton(self.settingsFrame)
        self.excelPreviewButton.setObjectName(u"excelPreviewButton")
        self.excelPreviewButton.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setPointSize(11)
        self.excelPreviewButton.setFont(font4)
        self.excelPreviewButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.excelPreviewButton)

        self.darkModeCheckBox = QCheckBox(self.settingsFrame)
        self.darkModeCheckBox.setObjectName(u"darkModeCheckBox")
        self.darkModeCheckBox.setMinimumSize(QSize(0, 40))
        self.darkModeCheckBox.setFont(font4)
        self.darkModeCheckBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.darkModeCheckBox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.settingsVSpacer = QSpacerItem(20, 518, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.settingsVSpacer)


        self.horizontalLayout_7.addWidget(self.settingsFrame)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.creditsFrame = QFrame(self.rightContentSection)
        self.creditsFrame.setObjectName(u"creditsFrame")
        self.creditsFrame.setMaximumSize(QSize(16777215, 30))
        self.creditsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.creditsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.creditsFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 3, 9, 3)
        self.creditsByLabel = QLabel(self.creditsFrame)
        self.creditsByLabel.setObjectName(u"creditsByLabel")

        self.horizontalLayout_3.addWidget(self.creditsByLabel)


        self.verticalLayout.addWidget(self.creditsFrame)


        self.horizontalLayout.addWidget(self.rightContentSection)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.rightStackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Szukaj", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"6", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.btnHome.setText("")
        self.topMenuLogo.setText("")
        self.topMenuLabel.setText(QCoreApplication.translate("MainWindow", u"Serwis komputerowy", None))
        self.settingsButton.setText("")
        self.btnMin.setText("")
        self.btnMax.setText("")
        self.btnClose.setText("")
        self.infoPageLabel.setText(QCoreApplication.translate("MainWindow", u"Zlecenie nr. 3", None))
        self.infoPagePhoneLabel.setText(QCoreApplication.translate("MainWindow", u"Nr. tel", None))
        self.infoPageModelLabel.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.infoPageForUsLabel.setText(QCoreApplication.translate("MainWindow", u"Dla nas", None))
        self.infoPageDescLabel.setText(QCoreApplication.translate("MainWindow", u"Opis", None))
        self.infoPageReadyCheckBox.setText(QCoreApplication.translate("MainWindow", u"Gotowe", None))
        self.infoPageConfirmButton.setText(QCoreApplication.translate("MainWindow", u"Drukuj", None))
        self.infoPageEditButton.setText(QCoreApplication.translate("MainWindow", u"Edytuj", None))
        self.infoPageCancelButton.setText(QCoreApplication.translate("MainWindow", u"Anuluj", None))
        self.addPageLabel.setText(QCoreApplication.translate("MainWindow", u"Dodawanie zlecenia nr. 3", None))
        self.addPagePhoneLabel.setText(QCoreApplication.translate("MainWindow", u"Nr. tel", None))
        self.addPageModelLabel.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.addPageForUsLabel.setText(QCoreApplication.translate("MainWindow", u"Dla nas", None))
        self.addPageDescLabel.setText(QCoreApplication.translate("MainWindow", u"Opis", None))
        self.addPageConfirmButton.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.addPageCancelButton.setText(QCoreApplication.translate("MainWindow", u"Anuluj", None))
        self.editPageLabel.setText(QCoreApplication.translate("MainWindow", u"Edytowanie zlecenia nr. 3", None))
        self.editPagePhoneLabel.setText(QCoreApplication.translate("MainWindow", u"Nr. tel", None))
        self.editPageModelLabel.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.editPageForUsLabel.setText(QCoreApplication.translate("MainWindow", u"Dla nas", None))
        self.editPageDescLabel.setText(QCoreApplication.translate("MainWindow", u"Opis", None))
        self.editPageReadyCheckBox.setText(QCoreApplication.translate("MainWindow", u"Gotowe", None))
        self.editPageConfirmButton.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.editPageCancelButton.setText(QCoreApplication.translate("MainWindow", u"Anuluj", None))
        self.excelPreviewButton.setText(QCoreApplication.translate("MainWindow", u"Podgl\u0105d Excela", None))
        self.darkModeCheckBox.setText(QCoreApplication.translate("MainWindow", u"Dark mode", None))
        self.creditsByLabel.setText(QCoreApplication.translate("MainWindow", u"By: Krystian Figiela", None))
    # retranslateUi

