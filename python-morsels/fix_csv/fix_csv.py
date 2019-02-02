import sys
import csv
import argparse

_, input_file, output_file = sys.argv

#parser = argparse.ArgumentParser()
#parser.add_argument('inputs', nargs=2, help='source and dest')
#parser.add_argument('--in-delimiter', dest='delimiter', default='|')
#parser.add_argument('--in-quote', dest='quote', default='"')
#args = parser.parse_args()
#print(args)

with open(input_file, 'r') as i_fp:
    with open(output_file, 'w+') as o_fp:
        rdr = csv.reader(i_fp, delimiter=delimiter)
        cw = csv.writer(o_fp)
        for row in rdr:
            cw.writerow(row)

