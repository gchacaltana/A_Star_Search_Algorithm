# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Node Class
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@outlook.com"

class Node(object):

    def __init__(self, name, estimatedCost):
        self.childNodes = []
        self.childNodesRealCost = {}
        self.name = name
        self.estimatedCost = estimatedCost

    def addChild(self,childNode, realCost):
        """
        Agrega nodo hijo a nodo padre.

        Parameters
        ----------
        childNode : Node Object, obligatorio
            Nodo hijo

        realCost : float, obligatorio
            Esfuerzo real del nodo hijo.
        """

        self.childNodes.append(childNode)
        self.childNodesRealCost[childNode.name] = realCost

    def getChildrenNodes(self):
        """
        Devuelve los nodos hijos del nodo padre.
        """
        return self.childNodes
    
    def getRealCostChildren(self) -> float:
        """
        Devuelve el esfuerzo real por cada nodo hijo del nodo padre.

        Returns
        -------
        float
            esfuerzo real del nodo hijo

        """
        return self.childNodesRealCost
    
    def assignEstimatedCost(self, value):
        """
        Asignar esfuerzo estimado a nodo.

        Parameters
        ----------
        value : float, obligatorio
            esfuerzo estimado

        """
        self.estimatedCost = value