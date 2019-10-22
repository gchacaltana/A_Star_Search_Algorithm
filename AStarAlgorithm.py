# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AStarAlgorithm Class
"""
import sys

__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"


class AStarAlgorithm(object):

    def __init__(self, startNode, finishNode):
        self.startNode = startNode
        self.searchList = []
        self.iteration = 0
        self.finishNode = finishNode

    def run(self):
        
        while True:
            self.iteration+=1
            if (self.iteration ==1):
                self.searchList.append(self.startNode)
                print(self.searchList[0].name)
                sys.exit()
            sys.exit()
