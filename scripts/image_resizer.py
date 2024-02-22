#!/usr/bin/python3

import os
from PIL import Image

def navigate_to_docs():
    match os.getcwd().split('/')[-1]:
        case "docs":
            return
        case "Unfavorable-Semicircle-Wiki":
            os.chdir("docs")
        case "scripts":
            os.chdir("../docs")
        case _:
            err_msg = "Directory not found. Please run script inside Unfavorable-Semicircle-Wiki"
            raise RuntimeError(err_msg)

def try_open_img(path):
    try:
        return Image.open(path)
    except:
        return

def fullsize_filename(orig_fname):
    parts   = orig_fname.split(".")
    if "full" in parts:
        return orig_fname
    else:
        return "".join(parts[:-1]) + ".full." + parts[1]

def resize_for_wiki(img, dim):
    factor      = dim / max(img.size)
    new_size    = (int(img.size[0] * factor), int(img.size[1] * factor))
    return img.resize(new_size)

def check_and_resize(img, dim=500):
    fs_fn   = fullsize_filename(img.filename)
    if (img.size[0] > dim or img.size[1] > dim) and fs_fn not in os.listdir():
        print("\nResizing " + img.filename)
        resize_for_wiki(img, dim).save(img.filename)
        img.save(fs_fn)
        print("Original saved as " + fs_fn)

if __name__ == "__main__":
    navigate_to_docs()

    # Attempts to open each file as an image and only includes those that are successful
    imgs = filter(lambda x: x != None, [try_open_img(x) for x in os.listdir()])

    for img in imgs:
        # Resizes any image with either dimension larger than 500 to a maximum of 500
        # To use a different max dimension use the keyword dim. e.g.:
        # check_and_resize(img, dim=1000)
        check_and_resize(img)
