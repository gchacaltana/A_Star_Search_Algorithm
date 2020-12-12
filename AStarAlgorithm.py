# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AStarAlgorithm Class
"""
import sys

__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@outlook.com"

from Route import Route


class AStarAlgorithm(object):

    def __init__(self, nodeStart, nodeEnd):
        """
        Parameters
        ----------
        nodeStart : Node Object, obligatorio
            Nodo de inicio de la ruta.
        nodeEnd : Node Object, obligatorio
            Nodo final de la ruta.
        """
        self.iteration = 0
        self.iterationList = {}
        self.routeList = []
        self.nodeStart = nodeStart
        self.nodeEnd = nodeEnd
        self.valueMin = 0
        self.routeMin = False

    def run(self):
        """ main method """
        while True:
            self.iteration += 1
            self.routeslist = []
            self.searchInitialNode() if (len(self.iterationList) == 0) else self.searchNode()
            self.printIterationList()

    def searchInitialNode(self):
        route = Route(self.nodeStart.name, self.calculateRouteValue(
            0, self.nodeStart.estimatedCost), 0, self.iteration, self.nodeStart)
        self.routeslist.append(route)
        self.iterationList[self.iteration] = self.routeslist

    def searchNode(self):
        self.evaluateMininiumRoute()
        for r in self.iterationList[self.iteration-1]:
            if (r.name == self.routeMin):
                childrens = r.node.getChildrenNodes()
                self.validateResultFound(
                    r.node.name, self.nodeEnd.name, childrens)
                for child in childrens:
                    nameRoute = self.routeMin + "-" + child.name
                    realCost = r.realCost + \
                        r.node.childNodesRealCost[child.name]
                    value = realCost + child.estimatedCost
                    route = Route(nameRoute, value, realCost,
                                  self.iteration, child)
                    self.routeslist.append(route)
            else:
                self.routeslist.append(r)
        self.iterationList[self.iteration] = self.routeslist

    def validateResultFound(self, routeName, nodeSearch, childrens):
        if (routeName == nodeSearch and len(childrens) == 0):
            sys.exit()

    def calculateRouteValue(self, realCost, estimatedCost):
        return realCost + estimatedCost

    def printIterationList(self):
        print("[%s] " % (self.iteration), end='')
        counter = 0
        total = len(self.iterationList[self.iteration])
        for r in self.iterationList[self.iteration]:
            counter += 1
            print("%s: %s" % (r.name, r.value), end='') if (counter == total) else print("%s: %s, " % (r.name, r.value), end='')
        print("")

    def evaluateMininiumRoute(self):
        counter = 0
        for route in self.iterationList[self.iteration-1]:
            counter += 1
            if (counter == 1):
                self.valueMin = route.value; self.routeMin = route.name
            else:
                if (route.value < self.valueMin):
                    self.valueMin = route.value; self.routeMin = route.name
        CYELLOW = '\33[33m'; CEND = '\033[0m'
        print(CYELLOW + "Recorrido Minimo : %s : %s\n" %
              (self.routeMin, self.valueMin) + CEND)
