#!/usr/bin/env bash

echo -n "Give first number: "
read a

echo -n "Give another number: "
read b

temp=$a
a=$b;
b=$temp;

echo "a = $a";
echo "b = $b";

