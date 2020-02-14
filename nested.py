#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "???"

import sys


def is_nested(line):
    token_1 = '(*'
    token_2 = '*)'
    brackets_dict = {
        token_2: token_1,
        ']': '[',
        '>': '<',
        ')': '(',
        '}': '{'
    }
    bracket_list = []
    index_counter = 0
    while line:
        token_3 = line[0]
        if line.startswith(token_1) or line.startswith(token_2):
            token_3 = line[:2]
        if token_3 in brackets_dict.values():
            bracket_list.append(token_3)
            line = line[len(token_3):]
            index_counter += 1
        elif token_3 in brackets_dict.keys():
            if bracket_list and brackets_dict[token_3] == bracket_list[-1]:
                bracket_list.pop()
                line = line[len(token_3):]
                index_counter += 1
            else:
                index_counter += 1
                return 'NO ' + str(index_counter)
        else:
            line = line[len(token_3):]
            index_counter += 1
    if bracket_list:
        return 'NO ' + str(index_counter)
    return 'YES'
    """Validate a single input line for correct nesting"""


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    with open("input.txt") as f:
        with open("output.txt", 'w') as o:
            for line in f:
                result = is_nested(line)
                print(result)
                o.writelines(result)


if __name__ == '__main__':
    main(sys.argv[1:])
