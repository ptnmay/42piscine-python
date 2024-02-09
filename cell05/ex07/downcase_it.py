#!/usr/bin/env python3

import sys

len = len(sys.argv)

if len == 2:
	print(sys.argv[1].lower())
else:
	print("none")