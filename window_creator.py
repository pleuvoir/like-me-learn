#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp, QApplication, QSystemTrayIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from componment.log_view import LogView
from componment.splitter_view import SplitterView
from tools.config import Const


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # 独立显示日志
        self.log_view = LogView()

        self.log_view.info('[*] 初始化窗口')
        self.init_window()

        self.log_view.info('[*] 初始化菜单栏')
        self.init_menu()

        self.log_view.info('[*] 初始化状态栏')
        self.init_status_bar()

        self.log_view.info('[*] 初始化中心区域')
        self.init_central_area()

    def init_window(self):
        """
        初始化窗口
        """
        self.resize(1175, 685)
        self.setMinimumSize(1050, 550)
        self.setWindowTitle('Learn like me')
        self.center()

        QApplication.setQuitOnLastWindowClosed(False)  # 禁止默认的closed方法
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(Const.tray_icon_path))
        self.tray_icon.setToolTip(Const.project_name)

        self.tray_icon.activated.connect(self.onTrayIconActivated)
        self.tray_icon.show()

        # 设置拆分窗口为中心布局
        splitter_view = SplitterView()
        self.setCentralWidget(splitter_view)

    def onTrayIconActivated(self, reason):
        """
        系统托盘点击事件
        :param reason:  Trigger/MiddleClick
        """
        if reason == self.tray_icon.Trigger:
            self.show()

    def init_menu(self):
        """
        初始化菜单栏
        """
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&文件')
        exit_act = QAction(QIcon(Const.exit_img_path), '&退出', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('退出')
        exit_act.triggered.connect(qApp.quit)
        file_menu.addAction(exit_act)

        log_act = QAction(QIcon(Const.exit_img_path), '&查看日志', self)
        log_act.setStatusTip('查看日志')
        log_act.triggered.connect(lambda: self.log_view.show())
        file_menu.addAction(log_act)

    def init_status_bar(self):
        """
        初始化状态栏
        """
        pass

    def init_central_area(self):
        """
        初始化中心区域
        """
        pass

    def center(self):
        """
        居中窗口
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
