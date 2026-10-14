#!/usr/bin/env python3
import os, sys

print("Content-Type: text/plain")
print()
print("hello from python cgi")
print("method : " + os.environ.get("REQUEST_METHOD", ""))
print("query  : " + os.environ.get("QUERY_STRING", ""))
length = int(os.environ.get("CONTENT_LENGTH") or 0)
if length:
    print("body   : " + sys.stdin.read(length))
