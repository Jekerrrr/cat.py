#-----------------------Author: Jeker---------------------------------------
import argparse

parser = argparse.ArgumentParser(description='a text parser for windows.')

parser.add_argument("file", help="Prints the supplied argument.")

args = parser.parse_args()

f = open(args.file, 'r')
content = f.read()
print(content)
f.close
