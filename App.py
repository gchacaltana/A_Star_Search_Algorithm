# !/usr/bin/env python
# -*- coding: utf-8 -*-
# App Script
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

import json
import sys
from Node import Node
from AStarAlgorithm import AStarAlgorithm


class App(object):

    def __init__(self):
        self.createNodes()
        self.searchAStarAlgorithm(self.i, self.f)

    def createNodes(self):
        print("Creando nodos")
        self.i = Node("I", 7)
        self.a = Node("A", 6)
        self.b = Node("B", 2)
        self.c = Node("C", 2)
        self.d = Node("C", 1)
        self.f = Node("F", 0)
        self.i.addChild(self.a, 1)
        self.i.addChild(self.b, 4)
        self.a.addChild(self.b, 2)
        self.a.addChild(self.c, 5)
        self.a.addChild(self.f, 12)
        self.b.addChild(self.c, 2)
        self.c.addChild(self.f, 3)

    def searchAStarAlgorithm(self, nodeStart, nodeEnd):
        print("Buscando con Algoritmo A Estrella")
        astar = AStarAlgorithm(nodeStart, nodeEnd)
        astar.run()


if __name__ == "__main__":
    try:
        app = App()
    except (ValueError, FileNotFoundError, AttributeError) as ex:
        print(ex)
