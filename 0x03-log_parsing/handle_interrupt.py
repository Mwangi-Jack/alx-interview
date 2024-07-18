#!/usr/bin/env python3

import sys
import signal


LINE_COUNT = 0
STATUS_CODE_DICT = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
TOTAL_FILE_SIZE = 0

def interrupt_handler(sig, frame):
    """keyboardInterrupt handler"""
    print(f'File size: {TOTAL_FILE_SIZE}')
    for k, v in STATUS_CODE_DICT.items():
        print(f'{k}: {v}')

    sys.exit(0)


for line in sys.stdin:
	LINE_COUNT += 1
	print(f'Line {LINE_COUNT} ::: {line}')


signal.signal(signal.SIGINT, interrupt_handler)

