#!/usr/bin/env python3

import re


# open the file prog.log and output a new file that removed all duplicated lines
def remove_dup():
    with open('prog.log', 'r') as f:
        lines = f.readlines()
        lines_set = set(lines)
        unique_lines = list(lines_set)
        with open('prog2.log', 'w') as f:
            for line in unique_lines:
                f.write(line)
 
with open('prog2.log') as f:
 
 
    for line in f:
        match = re.search(r'[a-zA-z]+, \d+, \d+, \d*-\d*-\d*', line)
        if match:
            print()
 