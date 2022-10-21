# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys, os
from business_logic.business_logic import BusinessLogic
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QDir, Qt)
from PySide6.QtWidgets import (QMainWindow, QAbstractScrollArea, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout, QMessageBox,
    QCheckBox, QWidget, QFileDialog, QDialog, QProgressBar)

from PySide6 import QtGui
from dialogs.auth_dialog import AuthDialog
from datetime import datetime
import requests
import shutil
from pathlib import Path


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
        self.search_own_checkbox.setText("Искать везде")
        self.horizontalLayout.addWidget(self.search_own_checkbox)

        self.search_btn = QPushButton(self.layoutWidget)
        self.search_btn.setText("Искать")
        self.search_btn.clicked.connect(self.search_btn_clicked)
        self.horizontalLayout.addWidget(self.search_btn)

        self.load_more_btn = QPushButton(self.layoutWidget)
        self.load_more_btn.setText("Еще")
        # self.load_more_btn.setEnabled(False)
        self.load_more_btn.clicked.connect(self.load_more_btn_clicked)
        self.horizontalLayout.addWidget(self.load_more_btn)        

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
        self.btnAuth.clicked.connect(self.btn_auth_clicked)

        self.horizontalLayout_2.addWidget(self.btnAuth)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

        self.token = auth_dialog.token
        self.business_logic = BusinessLogic(self.token)

        self.docs_to_download_dict = {}
        self.docs_to_download_sizes = {}
        self.download_all_btn = None
        self.progressBar = None

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"vkDocuments", None))
        self.lblSearch.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btnDownload.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.btnRename.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u0442\u044c", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b \u0438 \u043f\u0430\u043f\u043a\u0438", None))
        self.btnLoad.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.btnAuth.setText(QCoreApplication.translate("MainWindow", "Авторизация", None))

    def btn_auth_clicked(self):
        auth_dialog = AuthDialog()
        auth_dialog.exec()
        self.auth_successful = auth_dialog.successful
        if self.auth_successful == False:
            sys.exit()

    def sizeof_fmt(self, num, suffix="б"):
        for unit in ["", "К", "М", "Г", "Т", "П", "Э", "Ц"]:
            if abs(num) < 1024.0:
                return f"{num:3.1f}{unit}{suffix}"
            num /= 1024.0
        return f"{num:.1f}Yi{suffix}"

    def unix_to_datetime(self, date):
        ts = date

        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    def download_file(self, url, filepath):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(filepath, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        else:
            r.raise_for_status()

    def search_btn_clicked(self):
        self.own_docs = self.search_own_checkbox.isChecked()

        self.limit, self.offset = 0, 0
        docs = self.business_logic.search_doc(self.lnEdtSearch.text(), self.limit, self.offset, own_docs=self.own_docs)

        self.docs_table.clear()

        if docs != []:
            self.docs_table.setRowCount(len(docs))
            self.docs_table.setColumnCount(5)

            row_index = 0

            self.docs_table.setHorizontalHeaderLabels([
                'Название',
                'Размер',
                'Дата загрузки',
                # 'Ссылка',
            ])

            for doc in docs:
                to_download_checkbox = QCheckBox()
                to_download_checkbox.stateChanged.connect(lambda *args, sender=to_download_checkbox, link=doc['url'], filename=doc['title'], fileextension=doc['ext'], filesize=doc['size']: self.to_download_checkbox_checked(sender, link, filename, fileextension, filesize))

                self.docs_table.setItem(row_index, 0, QTableWidgetItem(doc['title']))
                self.docs_table.setItem(row_index, 1, QTableWidgetItem(str(self.sizeof_fmt(doc['size']))))
                self.docs_table.setItem(row_index, 2, QTableWidgetItem(str(self.unix_to_datetime(doc['date']))))

                self.docs_table.setCellWidget(row_index, 3, to_download_checkbox)
                # self.docs_table.cellWidget(row_index, 3).(Qt.AlignHCenter)

                download_file_btn = QPushButton("Скачать")
                download_file_btn.clicked.connect(lambda *args, row=self.docs_table.rowCount() - 1, column=2, value=doc['url'], filename=doc['title'], fileextension=doc['ext'], filesize=doc['size']: self.download_file_btn_clicked(row, column, value, filename, fileextension, filesize))
                self.docs_table.setCellWidget(row_index, 4, download_file_btn)

                # self.docs_table.setItem(row_index, 3, QTableWidgetItem(doc['url']))

                row_index += 1

            # self.docs_table.resizeColumnToContents(0)
            self.docs_table.setColumnWidth(0, 400)

    def download_file_btn_clicked(self, row, column, value, filename, fileextension, filesize):
        downloads_path = str(Path.home() / "Downloads")
        if os.path.splitext(filename) == "":
            filepath = '%s/%s.%s'%(downloads_path, filename, fileextension)
        else:
            filepath = '%s/%s'%(downloads_path, filename)

        if self.progressBar == None:
            self.progressBar = QProgressBar(self)
            self.verticalLayout.addWidget(self.progressBar)

        self.download_file(value, filepath)
        total = filesize

        download_percentage = filesize * 100 / total

        self.progressBar.setValue(download_percentage)
        QApplication.processEvents()

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setInformativeText("Скачивание завершено!")
        msg_box.setWindowTitle("Сообщение")
        msg_box.exec()

        self.progressBar.setValue(0)

    def to_download_checkbox_checked(self, sender, link, filename, fileextension, filesize):
        if sender.isChecked():
            if self.download_all_btn == None:
                self.download_all_btn = QPushButton("Скачать выделенные")
                self.download_all_btn.clicked.connect(self.download_all_btn_clicked)
                self.verticalLayout.addWidget(self.download_all_btn)

            self.docs_to_download_dict[filename] = link + "   " + fileextension
            self.docs_to_download_sizes[filename] = filesize
        else:
            if self.docs_to_download_dict != {}:
                del self.docs_to_download_dict[filename]
                del self.docs_to_download_sizes[filename]

        if self.docs_to_download_dict == {}:
            self.download_all_btn.setParent(None)
            self.download_all_btn = None

    def download_all_btn_clicked(self):
        download_path = str(QFileDialog.getExistingDirectory(self, "Выберите папку"))
        if self.progressBar == None:
            self.progressBar = QProgressBar(self)
            self.verticalLayout.addWidget(self.progressBar)

        total = sum(self.docs_to_download_sizes.values())

        for filename, link_ext in self.docs_to_download_dict.items():
            link = link_ext.split('   ')[0]
            fileextension = link_ext.split('   ')[1]

            if os.path.splitext(filename) == "":
                filepath = '%s/%s.%s'%(download_path, filename, fileextension)
            else:
                filepath = '%s/%s'%(download_path, filename)

            download_percentage = self.docs_to_download_sizes.get(filename) * 100 / total
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()

            self.download_file(link, filepath)

        self.progressBar.setValue(0)

    def load_more_btn_clicked(self):
        self.own_docs = self.search_own_checkbox.isChecked()
        self.limit += 10
        self.offset += 10
        docs = self.business_logic.search_doc(self.lnEdtSearch.text(), self.limit, self.offset, own_docs=self.own_docs)

        # self.docs_table.clear()

        if docs != []:
            row_index = self.docs_table.rowCount() - 1
            self.docs_table.setRowCount(len(docs) + self.docs_table.rowCount() - 1)

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

                download_file_btn = QPushButton("Скачать")
                download_file_btn.clicked.connect(lambda *args, row=self.docs_table.rowCount() - 1, column=2, value=doc['url'], filename=doc['title'], fileextension=doc['ext'], filesize=doc['size']: self.download_file_btn_clicked(row, column, value, filename, fileextension, filesize))
                self.docs_table.setCellWidget(row_index, 3, download_file_btn)

                # self.docs_table.setItem(row_index, 3, QTableWidgetItem(doc['url']))

                row_index += 1

            # self.docs_table.resizeColumnToContents(0)
            self.docs_table.setColumnWidth(0, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
