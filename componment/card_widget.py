#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import typing

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QListWidget,QGridLayout


class CardWidget(QListWidgetItem):

    def __init__(self, parent: QListWidget):
        super(CardWidget, self).__init__()

        self.parent = parent

        self.grid_layout = QGridLayout()
        # 名称
        self.grid_layout.addWidget('名称', 0, 0)
        # 简介
        self.grid_layout.addWidget('', 0, 0)

