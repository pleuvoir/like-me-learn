#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QLabel, QTextEdit, QPushButton, QMessageBox, \
    QTextBrowser
from tools.config import Const


class LogView(QWidget):

    def __init__(self):
        super().__init__()

        self.signal_ins = pyqtSignal()  # 自定义信号

        self.browser = QTextBrowser(self)
        self.browser.setPlaceholderText('程序运行日志')

        self.clear_btn = QPushButton('清空', self)
        self.clear_btn.clicked.connect(lambda: self.browser.clear())

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.browser)
        self.v_layout.addWidget(self.clear_btn)

        self.setLayout(self.v_layout)
        self.resize(1200, 850)
        self.setWindowTitle(Const.project_name)

    def info(self, text: str):
        self.browser.insertPlainText(text + '\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = LogView()
    view.show()
    sys.exit(app.exec_())
