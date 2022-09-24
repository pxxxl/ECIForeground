# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLCDNumber, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QStatusBar, QTextBrowser, QTextEdit,
    QTreeView, QVBoxLayout, QWidget)

from circuit_board.circuit_board import ECIBoard
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(538, 460)
        icon = QIcon()
        icon.addFile(u":/window_icon/icons/Final.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.act_save = QAction(MainWindow)
        self.act_save.setObjectName(u"act_save")
        self.act_saveas = QAction(MainWindow)
        self.act_saveas.setObjectName(u"act_saveas")
        self.act_open_file = QAction(MainWindow)
        self.act_open_file.setObjectName(u"act_open_file")
        self.act_open_folder = QAction(MainWindow)
        self.act_open_folder.setObjectName(u"act_open_folder")
        self.act_close_folder = QAction(MainWindow)
        self.act_close_folder.setObjectName(u"act_close_folder")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton#edit_tab{\n"
"background-color: transparent;\n"
"border: 0px;\n"
"margin:5\n"
"\n"
"}\n"
"\n"
"QPushButton#folder_tab{\n"
"background-color: transparent;\n"
"border: 0px;\n"
"margin:5\n"
"\n"
"}\n"
" QPushButton#solve_tab{\n"
"background-color: transparent;\n"
"border: 0px;\n"
"margin:5\n"
"\n"
"}\n"
"QPushButton#notes_tab{\n"
"background-color: transparent;\n"
"border: 0px;\n"
"margin:5\n"
"\n"
"}\n"
"QPushButton#report_tab {\n"
"background-color: transparent;\n"
"border: 0px;\n"
"margin:5\n"
"\n"
"}\n"
"\n"
"/*\n"
"QPushButton#edit_tab:hover{\n"
"background-color: rgba(173, 173, 173, 50);\n"
"border: 0px;\n"
"margin:5\n"
"\n"
"}\n"
"QPushButton#folder_tab:hover{\n"
"background-color: rgba(173, 173, 173, 50);\n"
"border: 0px;\n"
"margin:5\n"
"}\n"
" QPushButton#solve_tab:hover{\n"
"background-color: rgba(173, 173, 173, 50);\n"
"border: 0px;\n"
"margin:5\n"
"}\n"
"QPushButton#notes_tab:hover{\n"
"background-color: rgba(173, 173, 173, 50);\n"
"border: 0px;\n"
"margin:5\n"
"}\n"
"QPushButton#report_t"
                        "ab:hover {\n"
"background-color: rgba(173, 173, 173, 50);\n"
"border: 0px;\n"
"margin:5\n"
"}\n"
"*/")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_layout = QVBoxLayout()
        self.left_side_layout.setSpacing(0)
        self.left_side_layout.setObjectName(u"left_side_layout")
        self.left_side_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.folder_tab = QPushButton(self.centralwidget)
        self.folder_tab.setObjectName(u"folder_tab")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folder_tab.sizePolicy().hasHeightForWidth())
        self.folder_tab.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.folder_tab.setPalette(palette)
        self.folder_tab.setAutoFillBackground(False)
        self.folder_tab.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/tab_button/folder", QSize(), QIcon.Normal, QIcon.Off)
        self.folder_tab.setIcon(icon1)
        self.folder_tab.setIconSize(QSize(36, 36))
        self.folder_tab.setCheckable(True)

        self.left_side_layout.addWidget(self.folder_tab)

        self.edit_tab = QPushButton(self.centralwidget)
        self.edit_tab.setObjectName(u"edit_tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.edit_tab.sizePolicy().hasHeightForWidth())
        self.edit_tab.setSizePolicy(sizePolicy1)
        self.edit_tab.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/tab_button/edit", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_tab.setIcon(icon2)
        self.edit_tab.setIconSize(QSize(36, 36))
        self.edit_tab.setCheckable(True)

        self.left_side_layout.addWidget(self.edit_tab)

        self.solve_tab = QPushButton(self.centralwidget)
        self.solve_tab.setObjectName(u"solve_tab")
        sizePolicy.setHeightForWidth(self.solve_tab.sizePolicy().hasHeightForWidth())
        self.solve_tab.setSizePolicy(sizePolicy)
        self.solve_tab.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/tab_button/solve", QSize(), QIcon.Normal, QIcon.Off)
        self.solve_tab.setIcon(icon3)
        self.solve_tab.setIconSize(QSize(36, 36))
        self.solve_tab.setCheckable(True)

        self.left_side_layout.addWidget(self.solve_tab)

        self.notes_tab = QPushButton(self.centralwidget)
        self.notes_tab.setObjectName(u"notes_tab")
        sizePolicy.setHeightForWidth(self.notes_tab.sizePolicy().hasHeightForWidth())
        self.notes_tab.setSizePolicy(sizePolicy)
        self.notes_tab.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/tab_button/note", QSize(), QIcon.Normal, QIcon.Off)
        self.notes_tab.setIcon(icon4)
        self.notes_tab.setIconSize(QSize(36, 36))
        self.notes_tab.setCheckable(True)

        self.left_side_layout.addWidget(self.notes_tab)

        self.report_tab = QPushButton(self.centralwidget)
        self.report_tab.setObjectName(u"report_tab")
        sizePolicy.setHeightForWidth(self.report_tab.sizePolicy().hasHeightForWidth())
        self.report_tab.setSizePolicy(sizePolicy)
        self.report_tab.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/tab_button/report", QSize(), QIcon.Normal, QIcon.Off)
        self.report_tab.setIcon(icon5)
        self.report_tab.setIconSize(QSize(36, 36))
        self.report_tab.setCheckable(True)

        self.left_side_layout.addWidget(self.report_tab)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)

        self.left_side_layout.addWidget(self.widget)


        self.horizontalLayout.addLayout(self.left_side_layout)

        self.left_page = QStackedWidget(self.centralwidget)
        self.left_page.setObjectName(u"left_page")
        self.folder_page = QWidget()
        self.folder_page.setObjectName(u"folder_page")
        self.horizontalLayout_4 = QHBoxLayout(self.folder_page)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_2 = QPushButton(self.folder_page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.folder_page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_8.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.folder_page)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_8.addWidget(self.pushButton_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.folder_view = QTreeView(self.folder_page)
        self.folder_view.setObjectName(u"folder_view")

        self.verticalLayout_4.addWidget(self.folder_view)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.left_page.addWidget(self.folder_page)
        self.edit_page = QWidget()
        self.edit_page.setObjectName(u"edit_page")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.edit_page.sizePolicy().hasHeightForWidth())
        self.edit_page.setSizePolicy(sizePolicy3)
        self.edit_page.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.edit_page)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.edit_button_layout = QHBoxLayout()
        self.edit_button_layout.setSpacing(0)
        self.edit_button_layout.setObjectName(u"edit_button_layout")
        self.choose_button = QPushButton(self.edit_page)
        self.choose_button.setObjectName(u"choose_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.choose_button.sizePolicy().hasHeightForWidth())
        self.choose_button.setSizePolicy(sizePolicy4)
        icon6 = QIcon()
        icon6.addFile(u":/edit_button/choose_c", QSize(), QIcon.Normal, QIcon.Off)
        self.choose_button.setIcon(icon6)
        self.choose_button.setIconSize(QSize(24, 24))
        self.choose_button.setCheckable(True)
        self.choose_button.setChecked(True)

        self.edit_button_layout.addWidget(self.choose_button)

        self.add_button = QPushButton(self.edit_page)
        self.add_button.setObjectName(u"add_button")
        sizePolicy4.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy4)
        icon7 = QIcon()
        icon7.addFile(u":/edit_button/add", QSize(), QIcon.Normal, QIcon.Off)
        self.add_button.setIcon(icon7)
        self.add_button.setIconSize(QSize(24, 24))
        self.add_button.setCheckable(True)

        self.edit_button_layout.addWidget(self.add_button)

        self.rotate_button = QPushButton(self.edit_page)
        self.rotate_button.setObjectName(u"rotate_button")
        sizePolicy4.setHeightForWidth(self.rotate_button.sizePolicy().hasHeightForWidth())
        self.rotate_button.setSizePolicy(sizePolicy4)
        icon8 = QIcon()
        icon8.addFile(u":/edit_button/rotate", QSize(), QIcon.Normal, QIcon.Off)
        self.rotate_button.setIcon(icon8)
        self.rotate_button.setIconSize(QSize(24, 24))
        self.rotate_button.setCheckable(True)

        self.edit_button_layout.addWidget(self.rotate_button)

        self.delete_button = QPushButton(self.edit_page)
        self.delete_button.setObjectName(u"delete_button")
        sizePolicy4.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy4)
        icon9 = QIcon()
        icon9.addFile(u":/edit_button/delete", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon9)
        self.delete_button.setIconSize(QSize(24, 24))
        self.delete_button.setCheckable(True)

        self.edit_button_layout.addWidget(self.delete_button)

        self.link_button = QPushButton(self.edit_page)
        self.link_button.setObjectName(u"link_button")
        sizePolicy4.setHeightForWidth(self.link_button.sizePolicy().hasHeightForWidth())
        self.link_button.setSizePolicy(sizePolicy4)
        icon10 = QIcon()
        icon10.addFile(u":/edit_button/link", QSize(), QIcon.Normal, QIcon.Off)
        self.link_button.setIcon(icon10)
        self.link_button.setIconSize(QSize(24, 24))
        self.link_button.setCheckable(True)

        self.edit_button_layout.addWidget(self.link_button)

        self.unlink_button = QPushButton(self.edit_page)
        self.unlink_button.setObjectName(u"unlink_button")
        sizePolicy4.setHeightForWidth(self.unlink_button.sizePolicy().hasHeightForWidth())
        self.unlink_button.setSizePolicy(sizePolicy4)
        icon11 = QIcon()
        icon11.addFile(u":/edit_button/unlink", QSize(), QIcon.Normal, QIcon.Off)
        self.unlink_button.setIcon(icon11)
        self.unlink_button.setIconSize(QSize(24, 24))
        self.unlink_button.setCheckable(True)

        self.edit_button_layout.addWidget(self.unlink_button)

        self.widget_2 = QWidget(self.edit_page)
        self.widget_2.setObjectName(u"widget_2")

        self.edit_button_layout.addWidget(self.widget_2)


        self.verticalLayout.addLayout(self.edit_button_layout)

        self.scrollArea = QScrollArea(self.edit_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 254, 373))
        self.scrollAreaWidgetContents.setStyleSheet(u"QPushButton{\n"
"	Text-align:left	\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	Text-align:left	\n"
"	background:white\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.choose_node = QPushButton(self.scrollAreaWidgetContents)
        self.choose_node.setObjectName(u"choose_node")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.choose_node.sizePolicy().hasHeightForWidth())
        self.choose_node.setSizePolicy(sizePolicy5)
        font = QFont()
        font.setPointSize(12)
        self.choose_node.setFont(font)
        icon12 = QIcon()
        icon12.addFile(u":/elems/icons/Node.png", QSize(), QIcon.Normal, QIcon.Off)
        self.choose_node.setIcon(icon12)
        self.choose_node.setIconSize(QSize(32, 32))
        self.choose_node.setCheckable(True)
        self.choose_node.setChecked(True)

        self.verticalLayout_6.addWidget(self.choose_node)

        self.choose_resistor = QPushButton(self.scrollAreaWidgetContents)
        self.choose_resistor.setObjectName(u"choose_resistor")
        sizePolicy5.setHeightForWidth(self.choose_resistor.sizePolicy().hasHeightForWidth())
        self.choose_resistor.setSizePolicy(sizePolicy5)
        self.choose_resistor.setFont(font)
        icon13 = QIcon()
        icon13.addFile(u":/elems/icons/Resistance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.choose_resistor.setIcon(icon13)
        self.choose_resistor.setIconSize(QSize(32, 32))
        self.choose_resistor.setCheckable(True)

        self.verticalLayout_6.addWidget(self.choose_resistor)

        self.choose_capacitor = QPushButton(self.scrollAreaWidgetContents)
        self.choose_capacitor.setObjectName(u"choose_capacitor")
        sizePolicy5.setHeightForWidth(self.choose_capacitor.sizePolicy().hasHeightForWidth())
        self.choose_capacitor.setSizePolicy(sizePolicy5)
        self.choose_capacitor.setFont(font)
        icon14 = QIcon()
        icon14.addFile(u":/elems/icons/Capacity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.choose_capacitor.setIcon(icon14)
        self.choose_capacitor.setIconSize(QSize(32, 32))
        self.choose_capacitor.setCheckable(True)

        self.verticalLayout_6.addWidget(self.choose_capacitor)

        self.choose_intuctor = QPushButton(self.scrollAreaWidgetContents)
        self.choose_intuctor.setObjectName(u"choose_intuctor")
        sizePolicy5.setHeightForWidth(self.choose_intuctor.sizePolicy().hasHeightForWidth())
        self.choose_intuctor.setSizePolicy(sizePolicy5)
        self.choose_intuctor.setFont(font)
        self.choose_intuctor.setIcon(icon13)
        self.choose_intuctor.setIconSize(QSize(32, 32))
        self.choose_intuctor.setCheckable(True)

        self.verticalLayout_6.addWidget(self.choose_intuctor)

        self.choose_vs = QPushButton(self.scrollAreaWidgetContents)
        self.choose_vs.setObjectName(u"choose_vs")
        sizePolicy5.setHeightForWidth(self.choose_vs.sizePolicy().hasHeightForWidth())
        self.choose_vs.setSizePolicy(sizePolicy5)
        self.choose_vs.setFont(font)
        icon15 = QIcon()
        icon15.addFile(u":/elems/icons/VoltageSource.png", QSize(), QIcon.Normal, QIcon.Off)
        self.choose_vs.setIcon(icon15)
        self.choose_vs.setIconSize(QSize(32, 32))
        self.choose_vs.setCheckable(True)

        self.verticalLayout_6.addWidget(self.choose_vs)

        self.choose_cvs = QPushButton(self.scrollAreaWidgetContents)
        self.choose_cvs.setObjectName(u"choose_cvs")
        sizePolicy5.setHeightForWidth(self.choose_cvs.sizePolicy().hasHeightForWidth())
        self.choose_cvs.setSizePolicy(sizePolicy5)
        self.choose_cvs.setFont(font)
        icon16 = QIcon()
        icon16.addFile(u":/elems/icons/CVoltageSource.png", QSize(), QIcon.Normal, QIcon.Off)
        self.choose_cvs.setIcon(icon16)
        self.choose_cvs.setIconSize(QSize(32, 32))
        self.choose_cvs.setCheckable(True)

        self.verticalLayout_6.addWidget(self.choose_cvs)

        self.choose_cs = QPushButton(self.scrollAreaWidgetContents)
        self.choose_cs.setObjectName(u"choose_cs")
        sizePolicy5.setHeightForWidth(self.choose_cs.sizePolicy().hasHeightForWidth())
        self.choose_cs.setSizePolicy(sizePolicy5)
        self.choose_cs.setFont(font)
        icon17 = QIcon()
        icon17.addFile(u":/elems/icons/CurrentSource.png", QSize(), QIcon.Normal, QIcon.Off)
        self.choose_cs.setIcon(icon17)
        self.choose_cs.setIconSize(QSize(32, 32))
        self.choose_cs.setCheckable(True)

        self.verticalLayout_6.addWidget(self.choose_cs)

        self.choose_ccs = QPushButton(self.scrollAreaWidgetContents)
        self.choose_ccs.setObjectName(u"choose_ccs")
        sizePolicy5.setHeightForWidth(self.choose_ccs.sizePolicy().hasHeightForWidth())
        self.choose_ccs.setSizePolicy(sizePolicy5)
        self.choose_ccs.setFont(font)
        icon18 = QIcon()
        icon18.addFile(u":/elems/icons/CCurrentSource.png", QSize(), QIcon.Normal, QIcon.Off)
        self.choose_ccs.setIcon(icon18)
        self.choose_ccs.setIconSize(QSize(32, 32))
        self.choose_ccs.setCheckable(True)

        self.verticalLayout_6.addWidget(self.choose_ccs)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_6.addWidget(self.widget_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.left_page.addWidget(self.edit_page)
        self.solve_page = QWidget()
        self.solve_page.setObjectName(u"solve_page")
        self.horizontalLayout_7 = QHBoxLayout(self.solve_page)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.solve_page)
        self.pushButton.setObjectName(u"pushButton")
        icon19 = QIcon()
        icon19.addFile(u":/page_button/icons/debug.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon19)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.comboBox = QComboBox(self.solve_page)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalLayout_2.setStretch(1, 6)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.lcdNumber = QLCDNumber(self.solve_page)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy5.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy5)

        self.verticalLayout_2.addWidget(self.lcdNumber)

        self.widget_4 = QWidget(self.solve_page)
        self.widget_4.setObjectName(u"widget_4")

        self.verticalLayout_2.addWidget(self.widget_4)

        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 10)

        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.left_page.addWidget(self.solve_page)
        self.notes_page = QWidget()
        self.notes_page.setObjectName(u"notes_page")
        self.horizontalLayout_5 = QHBoxLayout(self.notes_page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit = QTextEdit(self.notes_page)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.textEdit.setFont(font1)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.left_page.addWidget(self.notes_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.horizontalLayout_6 = QHBoxLayout(self.report_page)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textBrowser = QTextBrowser(self.report_page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFont(font1)

        self.verticalLayout_5.addWidget(self.textBrowser)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.left_page.addWidget(self.report_page)

        self.horizontalLayout.addWidget(self.left_page)

        self.board = ECIBoard(self.centralwidget)
        self.board.setObjectName(u"board")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.board.sizePolicy().hasHeightForWidth())
        self.board.setSizePolicy(sizePolicy6)
        self.board.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.board)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 10000)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 538, 23))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.menubar.setFont(font2)
        self.file_menu = QMenu(self.menubar)
        self.file_menu.setObjectName(u"file_menu")
        self.edit_menu = QMenu(self.menubar)
        self.edit_menu.setObjectName(u"edit_menu")
        self.solve_menu = QMenu(self.menubar)
        self.solve_menu.setObjectName(u"solve_menu")
        self.sight_menu = QMenu(self.menubar)
        self.sight_menu.setObjectName(u"sight_menu")
        self.setting_menu = QMenu(self.menubar)
        self.setting_menu.setObjectName(u"setting_menu")
        self.window_menu = QMenu(self.menubar)
        self.window_menu.setObjectName(u"window_menu")
        self.help_menu = QMenu(self.menubar)
        self.help_menu.setObjectName(u"help_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.solve_menu.menuAction())
        self.menubar.addAction(self.edit_menu.menuAction())
        self.menubar.addAction(self.sight_menu.menuAction())
        self.menubar.addAction(self.window_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())
        self.menubar.addAction(self.setting_menu.menuAction())
        self.file_menu.addAction(self.act_save)
        self.file_menu.addAction(self.act_saveas)
        self.file_menu.addAction(self.act_open_file)
        self.file_menu.addAction(self.act_open_folder)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.act_close_folder)

        self.retranslateUi(MainWindow)

        self.left_page.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.act_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(tooltip)
        self.act_save.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.act_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.act_saveas.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
