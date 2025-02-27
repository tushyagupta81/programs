#!/usr/bin/env bash

echo -n "Give first number: "
read a

echo -n "Give operator: "
read op

echo -n "Give another number: "
read b

case $op in
  "+")
    echo $(($a+$b));
    ;;

  "-")
    echo $(($a-$b));
    ;;

  "*")
    echo $(($a*$b));
    ;;

  "/")
    echo $(($a/$b));
    ;;

esac
