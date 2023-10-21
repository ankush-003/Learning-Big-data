#!/usr/bin/env python3

import sys
import json

def parse_data(line: str) -> list[str, int, int]:
    """
    function to parse the line string
    input: line string
    output: name, runs, balls
    """
    data = json.loads(line)
    name = data.get("name")
    runs = int(data.get("runs"))
    balls = int(data.get("balls"))
    return [name, runs, balls]
in_dict= json.loads(sys.stdin) 
print(in_dict)
"""
for line in sys.stdin:
    line = line.strip()
    # checking for '[' and ']' 
    if line.find('[') != -1 or line.find(']') != -1:
	    continue

    # removing trailing ','
    if line.endswith(','):
        line = line[:-1]

    name, runs, balls = parse_data(line)
    strike_rate = 0 if balls == 0 else round((runs / balls) * 100, 3)
    print(f"{name}\t{strike_rate}")
    """
