#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    table, data = line.split("\t",1)
    data = data.split("\t")
    # print(type, len(data))
    if(table == "order"):
        _, customer_id, product_id, quantity,_ = data
        rating = 0
	# if(table == "review"):
    else:
        _, product_id, customer_id, rating,_ = data
        quantity = 0

	# key: product_id, customer_id
	# value: quantity, rating
    print(f"{product_id},{customer_id}\t{quantity},{rating}")
