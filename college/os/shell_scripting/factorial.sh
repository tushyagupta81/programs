#!/usr/bin/env bash

echo -n "Enter a number: "
read a

b=1
for i in $(seq 1 $a); do
  b=$(($b*$i))
done

echo $b
