#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea, QWidget, QGridLayout

from componment.card_widget import CardWidget
from helper.qlabel_img import QLabelImg
from tools.config import Const, GlobalContext


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

        # 重写点击事件，加号
        label_img = QLabelImg(img_path=Const.add_icon_path, press_event_fn=lambda: self.add_btn_fn())

        h_layout.addWidget(label_title)
        h_layout.addStretch(1)
        h_layout.addWidget(label_img)

        # 滚动条区域指定一个父面板，然后往这个父面板上添加子面板
        parent_card_widget = QWidget()
        card_area = QScrollArea()
        card_area.setWidget(parent_card_widget)  # 绑定滚动条和父面板
        card_area.setWidgetResizable(True)
        card_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 关闭横向

        # 网格布局
        self.q_grid_layout = QGridLayout(parent_card_widget)
        self.q_grid_layout.setSpacing(10)

        for i in range(10):
            self.q_grid_layout.addWidget(CardWidget(), i, 0)

        v_layout.addLayout(h_layout)
        v_layout.addWidget(card_area)

        self.setLayout(v_layout)

    def add_btn_fn(self):
        """
        显示增加弹出框
        """
        GlobalContext.add_dialog().show()
