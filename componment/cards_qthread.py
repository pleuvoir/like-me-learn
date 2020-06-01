#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal

from tools.config import Const
import os


class CardsThread(QThread):

    def __init__(self, attach_signal: pyqtSignal):
        super(CardsThread, self).__init__()
        self.attach_signal = attach_signal

    def run(self):
        if os.path.exists(Const.knowledge_folder_path):
            with open(Const.knowledge_folder_path, 'r', encoding='utf-8') as md:
                for line in md.readlines():
                    line_split = line.split('&&')
                    self.attach_signal.emit(line_split[0], line_split[1])
