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

        # 设置当前面板和主窗口一般大
      #  self.setGeometry(GlobalContext.main_window().frameGeometry())

        h_layout = QHBoxLayout()

        left_frame = LeftFrame()

        middle_frame = MiddleFrame()
        right_frame = RightFrame()

        mr_splitter = QSplitter()

        # 缩小三个框直接的缝隙
        mr_splitter.setHandleWidth(1)

        mr_splitter.insertWidget(0, middle_frame)
        mr_splitter.insertWidget(1, right_frame)

        mr_splitter.setStretchFactor(0, 0)  # 这样最左边的栏不会因为全屏而变宽
        mr_splitter.setStretchFactor(1, 0)

        # 设置为不可拖动至隐藏
        mr_splitter.setCollapsible(0, False)
        mr_splitter.setCollapsible(1, False)

        h_layout.addWidget(left_frame)
        h_layout.addWidget(mr_splitter)

        self.setLayout(h_layout)
