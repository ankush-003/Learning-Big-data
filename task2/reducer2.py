#!/usr/bin/env python3

import sys

current_product = None
total_rating = 0
total_quantity = 0
total_num = 0

for line in sys.stdin:
	product, value = line.strip().split('\t')
	quantity, rating = map(int, value.split(','))

	if product == current_product:
		total_rating += rating
		total_quantity += quantity
		total_num += 1
	else:
		if current_product:
				print(f"{current_product}\t{total_quantity:.0f},{round(total_rating / total_num, 0):.0f}")
		current_product = product
		total_rating = rating
		total_quantity = quantity
		total_num = 1

if current_product:
	print(f"{current_product}\t{total_quantity:.0f},{round(total_rating / total_num, 0):.0f}")
