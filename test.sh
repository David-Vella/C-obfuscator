#!/bin/sh

FLAGS="-lncurses"

FAILURES=0
SUCCESSES=0

function get_time {
    echo $(($(date +%s%N)/1000000))
}

function run_test {
    local name=$(echo $1 | cut -d'.' -f1)

    echo -n "Running Test $name..."

    local files=$(ls tests/$name)

    cp -r tests/$name/* ./

    python -m cobfuscator $@
    local obfuscate=$?

    echo -n "Test $name: " >> compiler.log

    local output=$(gcc $FLAGS obfuscated.c 2>&1)
    local compile=$?

    rm $files

    if [[ $compile -eq 0 && $obfuscate -eq 0 ]]; then
        echo "Passed"
        ((SUCCESSES+=1))
    else
        echo "Failed"
        ((FAILURES+=1))
    fi

    if [ -z "$output" ]; then
        echo "None" >> compiler.log
    else
        echo -e "\n$output" >> compiler.log
    fi
}

function print_summary {
    echo -e "\n==== SUMMARY ===="
    echo "Successes: $SUCCESSES"
    echo "Failures: $FAILURES"
    echo -e "\nFinished in $(($(get_time)-START))ms"
}

for arg in $@; do
    if [ $arg == "-a" ]; then
        ALL=1
    fi
done

echo "C-Obfucscator compiler log" > compiler.log

START=$(get_time)

run_test hello.c
run_test loop.c
run_test tictactoe.c main.c

print_summary
