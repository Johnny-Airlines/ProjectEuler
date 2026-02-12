#!/usr/bin/env bash

thingy() {
	(time python3 $arg1) 2>&1 | grep real | awk ' {print $2} '
}
export -f thingy
export arg1=$1
timeout 300s bash -c 'thingy'
echo $?


