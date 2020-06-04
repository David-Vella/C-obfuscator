import sys

sys.path.insert(0, './')

from cobfuscator import lexer

sys.argv.pop(0)

for srcfile in sys.argv:

    # make sure source file name is in valid format
    if srcfile.count('.') != 1:
        sys.exit('error: failed to parse file name')

    # attempt to open source file
    try:
        src = open(srcfile, mode='r', encoding='utf-8')
    except IOError:
        sys.exit('error: file not found')

    name, extension = srcfile.split('.')
    hashfile = '{}.obf.{}'.format(name, extension)

    dst = open(hashfile, mode='w', encoding='utf-8')

    lexer.tokenize(src, dst)

    dst.close()
    src.close()

    print('created file: {}'.format(hashfile))