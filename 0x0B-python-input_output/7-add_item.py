#!/usr/bin/python3
"""Add all argument to a list in json file """


import sys
import json

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


item_file = "add_item.json"
argv_cnt = len(sys.argv)

try:
    items = load_from_json_file(item_file)

except Exception:
    items = []

if argv_cnt > 1:
    for i in range(1, argv_cnt):
        items.append(sys.argv[i])

save_to_json_file(items, item_file)
