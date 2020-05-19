#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QWidget
from qtpy import QtCore

from tools.config import Const

"""
左侧面板
"""


class LeftFrame(QFrame):

    def __init__(self):
        super(LeftFrame, self).__init__()

        v_layout = QVBoxLayout()

        label_img = QLabel()
        origin_icon = QPixmap(Const.book_icon_path)
        scaled = origin_icon.scaled(QSize(35, 35))

        label_img.setPixmap(scaled)
        label_img.setFrameStyle(QFrame.NoFrame)
        label_img.setScaledContents(True)
        label_img.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        v_layout.addStretch(1)
        v_layout.addWidget(label_img)
        v_layout.addStretch(9)

        self.setLayout(v_layout)
