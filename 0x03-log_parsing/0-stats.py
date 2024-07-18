#!/usr/bin/python3
"""Log Parsing"""

import sys
import re
import signal


LINE_COUNT = 0
STATUS_CODE_DICT = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
TOTAL_FILE_SIZE = 0
REGEX_PATTERN = (
    r'(?P<ip>[\d.]+) - \['
    r'(?P<date>[^\]]+)\] '
    r'"(?P<method>\w+) '
    r'(?P<url>[^ ]+) '
    r'(?P<protocol>[^"]+)" '
    r'(?P<status>\d+) '
    r'(?P<size>\d+)'
)


def interrupt_handler(sig, frame):
    """keyboardInterrupt handler"""
    print(f'File size: {TOTAL_FILE_SIZE}')
    for k, v in STATUS_CODE_DICT.items():
        print(f'{k}: {v}')

    sys.exit(0)


for line in sys.stdin:
    if LINE_COUNT % 10 == 0 and LINE_COUNT != 0:
        print(f'File size: {TOTAL_FILE_SIZE}')
        for key, value in STATUS_CODE_DICT.items():
            print(f'{key}: {value}')

    match = re.match(REGEX_PATTERN, line)

    if match:
        file_size = int(match.group('size'))
        status = int(match.group('status'))

        TOTAL_FILE_SIZE += file_size

        if isinstance(status, int):
            STATUS_CODE_DICT[status] += 1

    LINE_COUNT += 1

    signal.signal(signal.SIGINT, interrupt_handler)
