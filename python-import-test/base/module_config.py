#!/usr/bin/env python3
"""file class config"""

class Config:
    """class config"""

    def __init__(self, d):
        """class config constructor"""
        if isinstance(d, dict):
            self.d = d
        else:
            raise Exception(f'{d} in not dict')

    def set(self, var):
        """class config set"""
        self.d[var] = var
        return True

    def get(self, var):
        """class config get"""
        return self.d[var]

    def get_all(self):
        """class config get_all"""
        return self.d.items()
