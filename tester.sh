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
	done <"$SOLUTIONS_FILE"
else
	echo "Error: $SOLUTIONS_FILE not found." >&2
	exit 1
fi

tmp_time=$(mktemp)

tmp_bin=$(mktemp)

trap 'rm -f "$tmp_time" "$tmp_bin"' EXIT

ghc -O2 -no-keep-hi-files -no-keep-o-files "$1" -o "$tmp_bin" &>/dev/null
compile_status=$?

if [ $compile_status -ne 0 ]; then
	exit $compile_status
fi

set -o pipefail
program_output=$( (time "$tmp_bin") 2>"$tmp_time" | tail -n 1)
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
