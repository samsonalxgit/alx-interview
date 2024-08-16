#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

# Initialize metrics
file_size_total = 0
status_codes_count = defaultdict(int)
line_count = 0

def print_stats():
    """Print the collected statistics."""
    global file_size_total, status_codes_count
    print(f"File size: {file_size_total}")

    # Sort status codes and print them in ascending order
    for code in sorted(status_codes_count.keys()):
        print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interrupt and print final stats."""
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)

def process_line(line):
    """Process a single line of input."""
    global file_size_total, status_codes_count, line_count

    try:
        # Split the line and parse components
        parts = line.split()
        if len(parts) < 7:
            return

        file_size = int(parts[-1])
        status_code = int(parts[6])
        
        if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
            status_codes_count[status_code] += 1

        file_size_total += file_size
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

    except (ValueError, IndexError):
        # Ignore lines with invalid format or parsing errors
        pass

if __name__ == "__main__":
    for line in sys.stdin:
        process_line(line)
