#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea, QListWidget, QListWidgetItem

from tools.config import Const


class MiddleFrame(QFrame):

    def __init__(self):
        super(MiddleFrame, self).__init__()

        self.setFrameShape(QFrame.StyledPanel)
        self.resize(Const.middle_frame_width, Const.default_window_height)
        self.setMinimumWidth(Const.middle_frame_width - 100)

        # 垂直布局
        v_layout = QVBoxLayout()

        # 水平布局，最上面
        h_layout = QHBoxLayout()
        label_title = QLabel('知识库')
        label_img = QLabel()
        origin_icon = QPixmap(Const.add_icon_path)
        scaled = origin_icon.scaled(QSize(35, 35))
        label_img.setPixmap(scaled)
        label_img.setFrameStyle(QFrame.NoFrame)
        label_img.setScaledContents(True)
        label_img.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        h_layout.addWidget(label_title)
        h_layout.addStretch(1)
        h_layout.addWidget(label_img)

        # 下面的滚动卡片区域
        scroll_area = QScrollArea()
        card_list_widget = QListWidget(parent=scroll_area)
        for i in range(6):
            card_list_widget.addItem(QListWidgetItem('Item {}'.format(i)))


        v_layout.addLayout(h_layout)
        v_layout.addWidget(scroll_area)

        self.setLayout(v_layout)
