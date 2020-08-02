#!/usr/bin/env python
import argparse
import pandas as pd 
from yahooquery import Ticker
def main():
    args= parse_arguments()
    return args

def parse_arguments():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--quiet","-q",  action="store_true")
    group.add_argument("--verbosity", "-v", type=int, choices=[0, 1, 2],
                        help="increase output verbosity")
    parser.add_argument('--output', "-o", type=str, help="File to unload data.")
    parser.add_argument("--interval", "-i", type=str, help="Interval", choices=['1wk','1mo'])
    parser.add_argument("--ticker"  , "-t", type=str, help="Ticker to fetch")
    parser.set_defaults(interval='1mo',output="out.file.csv",verbosity=0, ticker='googl')
    args=parser.parse_args()
    if args.verbosity >0 : print(vars(args))
    return args

def fetch(args):
    tick = Ticker(args.ticker)
    history = tick.history(interval=args.interval)
    return history

def write(args,history=None):
    df = pd.DataFrame(history,columns=['high','volume'])
    df.to_csv(args.output)

if __name__ == "__main__":
    args= main()
    data=fetch(args)
    write(args,history=data)