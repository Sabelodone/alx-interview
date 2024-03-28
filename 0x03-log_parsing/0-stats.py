#!/usr/bin/python3

import sys
import signal

# Dictionary to store status code counts
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_file_size = 0
line_count = 0

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    global total_file_size
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def parse_line(line):
    parts = line.split()
    if len(parts) != 10:
        return None, None
    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except ValueError:
        return None, None

def main():
    global total_file_size, line_count
    signal.signal(signal.SIGINT, signal_handler)
    for line in sys.stdin:
        status_code, file_size = parse_line(line.strip())
        if status_code is not None and status_code in status_counts:
            status_counts[status_code] += 1
            total_file_size += file_size
            line_count += 1
        if line_count % 10 == 0:
            print_stats()

if __name__ == "__main__":
    main()
