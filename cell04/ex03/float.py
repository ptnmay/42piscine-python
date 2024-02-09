#!/usr/bin/env python3

from decimal import Decimal

num = float(input("Give me a number: "))
try:
	if Decimal(num) % 1 == 0:
		print("This number is an integer.")
	else:
		print("This number is a decimal.")
except:
	print("Error")