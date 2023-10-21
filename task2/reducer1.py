#!/usr/bin/env python3

import sys
# define the product-customer type
product = dict[str | None, int, int]

# Initialize variables to hold the current product and customer IDs
current_product:product = {"id": None, "t_quantity": 0, "t_rating": 0}

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")
    quantity, rating = map(int, value.split(","))
    
    # Check if the product and customer IDs have changed
    if key != current_product.get("id"):
        # If they have changed, output the previous product-customer pair and its total quantity and rating
        if current_product.get("id"):
            print(f"{current_product.get('id')}\t{current_product.get('t_quantity')},{current_product.get('t_rating')}")
        # Update the current product-customer and reset the accumulators
        current_product = {"id": key, "t_quantity": 0, "t_rating": 0}

    # Update the accumulators
    current_product["t_quantity"] += quantity
    current_product["t_rating"] += rating
    

# Output the last product-customer pair and its total quantity and rating
if current_product.get("id", None):
    print(f"{current_product.get('id')}\t{current_product.get('t_quantity')},{current_product.get('t_rating')}")
