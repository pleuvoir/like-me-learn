#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QTextEdit

"""
这个窗口应该依附于中心窗口布局
"""


class MiddleAddWidget(QWidget):

    def __init__(self, parent):

        super(MiddleAddWidget, self).__init__()

        self.setParent(parent)
        self.setStyleSheet("background-color:white")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(225, 325)
        # 设置窗口为模态，用户只有关闭弹窗后，才能关闭主界面
        self.setWindowModality(Qt.ApplicationModal)

        self.name_label = QLabel('名称:')
        self.name_line = QLineEdit()

        self.desc_label = QLabel('简介:')
        self.desc_line = QTextEdit()

        self.add_btn = QPushButton('新建')

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.name_label)
        self.v_layout.addWidget(self.name_line)
        self.v_layout.addWidget(self.desc_label)
        self.v_layout.addWidget(self.desc_line)
        self.v_layout.addWidget(self.add_btn)

        self.setLayout(self.v_layout)

        # 父窗体中心位置
        lmr_manager_center = parent.frameGeometry().center()

        self.move(QPoint(lmr_manager_center.x(), 0))

        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
