# Video scopes

In October 2021, Discord user `TaranLMG` contributed several Video Scopes of relevant [composites](Composite_visual_overview). Video Scopes are color- or brightness-based waveform analysis of images, which can be generated with editing software such as [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve/) (free and cross-platform), Adobe Premiére and After Effects.

> TaranLMG: a waveform works by mapping out all values from brightest to darkesty, no matter where they lie vertically.
>
> TaranLMG: that's not a very good way to describe it, but video guys know exactly how they work
>
> TaranLMG: but this too can be used to hide an image

For example:

![Example 1](/scopes/example1.png)

![Example 2](/scopes/example2.png)

Video scopes of composites are interesting mostly due to a couple of reasons:

1. While some produce random, garbage data, others produce clear structures which may or not be meaningful in some manner. For the sake of comparison, examples of both are included in this page.
2. Some of these, while not meaningful in themselves, might serve as "hints" that more interesting data could be extracted from said composites. Note, for example, how the [♐BREADTH](BREADTH) scope exhibits signs of the "ring" that is more clearly seen in its 3D composite.

Keep in mind that some of the composites have been rotated 90°, as can be seen in the images below.

## Less interesting scopes

[♐GOLDEN](GOLDEN) (looking at the individual sections produces similar non-noteworthy results):

![GOLDEN](/scopes/golden90.png)

[♐SLIM](SLIM):

![SLIM](/scopes/slim.png)

![SLIM](/scopes/slim90.png)

[♐NEO](NEO):

![NEO](/scopes/neo.png)

[♐CFO](CFO) (RGB):

![CFO](/scopes/cforgb.png)

[♐BREADTH](BREADTH) (YUV vectorscope):

![BREADTH](/scopes/breadthyuv.png)

## More interesting scopes

Note, for example, how some of those are purely RGB whle others feature yellow, pink, etc.

[♐DUAL](DUAL) (LUMA, RGB and YC):

![DUAL](/scopes/dualluma90.png)

![DUAL](/scopes/dualrgb.png)

![DUAL](/scopes/dualyc.png)

[♐DIAGONAL](DIAGONAL) (LUMA, RGB and YC):

![DIAGONAL](/scopes/diagonalluma.png)

![DIAGONAL](/scopes/diagonalrgb.png)

![DIAGONAL](/scopes/diagonalyc.png)

[♐LOCUS](LOCUS) (LUMA and RGB):

![LOCUS](/scopes/locusluma.png)

![LOCUS](/scopes/locusrgb.png)

[♐POINT](POINT) (LUMA, RGB and YC):

![POINT](/scopes/pointluma.png)

![POINT](/scopes/pointrgb.png)

![POINT](/scopes/pointyc.png)

[April 10 Twitter series](April_10_twitter_series) (LUMA and RGB):

![April 10](/scopes/april10luma.png)

![April 10](/scopes/april10rgb.png)

[♐AZO](AZO) (RGB):

![AZO](/scopes/azorgb.png)

# Further discussion

> tukkek: any idea how many discrete values from 0 to 100? more than just 100 right?
>
> TaranLMG: oh, I misunderstood this first time. it's a bit complicated. As i said before, video values actually kinda start at 16, and go up to 235. Then they are (hopefully) automatically stretched so that 16 becomes black (or #00000) and 235 becomes white (or #FFFFFF)
>
> TaranLMG: which means there are 219 total values from black to white
>
> TaranLMG: if this automatic stretching does NOT happen, then you have a full/partial mismatch, and the video will basically have too much or too little contrast
>
> TaranLMG: I only recently discovered that those top 20 values, AND bottom 16 values, are still actually there... just truncated on most screens/video players
>
> TaranLMG: Also, the luma information is encoded with much greater resolution than the chroma information. Basically color is stored in larger blocks of like 2 by 4 pixels, rather than per-pixel as you might expect. But considering the detailed 3D color models you guys have been able to extract, I don't think that this has been much of a problem.  It's called chroma subsampling.

These "top 20 values and bottom 16 values" are also related to another type of steganography `TaranLMG` demonstrated to be possible with `H.264` encoding. This isn't strictly relevant to Video Scopes in themselves necessarily but is nonetheless another yet-untapped method of inquiry into UFSC:

![Darker than black](/scopes/darkerthanblack1.png)

> TaranLMG: this seems to be an ordinary image, yes?
>
> TaranLMG: but if you put a brightness & contrast effect on the footage, and reduce contrast by 20....
>
> TaranLMG: hidden details emerge.

![Darker than black](/scopes/darkerthanblack2.png)

> TaranLMG: we call this "blacker than black."
>
> TaranLMG: and it is retained even when rendering to H.264 /mp4, and uploading to YouTube
>
> TaranLMG: it does not appear on YouTube itself, but the data is still there
>
> TaranLMG: you can even download the file, reduce contrast, and the data is still there
>
> TaranLMG: you CANNOT recover this data by doing a screen recording. you must download the original file... and hope that the video host's additional compression did not strip it out. YouTube, at least for now, does not.
>
> TaranLMG: there are many technical reasons for this. it's called a filter overshoot, if you want to read about it.
>
> TaranLMG: And you can read about "full" versus "partial" video
>
> TaranLMG: And realize that as a result, web video only goes from 16 to 235, meaning that only 219 values are used in a typical video signal instead of 256, and those are streeetched out so that 16 becomes 0, and 235 becomes 255, so ALL web video suffers from posterization as a result
>
> TaranLMG: all in the name of preserving backwards compatibility with some old standard that has long fallen out of use. Kind of like how we're still stuck with 29.97 fps rather than using the far more sensible 30fps, even though the days of NTSC color broadcasting are long behind us.
