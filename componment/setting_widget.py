#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QAction, QVBoxLayout, QLabel, QFrame

from tools.config import Const, GlobalContext


class SettingWidget(QFrame):

    def __init__(self):
        super(SettingWidget, self).__init__()


       # self.setParent(GlobalContext.main_window())

     #   self.setFixedSize(150,100)
     #   self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.setGeometry(300, 300, 300, 220)
        self.move(20,20)
        v_layout = QVBoxLayout()

        log_label = QLabel()
        log_label.setText('查看日志')

        exit_label = QLabel()
        exit_label.setText('退出')

        v_layout.addWidget(log_label)
        v_layout.addWidget(exit_label)


        # log_act = QAction(QIcon(Const.log_img_path), '&查看日志', self)
        #
        # log_act.triggered.connect(lambda: GlobalContext.log_view().show())

        # self.addAction(log_act)

        self.setLayout(v_layout)
