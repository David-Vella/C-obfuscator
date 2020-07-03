import sys, os

from cobfuscator import process

def main():
    sys.argv.pop(0)
    src_files = sys.argv
        
    with open('out.c', mode='w', encoding='utf-8') as out:
        process(src_files, out)
