#!/bin/bash

while :
do
	python $(dirname "$BASH_SOURCE")/mytile.py
	sleep 1
done
