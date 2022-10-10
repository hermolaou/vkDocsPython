# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from business_logic.business_logic import BusinessLogic
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,)
from PySide6.QtWidgets import (QMainWindow, QAbstractScrollArea, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QCheckBox, QWidget)

from dialogs.auth_dialog import AuthDialog
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        auth_dialog = AuthDialog()
        auth_dialog.exec()
        self.auth_successful = auth_dialog.successful
        if self.auth_successful == False:
            sys.exit()

        self.resize(807, 358)
        self.centralwidget = QWidget(self)
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

        self.search_own_checkbox = QCheckBox(self.layoutWidget)
        self.search_own_checkbox.setText("Среди своих")
        self.horizontalLayout.addWidget(self.search_own_checkbox)

        self.search_btn = QPushButton(self.layoutWidget)
        self.search_btn.setText("Искать")
        self.search_btn.clicked.connect(self.search_btn_clicked)
        self.horizontalLayout.addWidget(self.search_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.docs_table = QTableWidget(self.layoutWidget)
        self.docs_table.setObjectName(u"docs_table")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.docs_table.sizePolicy().hasHeightForWidth())
        self.docs_table.setSizePolicy(sizePolicy)
        self.docs_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.docs_table.setRowCount(0)
        self.docs_table.setColumnCount(0)
        self.docs_table.horizontalHeader().setCascadingSectionResizes(False)
        self.docs_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.docs_table)

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

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

        self.token = auth_dialog.token
        self.business_logic = BusinessLogic(self.token)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"vkDocuments", None))
        self.lblSearch.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btnDownload.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.btnRename.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u0442\u044c", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b \u0438 \u043f\u0430\u043f\u043a\u0438", None))
        self.btnLoad.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.btnAuth.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))

    def sizeof_fmt(self, num, suffix="б"):
        for unit in ["", "К", "М", "Г", "Т", "П", "Э", "Ц"]:
            if abs(num) < 1024.0:
                return f"{num:3.1f}{unit}{suffix}"
            num /= 1024.0
        return f"{num:.1f}Yi{suffix}"

    def unix_to_datetime(self, date):
        ts = date

        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    def search_btn_clicked(self):
        own_docs = self.search_own_checkbox.isChecked()
        docs = self.business_logic.search_doc(self.lnEdtSearch.text(), own_docs=own_docs)

        self.docs_table.clear()

        if docs != []:
            self.docs_table.setRowCount(len(docs))
            self.docs_table.setColumnCount(3)

            row_index = 0

            self.docs_table.setHorizontalHeaderLabels([
                'Название',
                'Размер',
                'Дата загрузки',
                # 'Ссылка',
            ])

            for doc in docs:
                self.docs_table.setItem(row_index, 0, QTableWidgetItem(doc['title']))
                self.docs_table.setItem(row_index, 1, QTableWidgetItem(str(self.sizeof_fmt(doc['size']))))
                self.docs_table.setItem(row_index, 2, QTableWidgetItem(str(self.unix_to_datetime(doc['date']))))
                # self.docs_table.setItem(row_index, 3, QTableWidgetItem(doc['url']))

                row_index += 1

            # self.docs_table.resizeColumnToContents(0)
            self.docs_table.setColumnWidth(0, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
