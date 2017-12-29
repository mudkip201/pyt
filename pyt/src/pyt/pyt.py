# -*- coding: utf-8 -*-

import interpreter2 as interp
import argparse
import io


def parse(line):
    return interp.parse(line,[])


def main():
    parser=argparse.ArgumentParser(description="Executes a pyt file")
    parser.add_argument("--file","-f",type=str,required=True)
    args=parser.parse_args()

    f=io.open(args.file,mode="r",encoding="utf-8")
    parse(f.read())
    f.close()



if __name__ == "__main__":
    main()