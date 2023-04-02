# Resolver-Tester_and_Gatherer
This Python script tests the responsiveness of DNS resolvers, can gather them from a file/URL, and filter by speed. Results can be output to a file, randomized, and shown for alive/non-alive resolvers. Queries are sent to each resolver to check its status.


# DNS Resolver Tester
This is a Python script that tests a list of DNS resolvers to determine which ones are alive and how fast they respond.

## Usage
usage: dns_resolver_tester.py [-h] [-a] [-s {slow,medium,fast}] [-r] [-o FILE] [-v] [FILE]

Test a list of DNS resolvers

positional arguments:
  FILE                  File or URL containing list of DNS resolvers (default: https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt)

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             Show both alive and non-alive resolvers (default: show only alive resolvers)
  -s {slow,medium,fast}, --speed {slow,medium,fast}
                        Filter resolvers by response speed
  -r, --randomize       This will randomize the list of resolvers
  -o FILE, --output FILE
                        Output the results to a file
  -v, --verbose         If printing to a file this will also make it print the results

## Example
### To test a list of resolvers in resolvers.txt and output the results to a file named results.txt:
python3 dns_resolver_tester.py resolvers.txt -o results.txt
### To test a website with a list of resolvers and only grab the fast ones
python3 dns_resolver_tester.py https://example.com/resolvers.txt -s fast
### To gather and test the list of resolvers
python3 dns_resolver_tester.py
### To test a gathered list of resolvers, radomize the list and keep only the fast ones output them to resolvers.txt but show every tested one even the ones that failed
python3 dns_resolver_tester.py --speed fast --output resolvers.txt --all --randomize
