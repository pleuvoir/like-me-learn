#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QFrame, QLabel


class QLabelImg(QLabel):
    """
    提供对图片的点击功能，可传入匿名函数
    """

    def __init__(self, img_path: str, press_event_fn=None):
        super(QLabelImg, self).__init__()

        self.setPixmap(QPixmap(img_path).scaled(QSize(35, 35)))
        self.setFrameStyle(QFrame.NoFrame)
        self.setScaledContents(True)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.press_event_fn = press_event_fn

    def mousePressEvent(self, event):
        if self.press_event_fn:
            self.press_event_fn()
        event.accept()
