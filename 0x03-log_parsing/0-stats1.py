import sys
import signal
import re
from collections import defaultdict

# Initialize metrics
total_file_size = 0
status_code_count = defaultdict(int)
line_count = 0

# Define the regex pattern for the log line
pattern = (
    r'(?P<ip>[\d.]+) - \['
    r'(?P<date>[^\]]+)\] '
    r'"(?P<method>\w+) '
    r'(?P<url>[^ ]+) '
    r'(?P<protocol>[^"]+)" '
    r'(?P<status>\d+) '
    r'(?P<size>\d+)'
)

def print_statistics():
    """Print the collected statistics."""
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_count):
        print(f"{code}: {status_code_count[code]}")

def signal_handler(sig, frame):
    """Handle the Ctrl+C signal."""
    print("\nKeyboard interrupt received. Printing statistics:")
    print_statistics()
    sys.exit(0)

# Set up the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read lines from stdin
    for line in sys.stdin:
        line = line.strip()
        match = re.match(pattern, line)
        if match:
            # Extract the relevant information
            status_code = match.group('status')
            file_size = int(match.group('size'))

            # Update the total file size
            total_file_size += file_size

            # Update the status code count
            if status_code.isdigit():
                status_code_count[int(status_code)] += 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()
                print("")

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("\nKeyboard interrupt received. Printing statistics:")
    print_statistics()
    sys.exit(0)

# Print final statistics after EOF
print_statistics()
