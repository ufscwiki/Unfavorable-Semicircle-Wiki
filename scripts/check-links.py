#!/usr/bin/python3
import glob

for page in sorted(glob.glob('docs/*.md')):
  i=0
  for line in open(page):
    i+=1
    if '\\[' in line:
      continue
    if '[' in line and (not '](' in line or not ')' in line):
      print(f'{page}:{i}')
      print(line)
      input()
