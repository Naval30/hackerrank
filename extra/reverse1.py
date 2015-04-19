#!/usr/bin/python -tt
import sys




def reverse(strs):
	j = strs[::-1]
	return j


strs = sys.argv

print(reverse(strs[1]))