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
        """ Método principal """
        while True:
            self.iteration += 1
            self.routeslist = []
            self.setRouteInitialNode() if (len(self.iterationList) == 0) else self.searchNode()
            self.printIterationList()

    def setRouteInitialNode(self):
        """
        Inicializar ruta con nodo de inicio.
        """
        route = Route(self.nodeStart.name, self.calculateRouteValue(
            0, self.nodeStart.estimatedCost), 0, self.iteration, self.nodeStart)
        self.routeslist.append(route)
        self.iterationList[self.iteration] = self.routeslist

    def searchNode(self):
        """
        Buscar nodo por ruta óptima
        """
        self.evaluateMininiumRoute()
        for r in self.iterationList[self.iteration-1]:
            if (r.name == self.routeMin):
                self.checkingRouteChildNodes(r)
            else:
                self.routeslist.append(r)

        self.iterationList[self.iteration] = self.routeslist

    def checkingRouteChildNodes(self, route):
        """
        Evaluando la ruta optima de los nodos hijos
        Parameters:
        -----------
        route: Ruta, obligatorio
        """
        childrens = route.node.getChildrenNodes()
        self.validateResultFound(route.node.name, self.nodeEnd.name, childrens)
        for child in childrens:
            nameRoute = self.routeMin + "-" + child.name
            realCost = route.realCost + \
                route.node.childNodesRealCost[child.name]
            value = realCost + child.estimatedCost
            route = Route(nameRoute, value, realCost, self.iteration, child)
            self.routeslist.append(route)

    def validateResultFound(self, routeName, nodeSearch, childrens):
        """
        Validar si llegamos al nodo final.

        Parameters
        -----------
        routeName : str, obligatorio
            nombre del nodo actual que tiene el recorrido (ruta).

        nodeSearch : str, obligatorio
            nombre del nodo destino final.

        childrens : int, obligatorio
            cantidad de nodos hijos que tiene el nodo actual del recorrido.
        """
        if (routeName == nodeSearch and len(childrens) == 0):
            sys.exit()

    def calculateRouteValue(self, realCost, estimatedCost) -> float:
        """
        Devuelve la suma del esfuerzo real + esfuerzo estimado.

        Parameters
        ----------
        realCost : float, obligatorio
            esfuerzo real de un nodo.

        estimatedCost : float, obligatorio
            esfuerzo estimado de un nodo.

        Returns
        --------
        float
            Suma del esfuerzo real + esfuerzo estimado de un nodo
        """
        return realCost + estimatedCost

    def printIterationList(self):
        """
        Imprimir en pantalla la lista de rutas seleccionadas.
        """
        print("[%s] " % (self.iteration), end='')
        counter = 0
        total = len(self.iterationList[self.iteration])
        for r in self.iterationList[self.iteration]:
            counter += 1
            print("%s: %s" % (r.name, r.value), end='') if (
                counter == total) else print("%s: %s, " % (r.name, r.value), end='')
        print("")

    def evaluateMininiumRoute(self):
        """
        Evaluar la ruta de menor esfuerzo
        """
        counter = 0
        for route in self.iterationList[self.iteration-1]:
            counter += 1
            if (counter == 1):
                self.valueMin = route.value
                self.routeMin = route.name
            else:
                if (route.value < self.valueMin):
                    self.valueMin = route.value
                    self.routeMin = route.name

        self.print_highlight(self.routeMin, self.valueMin)

    def print_highlight(self, routeMin, valueMin):
        """
        Imprimir ruta optima en color amarillo.

        Parameters
        ----------
        routeMin : str, obligatorio
            Nombre de ruta optima (secuencia de nodos)

        valueMin : int, obligatorio
            Valor mínimo de la ruta óptima
        """
        CYELLOW = '\33[33m'
        CEND = '\033[0m'
        print("{}Recorrido Minimo : {} : {} {}\n".format(
            CYELLOW, routeMin, valueMin, CEND))
