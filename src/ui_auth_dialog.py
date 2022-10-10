# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AuthDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_dlgAuth(object):
    def setupUi(self, dlgAuth):
        if not dlgAuth.objectName():
            dlgAuth.setObjectName(u"dlgAuth")
        dlgAuth.resize(429, 300)
        self.buttonBox = QDialogButtonBox(dlgAuth)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(dlgAuth)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 401, 121))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.accessToken = QLabel(self.layoutWidget)
        self.accessToken.setObjectName(u"accessToken")

        self.horizontalLayout.addWidget(self.accessToken)

        self.lnEdtAccessToken = QLineEdit(self.layoutWidget)
        self.lnEdtAccessToken.setObjectName(u"lnEdtAccessToken")

        self.horizontalLayout.addWidget(self.lnEdtAccessToken)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(dlgAuth)
        self.buttonBox.accepted.connect(dlgAuth.accept)
        self.buttonBox.rejected.connect(dlgAuth.reject)

        QMetaObject.connectSlotsByName(dlgAuth)
    # setupUi

    def retranslateUi(self, dlgAuth):
        dlgAuth.setWindowTitle(QCoreApplication.translate("dlgAuth", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.accessToken.setText(QCoreApplication.translate("dlgAuth", u"\u0422\u043e\u043a\u0435\u043d \u0434\u043e\u0441\u0442\u0443\u043f\u0430:", None))
    # retranslateUi

