# List of theories: hacking

## Memory manipulation

One idea is that the videos may be carrying [a payload](https://en.wikipedia.org/wiki/Payload_\(computing\)) or affecting
memory elsewhere when played, through memory leaks. This would be a
significant exploit and would be a huge deal. More specifically, `u/FesterCluck` believed the entity behind UFSC is
pen-testing for a GPU RAM exploit via YouTube (or video content in
general).

This is a bit of a controversial theory. Many of us are not sure how
this would work, or if it is even possible, but as of now hasn't
been proven either way.

[Original reddit post](https://www.reddit.com/r/UnfavorableSemicircle/comments/54pxyw/ive_done_it_and_it_is_truly_amazing/).

## Stagefright and Rowhammer

Discord user `festercluck`  has in multiple occasions identified similarities between malformed [MPEG atoms](http://atomicparsley.sourceforge.net/mpeg-4files.html) of UFSC videos and Android's [Stagefright](https://en.wikipedia.org/wiki/Stagefright_\(bug\)) family of media-related exploits - including the timeline and specific vectors of attack such as [CVE-2019-2017](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2017). Whether the use of these exploits is intentional or simply bugs or poor standard compliance from a custom encoder is hard to determine externally. Another criticism of this theory is that there seems to be little to gain from a successful Stagefright exploit on a YouTube viewer's device other than knowing it's possible or not (which could still be very valuable as a [0day](https://en.wikipedia.org/wiki/Zero-day_\(computing\)) or [white-hat](https://en.wikipedia.org/wiki/White_hat_\(computer_security\)) discovery or [grey-hat](https://en.wikipedia.org/wiki/Grey_hat) personal research).

A strong argument in favor of Stagefright in particular (and also Rowhammer, to a lesser extent) was the seeming gravity, exploitabilty and high-profile nature of the bugs (including [major media coverage](https://www.nbcnews.com/tech/security/android-flaw-could-let-hackers-take-over-phone-text-n399016)). This coincides with UFSC's timeline, at a time where the bugs were still very much "out there" and "up for grabs" for anyone who was able to turn the theoretical exploits into actual attacks - while fixes would come very slowly due to the sheer amount of attack vectors (and be impossible without replacing hardware, in the case of Rowhammer).

Ultimately, neither family of exploits were ever weaponized to their full potential, due to the difficulty of leveraging the bugs into practical uses for bad actors. The end of UFSC with [the Strange Reset](RESET_STRANGE_YD) could be seen either as a surrender after the window of opportunity drew to a close - or that a potential, desirable attack was finally found and as such, the author(s) completed the project and attempted to erase any traces left of it.

See also:

* More info on Discord user `festercluck`'s [theories on Stagefright and Rowhammer exploits](UFSC,_Stagefright_and_Rowhammer_exploits).
* "[A log](./videolog.txt) of *[BRILL](BRILL) 49999* triggering the stagefright exploit in VLC", also by `festercluck`, generated on an old Android smartphone.

## Playback glitches

The videos have been shown to cause strange behavior in some cases,
such as playing after the [YouTube](YouTube) duration bar
is over or causing Android phones to shut down their screens.
Whether this is intended or a byproduct of the custom process used
in creating videos is unknown.

While many reports of glitches have been made, few instances have been recorded and even less properly archived for posterity. In fact, it seems natural for reports to become more rare as interest in the old videos wane and video software irons out any glitches, over time. One of the few wiki pages with multiple recordings of such glirches is [♐OR](OR).

## Reverse-engineering

Another possibility is that the author(s) are trying to
[reverse-engineer](https://en.wikipedia.org/wiki/Reverse_engineering) YouTube internals (or Twitter, for that particular
account) by creating scenarios that would target specific systems
such as transcoding, storage or copyright identification.

To this effect, Discord user `festercluck` has pointed out a plethora of publicly-known unitialized-memory bugs within [`ffmpeg`](https://en.wikipedia.org/wiki/FFmpeg) which YouTube (and possibly other platforms, including Twitter and [Twitch](https://www.reddit.com/r/Twitch/comments/q351du/twitchout_of_an_abundance_of_caution_we_have/hfrwu6j/)) use for transcoding videos, some of which lie behind labeled-unsafe performance flags that YouTube seemingly chooses to utilize. Any memory segments exposed in such a way would probably be miniscule and too random to garner meaningful information for any practical purpose (but then again UFSC did upload thousands of videos, many with very long durations, which could have been an attempt at maximizing this attack surface)... Another open question is what sort of useful in-mermoy data could be extracted from a YouTube rendering-farm server, if any.

One user-facing example of such is the "rainbow column" found on older videos' thumbnails (as seen when navigating on the video's timeline), which is the result of a small section of uninitialized memory being used as [RGB image data](https://en.wikipedia.org/wiki/RGB_color_model). This particular bug has been fixed for many years now but can still be found on older videos uploaded while the glitch was still in operation.

The very name "Unfavorable Semicircle" has been suggested to be a play on the famous `©` copyright symbol - with YouTube's [ContentID](https://en.wikipedia.org/wiki/Content_ID_\(system\)) being "unfavorable" for bad actors who'd like to use the platform for piracy and profit. UFSC's strategy for reverse-engineering this system would be for thousands of similar videos of different lengths to be uploaded then claimed as copyright, then monitor whether they found matches between themselves, potentially exposing manners in which content is identified by YouTube or weaknesses to be exploited.

In November 2021, Discord user `electrojustin` reported the
possiblity of UFSC being an attack on YouTube meant to reveal
proprietary video codec- and compression-related information
([link](https://docs.google.com/document/d/1zHYQBtRiLHSkBlstCLgwoTuCX9mvrz27Es5_IiX98IA/edit)).

## ffmpeg vulnerabilities

`ffmpeg` is the ubiquitous transcoder for video platforms, known to be used by YouTube, X, Twitch and others. It is famously prone to attacks, especially if used with default parameters that are not tailored for security or others that favor performance (hence cost reduction on a massive scale).

Due to the fact that `ffmpeg` is a piece of the back-end and not immediately accessible to end-users, video platforms often overlook security considerations that would seem common-sense elsewhere.

Among other exploits, including very many uses of unitialized-memory leakage (like the "colored thumbnail column" that can still be seen in older, very-low-resolution videos), [Attacks on video converters](https://docs.google.com/presentation/d/1yqWy_aE3dQNXAhW8kxMxRqtP7qMHaIfMzUDpEqFneos/mobilepresent#slide=id.p) describes methods (some proven to work on YouTube) to exfiltrate internal file-system data.

As with other hacking theories, the extremely unusual quantity and nature of the videos also in themselves raise suspicion of a potential attack vector being exploited.
