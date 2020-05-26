#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout, QLabel, QFrame


class CardWidget(QFrame):

    def __init__(self, name: str, desc: str):
        super(CardWidget, self).__init__()

     #   self.setStyleSheet("background-color:white")
        self.grid_layout = QGridLayout()

        name_label = QLabel(name)
        desc_label = QLabel(desc)
        # 名称
        self.grid_layout.addWidget(name_label, 0, 0)
        # 简介
        self.grid_layout.addWidget(desc_label, 1, 0)

        self.setLayout(self.grid_layout)
