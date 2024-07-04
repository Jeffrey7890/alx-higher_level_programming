#!/bin/bash
# get contetn-length
curl -I -s $1 | grep Content-Length | grep -E -o '[[:digit:]]+'
