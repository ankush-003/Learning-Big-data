#!/usr/bin/env python3

import sys

for line in sys.stdin:
	product_id, quantity = line.strip().split('\t')
	print(f"{product_id}\t{quantity}")
