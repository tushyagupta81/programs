#!/usr/bin/env bash

echo -n "Enter number 1: "
read a

echo -n "Enter operator: "
read op

if [[ $op != "backspace" ]]; then
  echo -n "Enter number 2: "
  read b
fi

case "$op" in
  "+")
    res=$(($a+$b));
  ;;
  "-")
    res=$(($a-$b));
  ;;
  "/")
    res=$(($a/$b));
  ;;
  "*")
    res=$(($a*$b));
  ;;
  "backspace")
    res=$(($a/10));
  ;;
  *)
    echo "Invalid operator";
    exit 1;
  ;;
esac

echo "result = "$res
