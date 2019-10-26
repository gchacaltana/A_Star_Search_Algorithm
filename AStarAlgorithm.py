# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AStarAlgorithm Class
"""
import sys

__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"


class AStarAlgorithm(object):

    def __init__(self, nodeStart, nodeEnd):
        self.tour = []
        self.searchTour = []
        self.tour.append(nodeStart)
        self.iteration = 0
        self.nodeEnd = nodeEnd

    def run(self):

        while True:
            self.iteration += 1
            if (self.iteration == 1):
                print("[%s] %s: %d + %d" % (self.iteration,
                                            self.tour[0].name, 0, self.tour[0].estimatedCost))
                childrens = self.tour[0].getRealCostChildren()
                searchTour
            else:
                print("[%s] %s: %d + %d" % (self.iteration,
                                            self.searchList[0].name, 0, self.searchList[0].estimatedCost))
            sys.exit()
