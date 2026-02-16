#!/bin/bash

SOLUTIONS_FILE="solutions.txt"
declare -A lookup

if [[ -f "$SOLUTIONS_FILE" ]]; then
    while read -r line; do
        ans="${line#* }"
        ans="${ans//[[:space:]]/}"
        
        if [[ -n "$ans" ]]; then
            lookup["$ans"]="pass"
        fi
    done < "$SOLUTIONS_FILE"
else
    echo "Error: $SOLUTIONS_FILE not found." >&2
    exit 1
fi

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
