import argparse
import netaddr
import sys


def main():
    parser = argparse.ArgumentParser(
        prog=__file__,
        description='Check if an IP is in one of specified ranges',        
    )
    parser.add_argument('ip')
    args = parser.parse_args()
    ip_address = args.ip
    
    for range in (line.strip() for line in sys.stdin):
        if ip_address in netaddr.IPNetwork(range):
            print(f'{ip_address} is in {range}.')
            sys.exit(0)
        
    print(f'{ip_address} is not in any of the specified ranges.')
    sys.exit(1)


if __name__ == '__main__':
    main()