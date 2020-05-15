#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class Const(object):
    """
    常量
    """
    # 工程名
    project_name = 'like_me_learn'
    # 根目录
    root_path = os.path.abspath(os.path.dirname(__file__))
    # 资源文件夹
    assets_folder = os.path.join(root_path, 'assets')
    # 启动图
    window_start_gif_path = os.path.join(assets_folder, 'window_start.gif')
    # 窗口图
    window_icon_path = os.path.join(assets_folder, 'window_icon.png')
    # 退出图
    exit_img_path = os.path.join(assets_folder, 'exit.png')
