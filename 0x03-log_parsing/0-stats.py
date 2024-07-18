#!/usr/bin/python3
"""Log Parsing"""

import sys
import re
import signal
from tkinter import S


LINE_COUNT = 0
STATUS_CODE_DICT = {}
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


def print_stats():
    """prints current statistics"""
    print(f'File size: {TOTAL_FILE_SIZE}')
    for key in sorted(STATUS_CODE_DICT):
        print(f'{key}: {STATUS_CODE_DICT[key]}')

def interrupt_handler(sig, frame):
    """keyboardInterrupt handler"""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, interrupt_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        if LINE_COUNT % 10 == 0 and LINE_COUNT != 0:
            print_stats()

        match = re.match(REGEX_PATTERN, line)

        if match:
            file_size = int(match.group('size'))
            status = int(match.group('status'))

            TOTAL_FILE_SIZE += file_size

            if isinstance(status, int):
                if status in STATUS_CODE_DICT:
                    STATUS_CODE_DICT[status] += 1
                else:
                    STATUS_CODE_DICT[status] = 1

        LINE_COUNT += 1

except KeyboardInterrupt:
    print_stats()
