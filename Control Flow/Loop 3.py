# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:17:30 2019

@author: codePerfectPlus

Looping Example 2
"""

Phone = ['Iphone 10', 'Samsung S10', 'One plus 7 pro', 'Redmi note 7 pro']
accessories = ['Charger 3.0', 'Headphones']

prices ={1:'80000', 2:'70000', 3:'60000', 4:'15000', 5:'1000', 6:'2000'}

for index, c in enumerate(Phone, start =1):
    print((c, prices[index]))
    
for index, a in enumerate(accessories, start =1):
    print((a, prices[index+len(Phone)]))