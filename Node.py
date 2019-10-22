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
        self.name = name

    def addChild(self,node):
        # Agrega nodo hijo
        self.childNodes.append(node)

    def getChildrenNodes(self):
        # Devuelve los nodos hijos del nodo.
        return self.childNodes