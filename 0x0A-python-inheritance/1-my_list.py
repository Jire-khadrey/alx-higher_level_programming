#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:13:37 2022
@author: Shittu Rasheed
"""


class MyList(list):
    """
     class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
