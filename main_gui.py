# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from time import time, sleep

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from configuration import Const
from main_window_builder import MainWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)
    start = time()
    app.setWindowIcon(QIcon(Const.window_icon_path))

    splash = QSplashScreen()
    splash.setPixmap(QPixmap(Const.window_start_gif_path))
    splash.show()

    while time() - start < 1:
        sleep(0.001)
        app.processEvents()

    gui = MainWindow()
    gui.show()
    splash.finish(gui)
    sys.exit(app.exec_())
