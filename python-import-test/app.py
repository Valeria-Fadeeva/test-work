#!/usr/bin/env python3
"""Приложение"""

import ast
#from base.module_config import *
from base.module_config import Config
from package1.module_main import p1_main


with open('config.cfg', 'r', encoding='utf-8') as f:
    s = f.read().replace('\r\n', '')
    s = s.replace('\n', '')
    s = s.replace(' ', '')

    d = ast.literal_eval(s)

    config = Config(d)

r = p1_main('aaa')
print(r)

#c.set(123)
#print(c.get_all())
print(config.get('name'))
