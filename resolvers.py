#!/usr/bin/env python3

import argparse
import socket
import time
import urllib.request
import random

DEFAULT_URL = "https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt"

def parse_args():
    parser = argparse.ArgumentParser(description="Test a list of DNS resolvers")
    parser.add_argument("file", metavar="FILE", nargs="?", default=DEFAULT_URL,
                        help=f"File or URL containing list of DNS resolvers (default: {DEFAULT_URL})")
    parser.add_argument("-a", "--all", action="store_true",
                        help="Show both alive and non-alive resolvers (default: show only alive resolvers)")
    parser.add_argument("-s", "--speed", choices=["slow", "medium", "fast"],
                        help="Filter resolvers by response speed")
    parser.add_argument("-r", "--randomize", action="store_true",
                        help="This will randomize the list of resolvers")
    parser.add_argument("-o", "--output", metavar="FILE",
                        help="Output the results to a file")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="If printing to a file this will also make it print the results")
    return parser.parse_args()


def get_resolvers(file):
    if file.startswith("http"):
        with urllib.request.urlopen(file) as f:
            resolvers = f.read().decode().splitlines()
    else:
        with open(file) as f:
            resolvers = f.read().splitlines()
    return resolvers

def test_resolver(resolver, filter_speed, all_ip, output_file, verbose):
    try:
        start_time = time.time()
        socket.create_connection((resolver, 53), timeout=5)
        elapsed_time = time.time() - start_time
        if not filter_speed or filter_speed == "fast" and elapsed_time <= 0.5 or filter_speed == "medium" and elapsed_time <= 1 or filter_speed == "slow" and elapsed_time <= 5:
            result = f"{resolver} is alive - response time: {elapsed_time:.3f}s"
            file_result = f"{resolver}"
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(file_result + '\n')
                    if verbose == True:
                        print(result)
            else:
                print(result)
    except (socket.error, UnicodeError, TimeoutError):
        if all_ip == True:
            if filter_speed:
                result = f"{resolver} is not alive"
            else:
                result = f"{resolver} is not alive - response time: N/A"
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(result + '\n')
            else:
                print(result)



def main():
    args = parse_args()
    resolvers = get_resolvers(args.file)
    if args.randomize:
        random.shuffle(resolvers)
    for resolver in resolvers:
        test_resolver(resolver, args.speed, args.all, args.output, args.verbose)

if __name__ == "__main__":
    main()
