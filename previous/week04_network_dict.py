#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Represent a simple network of nodes and connections between nodes.
This implementation uses a numpy array of ints as the main data structure.
"""

class Network:
    """
    Simple representation of a network as an adjacency matrix.
    
    The attribute Network.adjMat stores the matrix as a numpy array.
    
    Add nodes and connections using methods:
    Network.add_node()
    Network.add_connection()
    """
    
    def __init__(self, nodeList):
        """
        Required arguments:
        nodeList -- list of node names in the network
        
        Nodes are initialized without connections.
        Add connections with Network.add_connection().
        """
        if type(nodeList) == int:
            nodeList = list(range(1, nodeList+1))
        self.Nodes = {}
        self.nNodes = len(nodeList)
        for node in nodeList:
            self.Nodes[node] = {"connections": set()}
#        self.adjMat = numpy.zeros((nNodes, nNodes), dtype=int)
    
#    def update_repr(self):
#        keys = list(self.Nodes.keys())
#        repr = ['\t'+'\t'.join(keys)]
#        for key in keys:
#            line = [key]
#            for node in keys:
#                if key == node:
#                    line.append('-')
#                elif key in self.Nodes[node]["connections"]:
#                    line.append('1')
#                else:
#                    line.append('0')
#            line = '\t'.join(line)
#            repr.append(line)
#        self.__repr__ = '\n'.join(repr)
        
    def __repr__(self):
        """
        Show the network's adjacency matrix.
        """
        keys = list(self.Nodes.keys())
        repr = ''
        for key in keys:
            repr = repr + '\t' + str(key)
        repr = [repr]
        for key in keys:
            line = [str(key)]
            for node in keys:
                if key == node:
                    line.append('-')
                elif key in self.Nodes[node]["connections"]:
                    line.append('1')
                else:
                    line.append('0')
            line = '\t'.join(line)
            repr.append(line)
        repr = '\n'.join(repr)
        return repr
    
    def add_nodes(self, nodeList):
        """
        Add nNodes new nodes to the network.
        
        Required arguments:
        nNodes -- int number of nodes to add to the network
        
        Nodes are initialized without connections.
        Add connections with Network.add_connection().
        """
        if type(nodeList) == int:
            nodeList = list(range(self.nNodes+1,self.nNodes+nodeList+1))
        for node in nodeList:
            self.Nodes[node] = {"connections": set()}
        self.nNodes = len(self.Nodes.keys())
    
    def add_connection(self, mainNode, connectedNodes, directed=False):
        """
        Add a new connection between mainNode and all nodes in connectedNodes.
        
        Required arguments:
        nodeA, nodeB -- int ID numbers of nodes to connect
        """
        if type(connectedNodes) != list:
            connectedNodes = [connectedNodes]
        for node in connectedNodes:
            self.Nodes[mainNode]["connections"].add(node)
            if not directed:
                self.Nodes[node]["connections"].add(mainNode)


class DirectedNetwork(Network):
    """
    Simple representation of a directed network as an adjacency matrix.
    
    Inherits from Network class (which represents an undirected network).
    Only the method DirectedNetwork.add_connection() differs.
    """
    
    def add_connection(self, nodeA, nodeB):
        """
        Add a new connection from nodeA to nodeB.
        
        Required arguments:
        nodeA, nodeB -- int ID numbers of nodes to connect
        """
        self.adjMat[nodeA, nodeB] = 1