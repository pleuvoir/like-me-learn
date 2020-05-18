#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib
from collections import OrderedDict

# 动态导入，不然格式化会删掉没有显式调用的代码
importlib.import_module('tools.assets')


class Const(object):
    # 默认窗口宽度
    default_window_width = 1175
    # 默认窗口高度
    default_window_height = 685
    # 最小窗口宽度
    min_window_width = 1050
    # 最小窗口高度
    min_window_height = 550
    # 左侧固定宽度
    left_frame_width = 55

    # 工程名
    project_name = 'Like me learn'
    # 启动图
    window_start_path = ':assets/window_start.png'
    # 窗口图
    window_icon_path = ':assets/window_icon.png'
    # 退出图
    exit_img_path = ':assets/exit.svg'
    # 日志图
    log_img_path = ':assets/log.svg'
    # 系统托盘图
    tray_icon_path = ':assets/window_icon.png'
    # 左侧窗体图标
    book_icon_path = ':assets/book.svg'

    # 主窗口
    key_main_window = 'main_window'
    # 日志窗口
    key_log_view = 'log_view'
    # 系统托盘
    key_tray_view = 'tray_view'


class GlobalContext(object):
    _dict = OrderedDict()

    def __init__(self):
        super().__init__()

    @staticmethod
    def setup(key: str, value: object):
        GlobalContext._dict[key] = value

    @staticmethod
    def get_instance(key: str):
        return GlobalContext._dict.get(key)

    @staticmethod
    def main_window():
        return GlobalContext.get_instance(Const.key_main_window)

    @staticmethod
    def log_view():
        return GlobalContext.get_instance(Const.key_log_view)

    @staticmethod
    def tray_view():
        return GlobalContext.get_instance(Const.key_tray_view)
