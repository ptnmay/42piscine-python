# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: psaeyang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 21:51:05 by psaeyang          #+#    #+#              #
#    Updated: 2024/02/06 22:08:38 by psaeyang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

password = "Python is awesome"
check = input()

if (password == check):
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")