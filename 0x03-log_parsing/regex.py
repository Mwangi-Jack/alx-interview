#!/usr/bin/env python3
import re
import sys


def match_pattern():
    """match regex pattern"""

    status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    total_file_size = 0
    count = 0
    for line in sys.stdin:
        count += 1
        # Regular expression pattern to extract components
        pattern = r'(?P<ip>[\d.]+) - \[(?P<date>[^\]]+)\] "(?P<method>\w+) (?P<url>[^ ]+) (?P<protocol>[^"]+)" (?P<status>\d+) (?P<size>\d+)'

        match = re.match(pattern, line)

        if match:
            file_size = match.group('size')
            file_status = int(match.group('status'))
            total_file_size += int(file_size)
            if isinstance(file_status, int):
                print("STATUS IS INTEGER")
                status_dict[file_status] += 1

            print(f'Line {count}. Status: {file_status} ::: File Size: {file_size}')


    print(status_dict)
    print(total_file_size)



match_pattern()
