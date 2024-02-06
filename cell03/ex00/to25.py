# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to25.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: psaeyang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 22:36:30 by psaeyang          #+#    #+#              #
#    Updated: 2024/02/06 22:40:28 by psaeyang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num = int(input("Enter a number less than 25\n"))
if (num > 25):
	print("Error")
while num <= 25:
	print("Inside the loop, my variable is", num)
	num += 1