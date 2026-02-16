#!/bin/bash

# 1. Table
declare -A lookup
lookup=(
    ["233168"]="pass" ["4613732"]="pass" ["6857"]="pass" ["906609"]="pass" ["232792560"]="pass"
    ["25164150"]="pass" ["104743"]="pass" ["23514624000"]="pass" ["31875000"]="pass" ["142913828922"]="pass"
    ["70600674"]="pass" ["76576500"]="pass" ["5537376230"]="pass" ["837799"]="pass" ["137846528820"]="pass"
    ["1366"]="pass" ["21124"]="pass" ["1074"]="pass" ["171"]="pass" ["648"]="pass"
    ["31626"]="pass" ["691020"]="pass" ["4179871"]="pass" ["2783915460"]="pass" ["4782"]="pass"
    ["2496144"]="pass" ["21000"]="pass" ["26115"]="pass" ["27074400"]="pass" ["443839"]="pass"
    ["127520431"]="pass" ["45228"]="pass" ["40730"]="pass" ["1968329"]="pass" ["7129162514264337593543950335"]="pass"
    ["1492155"]="pass" ["748317"]="pass" ["932718654"]="pass" ["1035"]="pass" ["210500"]="pass"
    ["4543901"]="pass" ["1627549360"]="pass" ["16695334890"]="pass" ["547"]="pass" ["153372"]="pass"
    ["1476"]="pass" ["46693"]="pass" ["1000"]="pass" ["2408404"]="pass" ["4065424064"]="pass"
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
