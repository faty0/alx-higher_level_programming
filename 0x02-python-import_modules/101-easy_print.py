#!/usr/bin/python3
import os
msg = "#pythoniscool\n"
os.write(1, str.encode(msg))
