#!/usr/bin/python3
"""Log Parsing
Write a script that reads stdin line by line and computes metrics:
"""
import sys
import signal

# Define the status codes to track
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

def compute_statistics(lines):
    total_size = 0
    status_count = {code: 0 for code in STATUS_CODES}

    for line in lines:
        try:
            # Split the line and extract the file size and status code
            _, _, _, _, _, status_code_str, file_size_str = line.split(" ")
            status_code = int(status_code_str)
            file_size = int(file_size_str)

            # Update the total file size
            total_size += file_size

            # Update the status code count if it's in the desired codes
            if status_code in status_count:
                status_count[status_code] += 1

        except ValueError:
            # Skip lines with incorrect format
            continue

    return total_size, status_count

def print_statistics(total_size, status_count):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_count.keys()):
        count = status_count[status_code]
        if count > 0:
            print(f"{status_code}: {count}")

def signal_handler(sig, frame):
    # Handle CTRL+C
    print("\nProgram interrupted. Printing current statistics:")
    print_statistics(total_file_size, status_code_count)
    sys.exit(0)

if __name__ == "__main__":
    total_file_size = 0
    status_code_count = {code: 0 for code in STATUS_CODES}
    lines_buffer = []

    # Register the signal handler for CTRL+C
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            lines_buffer.append(line.strip())

            # Process and print statistics every 10 lines
            if len(lines_buffer) >= 10:
                total_file_size, status_code_count = compute_statistics(lines_buffer)
                print_statistics(total_file_size, status_code_count)
                lines_buffer = []

    except KeyboardInterrupt:
        # Handle manual interrupt (CTRL+C)
        print("\nProgram interrupted. Printing current statistics:")
        print_statistics(total_file_size, status_code_count)
        sys.exit(0)

    # Print final statistics when there are remaining lines
    if lines_buffer:
        total_file_size, status_code_count = compute_statistics(lines_buffer)
        print_statistics(total_file_size, status_code_count)
