#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea, QWidget

from componment.card_widget import CardWidget
from componment.cards_qthread import CardsThread
from helper.qlabel_img import QLabelImg
from tools.config import Const, GlobalContext


class MiddleFrame(QFrame):
    card_fill_result_signal = pyqtSignal(str, str)

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
        label_title.setObjectName('MiddleFrame_label_title')
        label_title.setStyleSheet("#MiddleFrame_label_title{font-size:21px}")

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
        self.q_v_layout = QVBoxLayout(parent_card_widget)
        self.q_v_layout.setSpacing(10)

        self.fill_cards()

        v_layout.addLayout(h_layout)
        v_layout.addWidget(card_area)

        self.setLayout(v_layout)

    def fill_cards(self):
        """
        异步加载知识库区域的内容
        """
        self.card_fill_result_signal.connect(self.fill_cards_callback)
        self.fill_card_thread = CardsThread(self.card_fill_result_signal)
        self.fill_card_thread.start()

    def fill_cards_callback(self, title, desc):
        self.q_v_layout.addWidget(CardWidget(title, desc))

    def add_btn_fn(self):
        """
        显示增加弹出框
        """
        GlobalContext.add_dialog().show()
