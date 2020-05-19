#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel

from tools.config import Const

"""
左侧面板
"""


class LeftFrame(QFrame):

    def __init__(self):
        super(LeftFrame, self).__init__()

        v_layout = QVBoxLayout()

        label_img_book = QLabel()
        origin_icon = QPixmap(Const.book_icon_path)
        scaled = origin_icon.scaled(QSize(35, 35))
        label_img_book.setPixmap(scaled)
        label_img_book.setFrameStyle(QFrame.NoFrame)
        label_img_book.setScaledContents(True)
        label_img_book.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        # 设置
        label_img_setting = QLabel()
        label_img_setting.setPixmap(QPixmap(Const.setting_icon_path).scaled(QSize(35, 35)))
        label_img_setting.setFrameStyle(QFrame.NoFrame)
        label_img_setting.setScaledContents(True)
        label_img_setting.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        v_layout.addStretch(1)
        v_layout.addWidget(label_img_book)
        v_layout.addStretch(20)
        v_layout.addWidget(label_img_setting)
        v_layout.addStretch(1)

        self.setLayout(v_layout)
