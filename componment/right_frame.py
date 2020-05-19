#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QFrame

from tools.config import Const


class RightFrame(QFrame):

    def __init__(self):
        super(RightFrame, self).__init__()

        self.setFrameShape(QFrame.StyledPanel)
        self.resize(Const.right_frame_width, Const.default_window_height)
        self.setMinimumWidth(Const.right_frame_width)

        #
        self.setObjectName("RightFrame")
        self.setStyleSheet("#RightFrame{border-image:url(:assets/right_bg.png);}")

    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #
    #     #  设置背景图片，平铺到整个窗口，随着窗口改变而改变
    #     pixmap = QPixmap(":assets/right_bg.png")
    #     painter.drawPixmap(self.rect(), pixmap)
