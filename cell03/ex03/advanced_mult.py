# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    advanced_mult.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: psaeyang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 22:53:04 by psaeyang          #+#    #+#              #
#    Updated: 2024/02/06 23:20:11 by psaeyang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 1:
	print("none")
else:
	i = 0
	while i < 11:
		j = 0
		print(f"Table de {i}:", end=' ')
		while j < 11:
			if j == 10:
				print(i * j)
			else:
				print(i * j, end=' ')
			j += 1
		i += 1