import os
import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from base_ import BaseGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    assets_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets')
    app.setWindowIcon(QIcon(os.path.join(assets_folder, 'window_icon.png')))

    splash = QSplashScreen()
    splash.setPixmap(QPixmap(os.path.join(assets_folder, 'window_start.gif')))
    splash.show()

    gui = BaseGUI()
    gui.showMaximized()
    sys.exit(app.exec_())
