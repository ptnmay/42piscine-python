#!/usr/bin/env python3

n1 = int(input("Give me the first number: "))
n2 = int(input("Give me the second number: "))
try:
	print("Thank you!")
	print(n1, '+', n2, '=', n1 + n2)
	print(n1, '-', n2, '=', n1 - n2)
	print(n1, '/', n2, '=', n1 / n2)
	print(n1, 'x', n2, '=', n1 * n2)
except:
	print("Error")