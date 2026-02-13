#!/bin/bash

# 1. Table
declare -A lookup
lookup=(
    ["233168"]="pass"       # 1: Multiples of 3 and 5
    ["4613732"]="pass"      # 2: Even Fibonacci numbers
    ["6857"]="pass"         # 3: Largest prime factor
    ["906609"]="pass"       # 4: Largest palindrome product
    ["232792560"]="pass"    # 5: Smallest multiple
    ["25164150"]="pass"     # 6: Sum square difference
    ["104743"]="pass"       # 7: 10001st prime
    ["23514624000"]="pass"  # 8: Largest product in a series
    ["31875000"]="pass"     # 9: Special Pythagorean triplet
    ["142913828922"]="pass" # 10: Summation of primes
    ["70600674"]="pass"     # 11: Largest product in a grid
    ["76576500"]="pass"     # 12: Highly divisible triangular number
    ["5537376230"]="pass"   # 13: Large sum
    ["837799"]="pass"       # 14: Longest Collatz sequence
    ["137846528820"]="pass" # 15: Lattice paths
    ["136689"]="pass"       # 16: Power digit sum
    ["21124"]="pass"        # 17: Number letter counts
    ["1074"]="pass"         # 18: Maximum path sum I
    ["171"]="pass"          # 19: Counting Sundays
    ["648"]="pass"          # 20: Factorial digit sum
)

tmp_time=$(mktemp)

set -o pipefail
program_output=$( (time python3 "$1") 2> "$tmp_time" | tail -n 1 )
exit_status=$?
real_time=$(grep -E "^real" "$tmp_time" | awk '{print $2}')


echo "$real_time"
rm "$tmp_time"
if [ $exit_status -ne 0 ]; then
	exit $exit_status
fi

if [[ ${lookup["$program_output"]} == "pass" ]]; then
    exit 0
else
    exit 1
fi
