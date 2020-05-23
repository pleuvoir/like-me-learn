#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QFrame, QVBoxLayout

from componment.setting_widget import SettingWidget
from helper.qlabel_img import QLabelImg
from helper.qpushbutton_img import QPushButtonImg
from tools.config import Const

"""
左侧面板
"""


class LeftFrame(QFrame):

    def __init__(self):
        super(LeftFrame, self).__init__()

        v_layout = QVBoxLayout()

        label_img_book = QLabelImg(Const.book_icon_path)

        # 设置
        setting_widget = SettingWidget()
        label_img_setting = QPushButtonImg(img_path=Const.setting_icon_path, press_event_fn=lambda: setting_widget.show())

        v_layout.addStretch(1)
        v_layout.addWidget(label_img_book)
        v_layout.addStretch(20)
        v_layout.addWidget(label_img_setting)
        v_layout.addStretch(1)

        self.setLayout(v_layout)
