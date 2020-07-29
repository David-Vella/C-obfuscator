A simple C-obfuscator

# Preprocess
1. create new files without comments *.tmp.c
2. recursive dump to glob.c
3. tokenize glob.c to tokens.c
4. replace all macros
5. write to out.c

# Obfuscate
1. create a list of tokens
2. replace int and char literals with hexadecimal
3. replace string literals with hex escapes
4. replace names with random 4 character string
