#!/usr/bin/env python3

import sys
import os


def newstr(s):
	#s = s[s.index("x") - 2] + s[s.index("x") - 1] + s[s.index("x") + 1:s.index(".")]
	s = s[s.index("x") - 1] + s[s.index("x") + 1:s.index(".")]
	return s

list = sorted(set([newstr(i) for i in sorted(os.listdir(sys.argv[1])) if ".srt" in i]))
"""
print(list)
print(len(list))
print()
"""
list1 = [i for i in sorted(os.listdir(sys.argv[2])) if sys.argv[3] in i]
#print(list1)
#print(len(list1))


for i, j in zip(list1, list):
	os.rename(sys.argv[2] + i, sys.argv[2] + j + "." + sys.argv[3])
	print(i, "-->", j + "." + sys.argv[3])
	print("Success")

