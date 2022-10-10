# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 358)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 761, 331))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblSearch = QLabel(self.layoutWidget)
        self.lblSearch.setObjectName(u"lblSearch")

        self.horizontalLayout.addWidget(self.lblSearch)

        self.lnEdtSearch = QLineEdit(self.layoutWidget)
        self.lnEdtSearch.setObjectName(u"lnEdtSearch")

        self.horizontalLayout.addWidget(self.lnEdtSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblWdgt = QTableWidget(self.layoutWidget)
        self.tblWdgt.setObjectName(u"tblWdgt")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblWdgt.sizePolicy().hasHeightForWidth())
        self.tblWdgt.setSizePolicy(sizePolicy)
        self.tblWdgt.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tblWdgt.setRowCount(0)
        self.tblWdgt.setColumnCount(0)
        self.tblWdgt.horizontalHeader().setCascadingSectionResizes(False)
        self.tblWdgt.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tblWdgt)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnDownload = QPushButton(self.layoutWidget)
        self.btnDownload.setObjectName(u"btnDownload")

        self.horizontalLayout_2.addWidget(self.btnDownload)

        self.btnRename = QPushButton(self.layoutWidget)
        self.btnRename.setObjectName(u"btnRename")

        self.horizontalLayout_2.addWidget(self.btnRename)

        self.btnAdd = QPushButton(self.layoutWidget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout_2.addWidget(self.btnAdd)

        self.btnLoad = QPushButton(self.layoutWidget)
        self.btnLoad.setObjectName(u"btnLoad")

        self.horizontalLayout_2.addWidget(self.btnLoad)

        self.btnAuth = QPushButton(self.layoutWidget)
        self.btnAuth.setObjectName(u"btnAuth")

        self.horizontalLayout_2.addWidget(self.btnAuth)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"vkDocuments", None))
        self.lblSearch.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btnDownload.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.btnRename.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u0442\u044c", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b \u0438 \u043f\u0430\u043f\u043a\u0438", None))
        self.btnLoad.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.btnAuth.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
    # retranslateUi

