import re

def extract_input(input_line):
    """Extracts sections of a line of an HTTP request log."""
    match = re.match(r'.*"\s*\S+\s+\S+\s+HTTP/1\.[01]"\s+(\d+)\s+(\d+)', input_line)
    if match:
        status_code = match.group(1)
        file_size = int(match.group(2))
        return status_code, file_size
    return None, 0

def print_statistics(total_file_size, status_codes_stats):
    """Prints the accumulated statistics of the HTTP request log."""
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_codes_stats.items()):
        if count > 0:
            print(f"{code}: {count}")

def update_metrics(status_code, file_size, total_file_size, status_codes_stats):
    """Updates the metrics from a given HTTP request log."""
    total_file_size += file_size
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size

def run():
    """Starts the log parser."""
    total_file_size = 0
    status_codes_stats = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    try:
        line_count = 0
        for line in iter(input, ''):
            status_code, file_size = extract_input(line)
            if status_code is not None:
                total_file_size = update_metrics(status_code, file_size, total_file_size, status_codes_stats)
                line_count += 1
                if line_count % 10 == 0:
                    print_statistics(total_file_size, status_codes_stats)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes_stats)

if __name__ == "__main__":
    run()