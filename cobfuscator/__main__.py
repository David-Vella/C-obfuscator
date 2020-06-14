import sys

sys.path.insert(0, './')

import os

try:
    os.mkdir('./tmp')
except FileExistsError:
    pass

from cobfuscator import lexer
from cobfuscator import preprocessor as pre

sys.argv.pop(0)
src_files = sys.argv
    
with open('out.c', mode='w', encoding='utf-8') as out:
    pre.process(src_files, out)


# with open('glob.c', mode='r', encoding='utf-8') as src:
#     with open('obf.c', mode='w', encoding='utf-8') as dst:
#         lexer.tokenize(src,dst)

# with open('obf.c', mode='r', encoding='utf-8') as src:
#     pre.process(src)


# for srcfile in sys.argv:

#     # make sure source file name is in valid format
#     if srcfile.count('.') != 1:
#         sys.exit('error: failed to parse file name')

#     # attempt to open source file
#     try:
#         src = open(srcfile, mode='r', encoding='utf-8')
#     except IOError:
#         sys.exit('error: file not found')

#     name, extension = srcfile.split('.')
#     hashfile = '{}.obf.{}'.format(name, extension)

#     dst = open(hashfile, mode='w', encoding='utf-8')

#     lexer.tokenize(src, dst)

#     dst.close()
#     src.close()

#     print('created file: {}'.format(hashfile))