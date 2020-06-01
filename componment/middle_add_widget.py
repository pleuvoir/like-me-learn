#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QTextEdit, QDialog, QHBoxLayout, QMessageBox

from componment.card_widget import CardWidget
from tools.config import GlobalContext, Const

"""
这个窗口应该依附于中心窗口布局
"""


class MiddleAddDialog(QDialog):

    def __init__(self, parent):
        super(MiddleAddDialog, self).__init__()

        self.setFixedSize(425, 325)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        # 设置窗口为模态，用户只有关闭弹窗后，才能关闭主界面
        self.setWindowModality(Qt.ApplicationModal)
        self.setParent(parent)

        self.name_label = QLabel('名称:')
        self.name_line = QLineEdit()

        self.desc_label = QLabel('简介:')
        self.desc_line = QTextEdit()

        self.h_layout = QHBoxLayout()
        self.add_btn = QPushButton('新建')
        self.add_btn.clicked.connect(lambda: self.add_slot())
        self.cancel_btn = QPushButton('取消')
        self.cancel_btn.clicked.connect(lambda: self.cancel_slot())
        self.h_layout.addWidget(self.cancel_btn)
        self.h_layout.addWidget(self.add_btn)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.name_label)
        self.v_layout.addWidget(self.name_line)
        self.v_layout.addWidget(self.desc_label)
        self.v_layout.addWidget(self.desc_line)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

        # 父窗体中心位置
        lmr_manager_center = parent.frameGeometry().center()

        self.move(QPoint(lmr_manager_center.x(), 0))
        # 设置了父窗体后此组件默认会显示，这里隐藏下
        self.close()

    def cancel_slot(self):
        self.name_line.setText('')
        self.desc_line.setText('')
        self.close()

    def add_slot(self):
        with open(Const.knowledge_folder_path, mode='a', encoding='utf-8') as f:
            print(self.name_line.text() + '&&' + self.desc_line.toPlainText(), end='\n', file=f)
        QMessageBox.information(self, 'information', '新建成功！', QMessageBox.Ok)

        GlobalContext.middle_frame().q_v_layout.addWidget(
            CardWidget(self.name_line.text(), self.desc_line.toPlainText()))
        self.name_line.setText('')
        self.desc_line.setText('')

        self.close()
