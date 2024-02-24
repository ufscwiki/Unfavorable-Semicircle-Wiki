#!/usr/bin/python3

import os
import sys
from PIL import Image
import subprocess
from datetime import date

def navigate_to_docs():
    wiki_dir    = "Unfavorable-Semicircle-Wiki"
    pwd         = os.getcwd()
    if wiki_dir in pwd:
        os.chdir(pwd.split(wiki_dir)[0] + wiki_dir + "/docs")
    else:
        msg = "Directory not found. Please run script inside Unfavorable-Semicircle-Wiki"
        raise RuntimeError(msg)

def check_ignore_date():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--ignore_date":
            return True
        else:
            raise RuntimeError("Unrecognised command line argument")
    else:
        return False

def check_date(fname):
    cmd         = 'git log -1 --pretty="format:%ci"'
    response    = subprocess.run(cmd.split(" ") + [fname], capture_output=True, text=True)
    if response.stderr != '':
        print("Unable to process creation date for " + fname + ". Skipping...")
    date_string = response.stdout.split("format:")[1].split(" ")[0]
    file_date   = date.fromisoformat(date_string)
    return file_date > date(2024, 2, 22)

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
        return "".join(parts[:-1]) + ".full." + parts[-1]

def resize_for_wiki(img, dim):
    factor      = dim / max(img.size)
    new_size    = (int(img.size[0] * factor), int(img.size[1] * factor))
    return img.resize(new_size)

def check_and_resize(img, dim=500):
    fs_fn   = fullsize_filename(img.filename)
    if fs_fn not in os.listdir() and (check_ignore_date() or check_date(img.filename)):
        print("\nResizing " + img.filename)
        resize_for_wiki(img, dim).save(img.filename)
        img.save(fs_fn)
        print("Original saved as " + fs_fn)

if __name__ == "__main__":
    navigate_to_docs()

    # Attempts to open each file as an image and only includes those that are successful
    imgs = filter(lambda x: x != None, [try_open_img(x) for x in os.listdir()])

    for img in imgs:
        # Resizes images created after 22 Feb 2024 so that the largest dimension is 500
        # (or 499 for some due to rounding)
        #
        # To skip the date check run the script with the command line argument --ignore_date
        #
        # To use a different max dimension use the keyword dim. e.g.:
        # check_and_resize(img, dim=1000)
        check_and_resize(img)
