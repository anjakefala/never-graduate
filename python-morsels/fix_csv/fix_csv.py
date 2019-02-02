import sys
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('inputs', nargs=2, help='source and dest')
parser.add_argument('--in-delimiter', dest='delimiter', default='|')
parser.add_argument('--in-quote', dest='quotechar', default='"')
args = parser.parse_args()

with open(args.inputs[0], 'r') as i_fp:
    with open(args.inputs[1], 'w+') as o_fp:
        rdr = csv.reader(i_fp, delimiter=args.delimiter, quotechar=args.quotechar)
        cw = csv.writer(o_fp)
        for row in rdr:
            cw.writerow(row)

