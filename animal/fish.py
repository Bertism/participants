# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:39:14 2024

@author: sinli208
"""

class Fish:
    def __init__(self):
        self.members=["goldfish","lionfish","jellyfish"]
    def printmembers(self):
        for member in self.members:
            print(member)