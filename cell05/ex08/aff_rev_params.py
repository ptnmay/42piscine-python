#!/usr/bin/python3

import sys

len = len(sys.argv)

if len < 3:
	print("none")
else:
	print(sys.argv[:0:-1])