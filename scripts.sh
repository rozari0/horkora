#!/bin/bash

if [[ "$@" == *export* ]]; then
  poetry export --without-hashes --format=requirements.txt | cut -d ';' -f 1 > requirements.txt
fi

