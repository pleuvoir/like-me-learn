#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter

from componment.left_frame import LeftFrame
from componment.middle_frame import MiddleFrame
from componment.right_frame import RightFrame
from tools.config import GlobalContext, Const


class LmrManager(QWidget):

    def __init__(self):
        super(LmrManager, self).__init__()

        self.h_layout = QHBoxLayout()

        self.left_frame = LeftFrame()

        self.middle_frame = MiddleFrame()
        self.right_frame = RightFrame()

        self.mr_splitter = QSplitter()

        # 缩小三个框直接的缝隙
        self.mr_splitter.setHandleWidth(1)

        self.mr_splitter.insertWidget(0, self.middle_frame)
        self.mr_splitter.insertWidget(1, self.right_frame)

        self.mr_splitter.setStretchFactor(0, 1)  # 全屏后保持1：4的比例，但是之前设置的最小宽度此时可能就比较小了
        self.mr_splitter.setStretchFactor(1, 4)

        # 设置为不可拖动至隐藏
        self.mr_splitter.setCollapsible(0, False)
        self.mr_splitter.setCollapsible(1, False)

        self.h_layout.addWidget(self.left_frame)
        self.h_layout.addWidget(self.mr_splitter)

        self.setLayout(self.h_layout)

