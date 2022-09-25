import os, sys
try:
    __import__("green").Main()
except Exception as e:
    exit(str(e))
