#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict
from tools import assets  # 必须导入，替换:assets qrc资源


class Const(object):
    """
    常量
    """
    # 工程名
    project_name = 'Like me learn'
    # 启动图
    window_start_path = ':assets/window_start.png'
    # 窗口图
    window_icon_path = ':assets/window_icon.png'
    # 退出图
    exit_img_path = ':assets/exit.png'
    # 系统托盘图
    tray_icon_path = ':assets/window_icon.png'
    # 左侧窗体图标
    book_icon_path = ':assets/book.svg'


class Global(object):
    dict = OrderedDict()

    def __init__(self):
        super().__init__()

    @staticmethod
    def setup(key: str, value: object):
        Global.dict[key] = value

    @staticmethod
    def get_instance(key: str):
        return Global.dict.get(key)
