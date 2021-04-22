The [composites](Video_Composites "wikilink") are created with
extracting each frame as a png file. So if a video has 30 frames per
second and the video is 90 seconds long you will have 2700 images. What
/u/tomasfra and /u/piecat have been doing is arranging those images to
create the composite. Some variables are how big is each image (1x1, 5x5
pixels, etc) and what are the dimensions of the grid.

## Composite maker kit

(*created by hellajt*)

Easy to use + with instructions, made for beginners:
~~<https://www.dropbox.com/s/ozn5emlgtaak85r/UFSC.7z?dl=0>~~ (*link inactive!*)

## Step-by-step method (for Mac)

So for example, using a video from the BRINE series...

Each video was 30 FPS and 180.2333 Seconds (30 FPS \* 180.2333 Seconds =
\~5407 Frames Total) Each frame was exported as a 50x50px image (5407
images total - and the 50x50 is the size UFSC uploaded them as) What
seemed to line up was 541 images on the x axis and 10 on the y axis
(although if you do the math it leaves you with a floating number) What
also worked was using 1080x5 which is why we saw some of /u/tomasfra's
"double" image composites. The script that was written by /u/tomasfra
stiches each of those 5407 images (541x10 grid) together into one image.
And so after each BRINE video was released, the new composite fit right
below the previous one. Sidenote: it would seem like 540 on the x-axis
would be a more consistent number (divisible by 1080 -\> a common aspect
ratio), but that resulted in that slanted version we've seen. Unlike the
previous BRILL composites that worked with 540 (IIRC). But changing that
to 541 made it look more correct.

To create your own composite you'll need to install python, the pillow
library, and ffmpeg

(Using BRINE 0 as an example):

#### Install Homebrew

Open Terminal and paste:  
` /usr/bin/ruby -e "$(curl -fsSL
 `<https://raw.githubusercontent.com/Homebrew/install/master/install>`)"`  
Restart Terminal

#### Install FFMPEG

`brew install ffmpeg`  
Restart Terminal

#### Install Python3

(Python 3 is needed for script to run) Video on how to Install Python 3

#### Install PIL

(Python Image Library - The script needs this to run correctly)

Install easy\_install  
` curl  `<https://bootstrap.pypa.io/ez_setup.py>`  -o - | sudo
python `  
  
Install PIP  
`sudo easy_install pip`  
  
Install PIL  
`pip install Pillow`  

### Create Composite

1.  Create a folder called UFSC (create anywhere, take note of the full
    path)
2.  Create 3 folders in UFSC called "videos", "keyframes", and "output"
3.  Download the BRINE0.mp4 file with keepvid.com ( link to BRINE0 is
    <https://www.youtube.com/watch?v=cSHu0M0jJRI> )
4.  Rename that file to BRINE0.mp4 and put in the UFSC/videos/ folder
    (getting rid of the sagittarius symbol makes it easier in terminal)
5.  Open up terminal and run ffmpeg to extract all the frames:
6.  ffmpeg -i /path/to/UFSC/videos/BRINE0.mp4
    /path/to/UFSC/keyframes/output-%000004d.png
7.  Copy /u/piecat's script at <http://pastebin.com/WMkfkcRk> , name it
    composite.py and save to /path/to/UFSC/ folder
8.  Edit with your editor some of the variables:
9.  inputdir = r"/path/to/UFSC/keyframes"
10. outputdir = r"/path/to/UFSC/output"
11. x = 0
12. y = 0
13. width = 541
14. height = int(5407/width)

Save the file and open terminal and run: python3 /path/to/composite.py

Check the /UFSC/output folder and you will see the composite image.

### Notes

You'll have to clear out the keyframes folder if you plan on working
with another file, or create a folder for BRINE0 in keyframes and change
output\_dir = r"path/to/UFSC/keyframes/BRINE0" (and you'll have to
change this for each video you want to extract from).

To output a file with a different name you can change line 46:
`comp.save(output_dir + 'brine0.png')`

You can combine all videos in a series using Qucktime, then create the
composite using that file instead of lining them up individually post
composite creation.

You can change the thumbnail size to whatever you want (default in
script is 1x1), but the script isn't written to automatically update the
height and axis placement, so you'll have to modify it, for example
using 2x2 images would change:

@ line 15: `height = (int(5407/width))*2`

@ line 19: `thumbnail_size = (2, 2)`

starting @ line 38:

`  `  
`x+= 2 `  
`if(x == width): `  
`x = 0 `  
`y+= 2`

## Exclusion composites

(*as suggested by piecat*)

  - downloaded every video in a series
  - imported them into photoshop
  - stacked them on top of each other using "exclusion" mode. (Exclusion
    does XOR between all the pixels)
  - rendered it and export as a video
  - take that video, explode it with ffmpeg, and make a composite in the
    regular way
