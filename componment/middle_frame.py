#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt, QStringListModel
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea, QListWidget, QListWidgetItem, \
    QListView

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
        card_list_view = QListView()
        card_list_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 关闭横向

        model = QStringListModel()
        model.setStringList(['item %s' % i for i in range(60)])
        card_list_view.setModel(model)

        v_layout.addLayout(h_layout)
        v_layout.addWidget(card_list_view)

        self.setLayout(v_layout)
