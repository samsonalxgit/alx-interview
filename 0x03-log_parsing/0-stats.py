#!/usr/bin/python3

'''log_parsing'''
import sys
import re
from collections import defaultdict

def print_stats(file_size_sum, status_codes):
    print(f"File size: {file_size_sum}")
    for status_code in sorted(status_codes):
        print(f"{status_code}: {status_codes[status_code]}")

def main():
    file_size_sum = 0
    status_codes = defaultdict(int)
    line_count = 0
    
    # Regular expression to match valid log lines
    log_pattern = re.compile(
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    )
    
    try:
        for line in sys.stdin:
            match = log_pattern.match(line)
            if match:
                status_code = match.group(3)
                file_size = int(match.group(4))
                
                file_size_sum += file_size
                status_codes[status_code] += 1
                line_count += 1
                
                if line_count % 10 == 0:
                    print_stats(file_size_sum, status_codes)
                    
    except KeyboardInterrupt:
        # Handle keyboard interruption
        print_stats(file_size_sum, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()

