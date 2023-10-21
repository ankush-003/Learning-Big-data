#!/usr/bin/env python3

import sys

for line in sys.stdin:
	key, value = line.strip().split('\t')
	product_id, _ = key.split(',')
	values = value.split(',')
	_, rating= map(int, values)
	if(rating > 0 and rating < 3):
		print(f'{product_id}\t{value}')
