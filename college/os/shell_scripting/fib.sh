#!/usr/bin/env bash

echo -n "Enter ending number: "
read a

b=0
c=1

while [ $b -le $a ]; do
  echo $b
  temp=$b
  b=$c
  c=$(($b+$temp))
done
