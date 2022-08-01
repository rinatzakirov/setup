#!/bin/bash

while :
do
	python3 $(dirname "$BASH_SOURCE")/mytile.py
	sleep 1
done
