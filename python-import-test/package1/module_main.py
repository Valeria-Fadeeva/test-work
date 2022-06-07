#!/usr/bin/env python3
"""p1_main"""


from package1.module1 import p1_m1
from package1.module2 import p1_m2
from package1.module3 import p1_m3


def p1_main(s: str) -> str:
    """func p1_main"""

    s += p1_m1(s)
    s += p1_m2(s)
    s += p1_m3(s)

    return s
