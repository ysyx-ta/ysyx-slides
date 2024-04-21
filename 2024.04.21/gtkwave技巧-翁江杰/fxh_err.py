#!/usr/bin/python3
import sys

def main():
    for line in sys.stdin:
        sys.stdout.write(line)
        sys.stderr.write(line)

if __name__ == "__main__":
    main()