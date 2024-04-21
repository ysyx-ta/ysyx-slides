#!/usr/bin/python3
import sys

def main():
    for line in sys.stdin:
        sys.stdout.write(line)
        sys.stdout.flush()
        sys.stderr.write(line)

if __name__ == "__main__":
    main()