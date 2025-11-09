#!/usr/bin/python3
import PIL.Image,sys

def rename(original):
  parts=original.split('.')
  parts.insert(len(parts)-1,'full')
  return '.'.join(parts)

def resize(image):
  size=image.size
  factor=500/max(size)
  size=list(map(lambda number:int(number*factor),size))
  return image.resize(size)

for path1 in sys.argv[1:]:
  image=PIL.Image.open(path1)
  path2=rename(path1)
  image.save(path2)
  resize(image).save(path1)
  print(f'Resized "{path1}" and saved the original to "{path2}"')
