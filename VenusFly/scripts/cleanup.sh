#!/bin/bash

if [ "$1" == "FILES" ]; then
rm -rf static/vids/* static/pics/*
elif [ "$1" == "LOG"  ]; then
echo "" > flypaper.log
fi

