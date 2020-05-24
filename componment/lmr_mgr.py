#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter

from componment.left_frame import LeftFrame
from componment.middle_frame import MiddleFrame
from componment.right_frame import RightFrame
from tools.config import GlobalContext


class LmrManager(QWidget):

    def __init__(self):
        super(LmrManager, self).__init__()

        h_layout = QHBoxLayout()

        left_frame = LeftFrame()

        middle_frame = MiddleFrame()
        right_frame = RightFrame()

        mr_splitter = QSplitter()

        # 缩小三个框直接的缝隙
        mr_splitter.setHandleWidth(1)

        mr_splitter.insertWidget(0, middle_frame)
        mr_splitter.insertWidget(1, right_frame)

        mr_splitter.setStretchFactor(0, 1)  # 全屏后保持1：4的比例，但是之前设置的最小宽度此时可能就比较小了
        mr_splitter.setStretchFactor(1, 4)

        # 设置为不可拖动至隐藏
        mr_splitter.setCollapsible(0, False)
        mr_splitter.setCollapsible(1, False)

        h_layout.addWidget(left_frame)
        h_layout.addWidget(mr_splitter)

        self.setLayout(h_layout)
