# !/usr/bin/env python
# -*- coding: utf-8 -*-
# App Main
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@outlook.com"

import sys
from Node import Node
from AStarAlgorithm import AStarAlgorithm

class App(object):

    def __init__(self):
        print("Creando nodos: ", end = '')
        self.i = Node("I", 7)
        self.a = Node("A", 6)
        self.b = Node("B", 2)
        self.c = Node("C", 1)
        self.f = Node("F", 0)
        self.i.addChild(self.a, 1)
        self.i.addChild(self.b, 4)
        print("I ", end ='')
        self.a.addChild(self.b, 2)
        self.a.addChild(self.c, 5)
        self.a.addChild(self.f, 12)
        print("A ", end ='')
        self.b.addChild(self.c, 2)
        print("B ", end ='')
        self.c.addChild(self.f, 3)
        print("C ", end ='')
        print("F ", end ='')

    def searchAStarAlgorithm(self):
        print("\nBuscando ruta optima con Algoritmo A*")
        astar = AStarAlgorithm(self.i, self.f)
        print("Nodo Inicial: %s -----> Nodo Final %s" % (self.i.name, self.f.name))
        astar.run()


if __name__ == "__main__":
    try:
        app = App()
        app.searchAStarAlgorithm()
    except (ValueError, FileNotFoundError, AttributeError) as ex:
        print(ex)
