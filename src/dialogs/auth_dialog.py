# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AuthDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QRect, Qt
from PySide6.QtWidgets import (QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy, QPushButton,
    QVBoxLayout, QWidget, QMessageBox)

from services.vk_service import VkService
import webbrowser
import config


class AuthDialog(QDialog):
    def __init__(self, parent=None):
        super(AuthDialog, self).__init__(parent=parent)

        self.setObjectName("authDialog")
        self.resize(429, 300)
        # self.buttonBox = QDialogButtonBox(self)
        # self.buttonBox.setObjectName("buttonBox")
        # self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        # self.buttonBox.setOrientation(Qt.Horizontal)
        # self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 401, 121))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accessToken = QLabel(self.layoutWidget)
        self.accessToken.setObjectName("accessToken")

        self.horizontalLayout.addWidget(self.accessToken)

        self.login_button = QPushButton(self)
        self.login_button.setText("Войти")
        self.login_button.clicked.connect(self.login_button_clicked)
        self.verticalLayout.addWidget(self.login_button)

        self.auth_button = QPushButton(self)
        self.auth_button.setText("Авторизоваться")
        self.auth_button.clicked.connect(self.auth_button_clicked)
        self.verticalLayout.addWidget(self.auth_button)

        self.access_token_edit = QLineEdit(self.layoutWidget)
        self.access_token_edit.setObjectName("access_token_edit")

        self.horizontalLayout.addWidget(self.access_token_edit)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()

        self.successful = False

        self.vk_service = VkService()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("authDialog", "Авторизация", None))
        self.accessToken.setText(QCoreApplication.translate("authDialog", "Токен доступа:", None))

    def login_button_clicked(self):
        try:
            if self.access_token_edit != "":
                # self.vk_service.auth(self.access_token_edit.text())
                vk_url = self.access_token_edit.text()

                self.successful = True
                sub1 = "access_token"
                sub2 = "&expires_in"

                idx1 = vk_url.index(sub1)
                idx2 = vk_url.index(sub2)

                token = ''

                for idx in range(idx1 + len(sub1) + 1, idx2):
                    token = token + vk_url[idx]

                self.token = token
                self.close()
        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setInformativeText("Неверная ссылка!")
            msg_box.setWindowTitle("Ошибка")
            msg_box.exec()

    def auth_button_clicked(self):
        webbrowser.open(config.URL)
