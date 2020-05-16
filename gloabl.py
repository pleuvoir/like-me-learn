#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import OrderedDict


class Global(object):
    dict = OrderedDict()

    def __init__(self):
        super().__init__()

    @staticmethod
    def setup(key: str, value: object):
        Global.dict[key] = value

    @staticmethod
    def getInstance(key: str):
        return Global.dict.get(key)
