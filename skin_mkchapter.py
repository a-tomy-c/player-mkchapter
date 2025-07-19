# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skin_mkchapter.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_PlayerMakeChapter(object):
    def setupUi(self, PlayerMakeChapter):
        if not PlayerMakeChapter.objectName():
            PlayerMakeChapter.setObjectName(u"PlayerMakeChapter")
        PlayerMakeChapter.resize(733, 522)
        self.verticalLayout_2 = QVBoxLayout(PlayerMakeChapter)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter_v = QSplitter(PlayerMakeChapter)
        self.splitter_v.setObjectName(u"splitter_v")
        self.splitter_v.setLineWidth(0)
        self.splitter_v.setOrientation(Qt.Orientation.Vertical)
        self.splitter_h = QSplitter(self.splitter_v)
        self.splitter_h.setObjectName(u"splitter_h")
        self.splitter_h.setLineWidth(0)
        self.splitter_h.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget = QWidget(self.splitter_h)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fm_top = QFrame(self.layoutWidget)
        self.fm_top.setObjectName(u"fm_top")
        self.fm_top.setMaximumSize(QSize(16777215, 30))
        self.fm_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.fm_top.setFrameShadow(QFrame.Shadow.Plain)
        self.fm_top.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.fm_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_time = QLabel(self.fm_top)
        self.lb_time.setObjectName(u"lb_time")
        font = QFont()
        font.setFamilies([u"Liberation Mono"])
        font.setPointSize(18)
        self.lb_time.setFont(font)

        self.horizontalLayout.addWidget(self.lb_time)

        self.bt_backward = QPushButton(self.fm_top)
        self.bt_backward.setObjectName(u"bt_backward")
        self.bt_backward.setMinimumSize(QSize(40, 0))
        self.bt_backward.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.bt_backward)

        self.bt_fordward = QPushButton(self.fm_top)
        self.bt_fordward.setObjectName(u"bt_fordward")
        self.bt_fordward.setMinimumSize(QSize(40, 0))
        self.bt_fordward.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.bt_fordward)

        self.bt_capture = QPushButton(self.fm_top)
        self.bt_capture.setObjectName(u"bt_capture")
        self.bt_capture.setMinimumSize(QSize(40, 0))
        self.bt_capture.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.bt_capture)

        self.horizontalSpacer = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_add = QPushButton(self.fm_top)
        self.bt_add.setObjectName(u"bt_add")
        self.bt_add.setMinimumSize(QSize(50, 0))
        self.bt_add.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.bt_add)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.fm_top)

        self.fm_player = QFrame(self.layoutWidget)
        self.fm_player.setObjectName(u"fm_player")
        self.fm_player.setFrameShape(QFrame.Shape.StyledPanel)
        self.fm_player.setFrameShadow(QFrame.Shadow.Plain)
        self.fm_player.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.fm_player)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.vly_player = QVBoxLayout()
        self.vly_player.setSpacing(0)
        self.vly_player.setObjectName(u"vly_player")

        self.verticalLayout_3.addLayout(self.vly_player)


        self.verticalLayout.addWidget(self.fm_player)

        self.splitter_h.addWidget(self.layoutWidget)
        self.fm_chapters = QFrame(self.splitter_h)
        self.fm_chapters.setObjectName(u"fm_chapters")
        self.fm_chapters.setFrameShape(QFrame.Shape.StyledPanel)
        self.fm_chapters.setFrameShadow(QFrame.Shadow.Plain)
        self.fm_chapters.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.fm_chapters)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tb_chapters = QTableWidget(self.fm_chapters)
        self.tb_chapters.setObjectName(u"tb_chapters")
        self.tb_chapters.setFrameShadow(QFrame.Shadow.Plain)
        self.tb_chapters.setLineWidth(0)

        self.verticalLayout_4.addWidget(self.tb_chapters)

        self.splitter_h.addWidget(self.fm_chapters)
        self.splitter_v.addWidget(self.splitter_h)
        self.sw_info = QStackedWidget(self.splitter_v)
        self.sw_info.setObjectName(u"sw_info")
        self.sw_info.setLineWidth(0)
        self.pag1 = QWidget()
        self.pag1.setObjectName(u"pag1")
        self.horizontalLayout_4 = QHBoxLayout(self.pag1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_bot = QSplitter(self.pag1)
        self.splitter_bot.setObjectName(u"splitter_bot")
        self.splitter_bot.setOrientation(Qt.Orientation.Horizontal)
        self.tex = QTextEdit(self.splitter_bot)
        self.tex.setObjectName(u"tex")
        self.splitter_bot.addWidget(self.tex)
        self.lb_capture = QLabel(self.splitter_bot)
        self.lb_capture.setObjectName(u"lb_capture")
        self.splitter_bot.addWidget(self.lb_capture)

        self.horizontalLayout_4.addWidget(self.splitter_bot)

        self.sw_info.addWidget(self.pag1)
        self.pag2 = QWidget()
        self.pag2.setObjectName(u"pag2")
        self.horizontalLayout_3 = QHBoxLayout(self.pag2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sw_info.addWidget(self.pag2)
        self.splitter_v.addWidget(self.sw_info)

        self.verticalLayout_2.addWidget(self.splitter_v)


        self.retranslateUi(PlayerMakeChapter)

        QMetaObject.connectSlotsByName(PlayerMakeChapter)
    # setupUi

    def retranslateUi(self, PlayerMakeChapter):
        PlayerMakeChapter.setWindowTitle(QCoreApplication.translate("PlayerMakeChapter", u"Form", None))
        self.lb_time.setText(QCoreApplication.translate("PlayerMakeChapter", u"00:00:00.000", None))
        self.bt_backward.setText(QCoreApplication.translate("PlayerMakeChapter", u"-", None))
        self.bt_fordward.setText(QCoreApplication.translate("PlayerMakeChapter", u"+", None))
        self.bt_capture.setText(QCoreApplication.translate("PlayerMakeChapter", u"C", None))
        self.bt_add.setText(QCoreApplication.translate("PlayerMakeChapter", u"ADD", None))
        self.lb_capture.setText("")
    # retranslateUi

