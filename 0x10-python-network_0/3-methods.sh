#!/bin/bash
# get Allowed opttions
curl -s -I $1 | grep Allow | sed 's/Allow: //'
