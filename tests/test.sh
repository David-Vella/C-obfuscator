#!/bin/bash

# Test hello world
python cobfuscator hello.c
gcc out.c

# Test tic-tac-toe game
python cobfuscator tictactoe.c main.c
gcc out.c -lncurses