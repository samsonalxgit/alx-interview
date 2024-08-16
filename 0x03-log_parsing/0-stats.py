#!/usr/bin/python3
"""
module for script that reads stdin line by line and computes metrics
"""
import sys


def log_stats():
    """Reads from stdin from piping"""
    count = 0
    total_size = 0
    status_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    valid_codes_count = {}

    try:
        for line in sys.stdin:
            if count == 10:
                print("File size: {}".format(total_size))
                for status in sorted(valid_codes_count):
                    print('{}: {}'.format(status, valid_codes_count[status]))
                count = 1
            else:
                count += 1

            fields = line.split()
            try:
                file_size = int(fields[-1])
                total_size += file_size
            except ValueError:
                pass

            try:
                valid_codes = fields[-2]
                if valid_codes in status_code:
                    if valid_codes_count.get(valid_codes, -1) == -1:
                        valid_codes_count[valid_codes] = 1
                    else:
                        valid_codes_count[valid_codes] += 1
            except (IndexError, ValueError, KeyError):
                pass

        print("File size: {}".format(total_size))
        for status in sorted(valid_codes_count):
            print('{}: {}'.format(status, valid_codes_count[status]))

    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for status in sorted(valid_codes_count):
            print('{}: {}'.format(status, valid_codes_count[status]))


if __name__ == "__main__":
    log_stats()
