# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    float.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: psaeyang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 23:45:08 by psaeyang          #+#    #+#              #
#    Updated: 2024/02/07 13:58:52 by psaeyang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from decimal import Decimal

num = float(input("Give me a number: "))
if Decimal(num) % 1 == 0:
	print("This number is an integer.")
else:
	print("This number is a decimal.")