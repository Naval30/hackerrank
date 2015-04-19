#!/usr/bin/python -tt

import sys

def unique(atrList):
    for character in atrList:
        if character == ' ':
            atrList = atrList.replace(' ','%20') 
    return atrList               # Check value from the array
            

atrList = sys.argv


print(unique(atrList[1]))
