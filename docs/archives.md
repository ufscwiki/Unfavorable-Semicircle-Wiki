
# Archives

## Overview

The original youtube account was shut down for TOS violations, and UFSC's creator(s) deliberately removed the later material.
An important part of the work on this project is ensuring that the
videos will remain available to this community and future researchers.

## Existing Archives

### Archives of videos

*listed from oldest to newest*

* An archive (large, but not complete) of the videos from the original youtube account can be found [here](http://www.mediafire.com/?94a040t5vwsprwx).<br/>(*n.b. The 7zip is 300MB, but what's inside is 7.5GB, 77442 files*)

* An archive of the videos from the second youtube account can be found [here](https://mega.nz/#F!ThAi2TZT!kFlgV0_JDaFeQdVWmJG7bg).

* tomasf has an archive of some videos [here](http://tomasf.se/projects/semi/videos/), including most major videos of the deleted channel as well as the deleted video [SQEN](SQEN "wikilink").

* Discord user Dom has started a new archive [here](https://mega.nz/folder/yQw2RaoR#DP89I-1yRbd_1ABzer1_IA) to consolidate the above, noting that it "contains a handy catalog so you can see what's included and what's missing."
  * The archive key is `DP89I-1yRbd_1ABzer1_IA` (it is included in the URL if you click the top link)

* User *Nostalgic* has created [a mirror of the archives on Internet Archive](https://archive.org/details/unfavorable-semicircle-archive) and on a file server [here](https://f.hitscan.org/ufsc).

### Archives of composites

* a downloadable archive of 2D and 3D composites can be found [here](composites-2021-04-28.zip "wikilink").

## Archiving videos

There are several ways to download the videos that are posted online.

### yt-dlp

[yt-dlp](https://github.com/yt-dlp/yt-dlp) is a command line utility for downloading videos from You-Tube, X and other sites. It can download groups of videos by keyword or channel and control the format of the video and audio it downloads in. It is based on the older `youtube-dl` project, whose last release was in 2021.

Here are some suggested command arguments for optimal use of `yt-dlp` when archiving:

> festercluck: This will get you thumbnails, all video formats without them writing over one another and not changed by any post-processing that youtube-dl might normally do:
> 
> festercluck: `yt-dlp --all-formats --fixup never --write-all-thumbnails -w --autonumber-start 0 -o %(title)s-%(id)s-%(container)s-%(autonumber)s.%(ext)s https://www.youtube.com/watch?v=whatever`

### Other programs

- [JDownloader](http://jdownloader.org/) is a free, open-source download management tool which will download material in the same format it was uploaded.
- Firefox users can use add-ons such as [Download YouTube Videos as MP4](https://github.com/gantt/downloadyoutube), which integrates with the site's interface, adding a button that allows them to download videos.

## Defunct archives 

* A mirror of previous sources above was also available [here](https://ufsc1654.blaucloud.de/index.php/s/ldXZzjZVuLPAXS0) but it appears as of June 2021 to be a dead link.
  * notes for this site read as follows: *(note that the website is very slow but it will eventually open and allow you to download the files at normal speed, just be patient). Total mirror size is just under 2GB.*
