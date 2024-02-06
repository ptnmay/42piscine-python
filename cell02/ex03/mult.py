# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: psaeyang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 22:23:28 by psaeyang          #+#    #+#              #
#    Updated: 2024/02/06 22:34:13 by psaeyang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))
ans = first * second
print(first, 'x', second, '=', ans)

if (ans > 0):
	print("The result is positive.")
elif (ans < 0):
	print("The result is negative.")
else:
	print("The result is positive and negative.")