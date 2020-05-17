#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QApplication, QSplitter, QFrame, QVBoxLayout, QPushButton, QLabel

from tools.config import Const
from tools import assets  # 必须导入，替换:assets qrc资源


class SplitterView(QWidget):

    def __init__(self):
        super(SplitterView, self).__init__()

        # 水平布局
        h_layout = QHBoxLayout()

        # 左侧面板
        self.left = QFrame()
        self.left.setFrameShape(QFrame.StyledPanel)

        # 中部面板
        self.middle = QFrame()
        self.middle.setFrameShape(QFrame.StyledPanel)

        # 右侧面板
        self.right = QFrame()
        self.right.setFrameShape(QFrame.StyledPanel)

        # 分割器
        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(1)  # 缩小三个框直接的缝隙

        splitter.insertWidget(0, self.left)
        splitter.insertWidget(1, self.middle)
        splitter.insertWidget(2, self.right)

        # 设置为不随着窗口大小改变而缩放
        splitter.setStretchFactor(0, 0)  # 这样最左边的栏不会因为全屏而变宽
        splitter.setStretchFactor(1, 1)
        splitter.setStretchFactor(2, 1)

        splitter.setSizes([55, 625, 800])

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
        label_img.setScaledContents(False)

        v_layout.addStretch(1)
        v_layout.addWidget(label_img)
        v_layout.addStretch(9)

        self.left.setLayout(v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = SplitterView()
    view.show()
    sys.exit(app.exec_())
