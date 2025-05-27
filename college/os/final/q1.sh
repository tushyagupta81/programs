#!/usr/bin/env bash

echo -n "Enter a: "
read a

echo -n "Enter b: "
read b

a=$(($a+$b))
b=$(($a-$b))
a=$(($a-$b))

echo "a = "$a
echo "b = "$b

