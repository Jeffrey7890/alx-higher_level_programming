#!/bin/bash
# get body of response
curl -s -w '%{http_code}' -f $1 | grep -q '200'&& curl -s $1
