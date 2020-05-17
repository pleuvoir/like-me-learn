#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil

_current_folder = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    os.system('pyrcc5 -o tools/assets.py tools/assets.qrc')
    # #os.system('pyinstaller -F -w -i assets/window_icon.png --distpath release main.py')
    # os.system('pyinstaller -F -w --distpath release main.py')
    # os.remove(os.path.join(_current_folder, 'main.spec'))
    # shutil.rmtree(os.path.join(_current_folder, 'build'))
