#!/usr/bin/python3
import glob,re,os.path

def findtitle(page):
  with open(page) as p:
    for line in p:
      if re.match('^# ',line):
        #print(line)
        return True
  return False

def addtitle(page):
  content=False
  with open(page) as p:
    content=p.read()
  name=os.path.basename(page)
  name=name[:name.find('.')]
  while '_' in name:
    name=name.replace('_',' ')
  content=f'# {name}\n\n{content}'
  print(content,file=open(page,'w'))
  
for page in sorted(glob.glob('docs/*.md')):
  if not findtitle(page):
    addtitle(page)
