from pathlib import Path
import os

#pass dictionary entries from gui.py to bills.py
names = []
file_name = None
keynames = ['Name', 'Price', 'Due Date']
p = Path('/home/wiggly/Documents/Finances')
f = None
file_loc = str(f"{p}/{file_name}")
