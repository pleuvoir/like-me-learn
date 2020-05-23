#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QAction, QMenu, qApp

from tools.config import Const, GlobalContext

"""
系统托盘
"""


class TrayView(QSystemTrayIcon):

    def __init__(self):
        super(TrayView, self).__init__()

        self.parent_window = GlobalContext.main_window()

        self.setParent(self.parent_window)

        # 设置托盘图标
        self.setIcon(QIcon(Const.tray_icon_path))
        self.setToolTip(Const.project_name)
        # 绑定左键信号
        self.activated.connect(self.tray_icon_click)

        show_action = QAction("显示", self.parent_window)
        quit_action = QAction("退出", self.parent_window)
        hide_action = QAction("隐藏", self.parent_window)
        show_action.triggered.connect(self.parent_window.show)
        hide_action.triggered.connect(self.parent_window.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.setContextMenu(tray_menu)
        self.show()

    def tray_icon_click(self, reason):
        """
        系统托盘点击事件
        :param reason:  Trigger/MiddleClick
        """
        if reason == QSystemTrayIcon.Trigger:
            self.parent_window.show()
