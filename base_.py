#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp

from abstract_gui_builder import AbstractGUIBuilder
from configuration import Const


class BaseGUI(AbstractGUIBuilder):

    def __init__(self):
        super().__init__()

    def init_window(self):
        self.setGeometry(50, 50, 850, 650)
        self.setWindowTitle('Learn like me')
        self.center()

    def init_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&文件')
        exit_act = QAction(QIcon(Const.exit_img_path), '&退出', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('退出')
        exit_act.triggered.connect(qApp.quit)
        file_menu.addAction(exit_act)

    def init_status_bar(self):
        pass

    def init_central_area(self):
        pass
