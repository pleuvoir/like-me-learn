import os
from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget


class AbstractGUIBuilder(QMainWindow):
    """
    GUI构造模板
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_menu()
        self.init_status_bar()
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

    @staticmethod
    def assets_folder():
        """
        获取资源文件目录
        """
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets')

    def center(self):
        """
        居中窗口
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
