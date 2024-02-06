# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    isneg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: psaeyang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 21:46:28 by psaeyang          #+#    #+#              #
#    Updated: 2024/02/06 21:49:33 by psaeyang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num = int(input())

if num == 0:
	print("This number is both positive and negative.")
elif num > 0:
	print("This number is positive.")
else:
	print("This number is negative.")