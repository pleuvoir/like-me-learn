#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QSplitter, QFrame, QVBoxLayout, QLabel, QDesktopWidget

from tools.config import Const, GlobalContext


class SplitterView(QWidget):

    def __init__(self):
        super(SplitterView, self).__init__()

        log = GlobalContext.log_view()

        # 分割器
        splitter = QSplitter(Qt.Horizontal)

        # 计算三个面板的宽度，采用自适应分辨率的方式
        left_width = Const.left_frame_width
        current_layout_width = self.frameGeometry().width()  # 如果没有设置初始值，它会有一个默认
        log.info('当前窗口的宽度为{}'.format(current_layout_width))
        remain_width = current_layout_width - left_width
        middle_width = remain_width / 100 * 35
        right_width = remain_width / 100 * 65
        log.info('当前窗口的剩余宽度为{}，middle_width={}，right_width={}'.format(remain_width, middle_width, right_width))



        # 水平布局
        h_layout = QHBoxLayout()

        # 左侧面板
        self.left = QFrame()
        self.left.setFrameShape(QFrame.StyledPanel)
        self.left.setFixedWidth(left_width)  # 左侧的一直是固定的
        log.info('设置左侧面板固定宽度为{}'.format(left_width))

        # 中部面板
        self.middle = QFrame()
        self.middle.setFrameShape(QFrame.StyledPanel)
        # self.middle.setMinimumWidth(middle_width / 100 * 100)
        # self.middle.setMaximumWidth(middle_width / 100 * 115)
        log.info('设置中部面板最小宽度为{}'.format(middle_width / 100 * 85))

        # 右侧面板
        self.right = QFrame()
        self.right.setFrameShape(QFrame.StyledPanel)
        self.right.setMinimumWidth(right_width / 100 * 100)
       # self.right.setMinimumWidth(380)
        log.info('设置右侧面板最小宽度为{}'.format(right_width / 100 * 85))



        splitter.setHandleWidth(1)  # 缩小三个框直接的缝隙

        splitter.insertWidget(0, self.left)
        splitter.insertWidget(1, self.middle)
        splitter.insertWidget(2, self.right)

        # 设置为不随着窗口大小改变而缩放
        splitter.setStretchFactor(0, 0)  # 这样最左边的栏不会因为全屏而变宽
        splitter.setStretchFactor(1, 1)
        splitter.setStretchFactor(2, 1)

        # 设置为不可拖动至隐藏
        splitter.setCollapsible(0, False)
        splitter.setCollapsible(1, False)
        splitter.setCollapsible(2, False)

        splitter.setSizes([left_width, middle_width, right_width]) # 不要移动到上面去，否则宽度等设置会出问题
       # splitter.setSizes([left_width, 50, 380])
        log.info(
            '设置分割器三面板宽度，left_width={}，middle_width={}，right_width={}'.format(left_width, middle_width, right_width))

        # 将分割器面板增加到水平布局中
        h_layout.addWidget(splitter)

        # 设置当前布局为水平布局的内容
        self.setLayout(h_layout)

        self.init_left_frame()

    def init_left_frame(self):
        v_layout = QVBoxLayout()

        label_img = QLabel()
        origin_icon = QPixmap(Const.book_icon_path)
        scaled = origin_icon.scaled(QSize(35, 35))

        label_img.setPixmap(scaled)
        label_img.setFrameStyle(QFrame.NoFrame)
        label_img.setScaledContents(True)

        v_layout.addStretch(1)
        v_layout.addWidget(label_img)
        v_layout.addStretch(9)

        self.left.setLayout(v_layout)
