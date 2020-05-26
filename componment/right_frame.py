#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFrame

from tools.config import Const


class RightFrame(QFrame):

    def __init__(self):
        super(RightFrame, self).__init__()

        self.setFrameShape(QFrame.StyledPanel)
        self.resize(Const.right_frame_width, Const.default_window_height)
        self.setMinimumWidth(Const.right_frame_width)

        self.setObjectName("RightFrame")
        self.setStyleSheet("#RightFrame{border-image:url(:assets/3.png);}")
