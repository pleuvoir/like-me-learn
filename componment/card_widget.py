#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QGridLayout, QLabel, QFrame

from tools.config import GlobalContext


class CardWidget(QFrame):

    def __init__(self, name: str, desc: str):
        super(CardWidget, self).__init__()

        self.setFixedHeight(100)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.grid_layout = QGridLayout()

        name_label = QLabel(name)
        desc_label = QLabel(desc)
        # 名称
        self.grid_layout.addWidget(name_label, 0, 0)
        # 简介
        self.grid_layout.addWidget(desc_label, 1, 0)

        self.setLayout(self.grid_layout)

        self.setObjectName("CardWidgetFrame")
        self.setStyleSheet("#CardWidgetFrame{border:1px solid #9b7576;border-radius:10px;;margin-top:2cm;}")


    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:

       # GlobalContext.right_frame().close()
        super().mousePressEvent(a0)


