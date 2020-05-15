#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from logger import logger


class AbstractGUIBuilder(QMainWindow):
    """
    GUI构造模板
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()
        logger.info('[*]初始化窗口')
        self.init_window()
        logger.info('[*]初始化菜单栏')
        self.init_menu()
        logger.info('[*]初始化状态栏')
        self.init_status_bar()
        logger.info('[*]初始化中心区域')
        self.init_central_area()

    @abstractmethod
    def init_window(self):
        """
        初始化窗口
        """
        pass

    @abstractmethod
    def init_menu(self):
        """
        初始化菜单栏
        """
        pass

    @abstractmethod
    def init_status_bar(self):
        """
        初始化状态栏
        """
        pass

    @abstractmethod
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
