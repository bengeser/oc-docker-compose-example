#!/bin/bash

url=$1
threads=$2

pids=""
start=$(date +%s)
for i in $( seq 1 $threads); do
  wget -O /dev/null -o /dev/null $url &
  pids="$pids $!"
done 

echo "waiting for pids $pids"
for pid in $pids; do
  wait $pid
done
end=$(date +%s)
taken_seconds=$(($end - $start))
echo "took $taken_seconds seconds"