import sys, os

from cobfuscator import process
from .lexer import token_list

def main():
    sys.argv.pop(0)
    src_files = sys.argv
        
    with open('out.c', mode='w', encoding='utf-8') as out:
        process(src_files, out)

    with open('out.c', mode='r', encoding='utf-8') as out:
        _list = token_list(out)
