#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QPushButton


class QPushButtonImg(QPushButton):

    def __init__(self, img_path: str, press_event_fn=None):
        super(QPushButtonImg, self).__init__()

        self.press_event_fn = press_event_fn
        self.setIcon(QIcon(img_path))
        self.setIconSize(QtCore.QSize(35, 35))
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.setStyleSheet("""
                  border: 0px;
              """)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.press_event_fn:
            self.press_event_fn()
        event.accept()
        print(event.localPos())
