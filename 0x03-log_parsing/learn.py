#!/usr/bin/env python3

# def read_file() :
#     """reading a file"""
#     count = 0
#     with open('file.txt', 'r', encoding='utf-8') as f:
#         file = f.readline()
#         while file:
#             count += 1
#             file = f.readline()
#             print(f'Line {count} ::: {file} \n')

#     print(f'The file has {count} lines.')

# read_file()


import sys


def write_file():
    """writing to a file"""
    count = 0

    for line in sys.stdin:
        if count % 10 == 0:
            print("Multiple of 10:: ", count)
        print(f'Line {count} ::: {line}')
        count += 1

write_file()
