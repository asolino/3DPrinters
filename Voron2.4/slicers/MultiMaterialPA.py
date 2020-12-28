#!/usr/bin/env python
import argparse
import sys

if __name__ == '__main__':
    # Init the example's logger theme

    parser = argparse.ArgumentParser(add_help=True, description="Nose")
    parser.add_argument('-debug', action='store_true', help='Turn DEBUG output ON')
    parser.add_argument('-input', action='store', help='input file name')

    options = parser.parse_args()

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    with open (options.input, 'r') as fp:
        line = fp.readline()
        while line:
            print(line.strip('\n'))
            if line.find('; CP TOOLCHANGE WIPE') >= 0:
                print('SET_PRESSURE_ADVANCE ADVANCE=1.1 SMOOTH_TIME=0.060')
            line = fp.readline()


