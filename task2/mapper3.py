#!/usr/bin/env python3

import sys

for line in sys.stdin:
	product_id, data = line.strip().split('\t')
	quantity, _ = data.split(',')
	print(f"{product_id}\t{quantity}")
