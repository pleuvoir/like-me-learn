#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QFrame, QVBoxLayout

from helper.qlabel_img import QLabelImg
from tools.config import Const

"""
左侧面板
"""


class LeftFrame(QFrame):

    def __init__(self):
        super(LeftFrame, self).__init__()

        v_layout = QVBoxLayout()

        label_img_book = QLabelImg(Const.book_icon_path)

        v_layout.addStretch(1)
        v_layout.addWidget(label_img_book)
        v_layout.addStretch(20)

        self.setLayout(v_layout)
