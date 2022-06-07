#!/usr/bin/env python3

import os
import sys


c = sys.argv[0]
fname = os.path.split(c)[-1]
p = c.replace(fname, '')

result_dir = os.path.abspath(os.path.join(p, 'result'))

pobj = [os.path.abspath(os.path.join(result_dir, x)) for x in os.listdir(result_dir)]
for p in pobj:
    if os.remove(p):
        print('remove', p)
