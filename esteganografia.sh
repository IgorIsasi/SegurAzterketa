#!/bin/bash

read -p "Idatzi direktorioaren izena: " dir
read -p "Idatzi irudiaren laburpen kriptografikoa: " lab

for irudi in $(ls $dir)
do
    md5=($(md5sum $dir/$irudi))
    if [ $md5 == $lab ]; then
        break
    fi
done

stegosuite $dir/$irudi