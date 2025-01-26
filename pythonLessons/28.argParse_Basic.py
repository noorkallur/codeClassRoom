# https://docs.python.org/3/library/argparse.html
import argparse

parser = argparse.ArgumentParser() #instantiate

parser.add_argument(prog = "INT SUMMATION", 
                    description='sums the input integers',
                    epilog='designed by Noor Kallur')

parser.add_argument('inputIntegers',
                    metavar='N',
                    type=int, 
                    nargs='+',
                    help='an integer for the sum opertation')

parser.add_argument('--sum',
                    dest='maxORsum',
                    action='store_const',
                    const=sum, # functions called
                    default=max, # functions called
                    help='sum the integers (default: find the max)')


args = parser.parse_args()
print(args.maxORsum(args.inputIntegers))



