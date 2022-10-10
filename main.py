import sys
import pathlib

from PySide6 import QtWidgets, QtCore, QtGui
# from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from main_window import Ui_MainWindow
from dialogs.auth_dialog import AuthDialog

from services.vk_service import get_docs

from src import config


# class AuthDialog(QtWidgets.QDialog):
#     def __init__(self):
#         super(AuthDialog, self).__init__()
#         self.ui = Ui_dlgAuth()
#         self.ui.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.docs = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.auth_dlg_window = AuthDialog()

        self.ui.btnAuth.clicked.connect(self._show_auth_dialog)

        self.ui.lnEdtSearch.textChanged.connect(self._search_docs)

        # self.access_token = None
        self.access_token = ""

        path = pathlib.Path(config.DATA)

        # if path.exists():
        #     with open(path) as f:
        #         data = f.read()
        #         self.access_token = data if data else None
        #         if self.access_token:
        #             self.ui.btnAuth.setEnabled(False)
        #             self.show_table_docs()

    def show_table_docs(self):
        self.ui.tblWdgt.setRowCount(0)
        self.ui.tblWdgt.setColumnCount(1)
        self.docs = get_docs(self.access_token)

        for i in range(len(self.docs)):
            self.ui.tblWdgt.insertRow(i)
            self.ui.tblWdgt.setItem(i, 0, QtWidgets.QTableWidgetItem(self.docs[i]['title']))

    @QtCore.Slot()
    def _show_auth_dialog(self):

        if not self.access_token:

            import webbrowser

            # webbrowser.open(config.URL)

            result = self.auth_dlg_window.exec()

            if result == QtWidgets.QDialog.Accepted:
                with open(config.DATA, 'w') as f:
                    self.access_token = self.auth_dlg_window.ui.lnEdtAccessToken.text()
                    f.write(self.access_token)

                self.auth_dlg_window.ui.lnEdtAccessToken.setText('')
                self.ui.btnAuth.setEnabled(False)

                self.show_table_docs()

    @QtCore.Slot()
    def _search_docs(self):
        self.ui.tblWdgt.setRowCount(0)
        pattern = self.ui.lnEdtSearch.text()
        counter = 0
        for doc in self.docs:
            if doc['title'].lower().find(pattern.lower()) != -1:
                self.ui.tblWdgt.insertRow(counter)
                self.ui.tblWdgt.setItem(counter, 0, QtWidgets.QTableWidgetItem(doc['title']))
                counter += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
