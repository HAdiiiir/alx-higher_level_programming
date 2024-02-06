#!/usr/bin/python3
"""modules imported"""
import json
import sys


save_file = __import__('5-save_to_json_file.py').save_to_json_file
load_file = __import__('6-load_from_json_file.py').load_from_json_file


file = "add_item.json"
try:
    new = load_file(file)
except (FileNotFoundError, ValueError):
    new = []
for args in sys.argv[1:]:
    new.append(args)
save_file(new, file)
