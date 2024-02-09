#!/usr/bin/python3

import sys
import re

len = len(sys.argv)

if len != 3:
	print("none")
else:
	first = sys.argv[1]
	second = sys.argv[2];
	n = second.count(first)
	if (n > 0):
		print(n)
	else:
		print('none')
