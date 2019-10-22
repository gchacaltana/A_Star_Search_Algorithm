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

    def __init__(self, jsonfile, nodeSearched):
        self.listNodes = []
        self.keyChildren = "children_nodes"
        self.keyEstimatedCost = "estimated_cost"
        self.parentNode = {}
        self.jsonfile = jsonfile
        self.nodeSearched = nodeSearched

    def main(self):
        self.openfile()
        self.createNodes()
        self.showNodes()
        self.runAStarAlgorithm()

    def openfile(self):
        print("\n1. Abriendo fichero.")
        with open(self.jsonfile, "r") as f:
            self.routes = json.load(f)

    def createNodes(self):
        i = 0
        print("\n2. Creando nodos")
        for node in self.routes:
            i += 1
            self.parentNode[i] = Node(node)
            self.assignChildrenNodes(i, node)
            self.assignEstimatedCost(i, node)

    def assignChildrenNodes(self, i, node):
        if self.routes[node].get(self.keyChildren) == None:
            raise Exception(
                "El nodo %s no cumple con el formato de nodos hijos." % node)
        else:
            for child, cost in self.routes[node][self.keyChildren].items():
                childNode = Node(child)
                self.parentNode[i].addChild(childNode, cost)
            self.listNodes.append(self.parentNode[i])

    def assignEstimatedCost(self, i, node):
        if self.routes[node].get(self.keyEstimatedCost) == None:
            raise Exception(
                "El nodo %s no cumple con el formato de costo estimado." % node)
        else:
            self.parentNode[i].assignEstimatedCost(
                self.routes[node][self.keyEstimatedCost])

    def showNodes(self):
        # Devuelve lista de nodos creados
        print("\nLista de Nodos")
        print("********************")
        for n in self.listNodes:
            print("Nodo: %s" % n.name)
            print("Costo Estimado: %d" % n.estimatedCost)
            print("Nodos Hijos y costo real\n")
            print(n.getRealCostChildren())
            print("\n-----------------------\n")

    def runAStarAlgorithm(self):
        print("4. Ejecutando Algortimo A Estrella")
        astar = AStarAlgorithm(self.parentNode[1], self.nodeSearched)
        astar.run()

if __name__ == "__main__":
    try:
        app = App("routes.json", "F")
        app.main()
    except (ValueError, FileNotFoundError, AttributeError) as ex:
        print(ex)
