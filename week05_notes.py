#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:30:51 2019

@author: Noa
"""

#%% Anthony's personal comments 
# Beautiful colors in your Spyder, Noa
# I like your computer. I tend to wish I'd gotten one with an SSD.
# If my computer breaks again, I think I might have to get a new computer, anyway.
# [16:56] I just sent you a dumb text

#%% Dictionary stuff

# example for creating a dictionary of nNodes
x = dict.fromkeys(range(4),[])
x[0].append(1)
# all dictionary key values share the same list

# if two lists a and b
a = []
b = a # b just points to a
b = a.copy() # creates duplicate list

# sets
# .add() and .discard() methods

x = {key: set() for key in range(4)}
x[0] = 1


#%% Modules
# import name_of_file if file in working directory or on path
import network_dict

# Basically runs the file. Any commands inside will happen.
# However, it is run inside its own namespace, not in __main__

# Variables, classes, etc. saved into the imported object's namespace
myNetword = network_dict.Network(4)

# can also import submodules/objects directly into __main__
from network_dict import Network
myNetwork = Network(4)

# Can import whole folders: named after name of module. 
# Modules like this also can have __init__.py files, which tells
# python the folder is a module, and this file runs upon module import

import my_module

# variables defined in the __init__ file are called 'constants' which can
# be used to control the overall way the module works. Usually all-capped
print(my_module.EXAMPLEVAR)

# module.__file__ attribute stores the location of the file that defines
# the module. Can be used to help find relative/absolute path to other
# data which may be stored in the module folder
print(my_module.__file__)

# submodules are .py files within the module folder

# __name__ attribute stores the name of the module
print(my_module.__name__)
# using it on its own tells you which namespace you are in
print(__name__) # returns __main__

# example use
if __name__ == '__main__':
    # code that only runs when script is being executed, not imported
    test = 'example'
    
#%% Git
# Not python commands, but command-line/terminal commands
$ git status # check if git is installed

# navigate to folder where you want to create a git repository
$ cd Documents/Uni/SoSe19/Python/my_repo