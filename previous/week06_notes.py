#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:13:29 2019

@author: anthony819
"""

import sqlite3

#%%
# connect to existing or create database
conn = sqlite3.connect('python.db')

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS subjects;')
cursor.execute('CREATE TABLE subjects (id INTEGER PRIMARY KEY, name TEXT UNIQUE, age INTEGER);')

names = ['luke', 'dave', 'percy']
ages = [37, 52, 29]

for name, age in zip(names, ages):
    cursor.execute('INSERT INTO subjects (name, age) VALUES(?, ?);', (name, age))

cursor.execute('SELECT * FROM subjects')
for result in cursor:
    print(result)
#cursor.fetchall()

# incomplete
cursor.execute('CREATE TABLE trials (id INTEGER PRIMARY KEY, subject INTEGER, rt FLOAT)')

# JOIN statement (combine two tables by id columns), WHERE statement (like if statement)

conn.commit()
conn.close()
