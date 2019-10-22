# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Node Class
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

class Node(object):

    def __init__(self, name):
        self.childNodes = []
        self.childNodesRealCost = {}
        self.name = name
        self.estimatedCost = 0

    def addChild(self,childNode, realCost):
        # Agrega nodo hijo
        self.childNodes.append(childNode)
        self.childNodesRealCost[childNode.name] = realCost

    def getChildrenNodes(self):
        # Devuelve los nodos hijos del nodo padre
        return self.childNodes
    
    def getRealCostChildren(self):
        # Devuelve el esfuerzo real por cada nodo hijos del nodo padre
        return self.childNodesRealCost
    
    def assignEstimatedCost(self, value):
        # Asignar costo estimado a nodo.
        self.estimatedCost = value