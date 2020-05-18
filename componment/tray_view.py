#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon

from tools.config import Const
from tools.config import Global

"""
系统托盘
"""


class TrayView(QSystemTrayIcon):

    def __init__(self):
        super(TrayView, self).__init__()
        # 设置托盘图标
        self.setIcon(QIcon(Const.tray_icon_path))
        self.setToolTip(Const.project_name)
        # 绑定信号
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        """
        系统托盘点击事件
        :param reason:  Trigger/MiddleClick
        """
        if reason == QSystemTrayIcon.Trigger:
            Global.getMainWindow().show()
