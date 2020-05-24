#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QAction, QVBoxLayout, QLabel, QFrame

from tools.config import Const, GlobalContext

"""
这个窗口应该依附于中心窗口布局
"""


class MiddleAddWidget(QWidget):

    def __init__(self):
        super(MiddleAddWidget, self).__init__()

        self.setParent(GlobalContext.lmr_manager())

        self.setFixedSize(650,400)
        # 设置窗口为模态，用户只有关闭弹窗后，才能关闭主界面
        self.setWindowModality(Qt.ApplicationModal)