#if QT_CONFIG(tooltip)
        self.act_saveas.setToolTip(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
#endif // QT_CONFIG(tooltip)
        self.act_open_file.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.act_open_file.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.act_open_file.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.act_open_folder.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
#if QT_CONFIG(tooltip)
        self.act_open_folder.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.act_close_folder.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6587\u4ef6\u5939", None))
#if QT_CONFIG(tooltip)
        self.act_close_folder.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.folder_tab.setText("")
        self.edit_tab.setText("")
        self.solve_tab.setText("")
        self.notes_tab.setText("")
        self.report_tab.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.choose_button.setText("")
        self.add_button.setText("")
        self.rotate_button.setText("")
        self.delete_button.setText("")
        self.link_button.setText("")
        self.unlink_button.setText("")
        self.choose_node.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b9", None))
        self.choose_resistor.setText(QCoreApplication.translate("MainWindow", u"\u7535\u963b", None))
        self.choose_capacitor.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5bb9", None))
        self.choose_intuctor.setText(QCoreApplication.translate("MainWindow", u"\u7535\u611f", None))
        self.choose_vs.setText(QCoreApplication.translate("MainWindow", u"\u7535\u538b\u6e90", None))
        self.choose_cvs.setText(QCoreApplication.translate("MainWindow", u"\u7535\u538b\u6e90", None))
        self.choose_cs.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6d41\u6e90", None))
        self.choose_ccs.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6d41\u6e90", None))
        self.pushButton.setText("")
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.edit_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6c42\u89e3", None))
        self.solve_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.sight_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.setting_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.window_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.help_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3", None))
    # retranslateUi

