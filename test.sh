#!/bin/sh

FLAGS="-lncurses"

FAILURES=0
SUCCESSES=0

for arg in $@; do
    if [ $arg == "-a" ]; then
        ALL=1
    fi
done

echo "C-Obfucscator compiler log" > compiler.log

run_test() {

    local name=$(echo $1 | cut -d'.' -f1)

    echo -n "Running Test $name..."

    local files=$(ls tests/$name)

    cp -r tests/$name/* ./

    python -m cobfuscator $@

    echo -n "Test $name: " >> compiler.log

    local output=$(gcc $FLAGS obfuscated.c 2>&1)

    rm $files

    if [ -z "$output" ]; then
        echo "Passed"

        echo "None" >> compiler.log

        ((SUCCESSES+=1))
    else
        echo "Failed"

        echo -e "\n$output" >> compiler.log

        ((FAILURES+=1))
    fi
}

print_summary() {
    echo -e "\n==== SUMMARY ===="
    echo "Successes: $SUCCESSES"
    echo "Failures: $FAILURES"
}

run_test hello.c
run_test loop.c
run_test tictactoe.c main.c

print_summary