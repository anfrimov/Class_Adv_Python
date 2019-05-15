#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:39:36 2019

@author: anthony819
"""

import numpy as np

class Network:

    def __init__(self, nNodes, directed=False):
        self.nNodes = nNodes
        self.adjMat = np.zeros((nNodes, nNodes), dtype=int)
        self.directed = directed
        
    # define what object does when: print(object)    
    def __str__(self):
        return str(self.adjMat)
    
    # define what object does when object entered by itself
    def __repr__(self):
        return self.__str__()

    def add_edge(self, nodeA, nodeB):
        self.adjMat[nodeA, nodeB] = 1
        if not self.directed:
            self.adjMat[nodeB, nodeA] = 1
            
    def add_nodes(self, num):
        total = self.nNodes + num
        self.adjMat = np.append(
                self.adjMat, 
                np.zeros([num, self.nNodes], dtype=int), 
                axis=0
                )
        self.adjMat = np.append(
                self.adjMat, 
                np.zeros([total, num], dtype=int), 
                axis=1
                )
        self.nNodes = total
        
class DirectedNetwork(Network):
    
    # everything in this directed network object is inherited from the
    # network object. add_edge method is overwritten
    def add_edge(self, nodeA, nodeB):
        self.adjMat[nodeA, nodeB] = 1
        
    
myNetwork = Network(4)

myNetwork.add_nodes(2)

print(myNetwork)

#print(myNetwork)