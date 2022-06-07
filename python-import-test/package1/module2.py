#!/usr/bin/env python3
"""p1_m2"""

import sys
sys.path.append('..')
from package2.module_main import p2_main


def p1_m2(s: str) -> str:
    """func p1_m2"""

    s += p2_main(s)

    return s
