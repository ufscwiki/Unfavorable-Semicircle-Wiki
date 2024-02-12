# Audio composites

**Audio-sample compositing** is a technique pioneered by Discord user `N25_CT13` in December, 2023 that involves converting the stereo audio channels of Unfavorable Semicircle's videos into images similar to [visual composites](Video_Composites "wikilink") - the core difference being that they are sourced from audio-samples rather than video-frames.

Some of the iconography unveiled through this process has been entirely novel to UFSC's body-of-work, while others seem more familiar.

The discovery of these composites seems to contradict the [♐️ANSWERS](ANSWERS "wikilink") tweet that claimed no major discoveries were left to be made in the UFSC investigation.

## First composite

> N25_CT13: i dont know if this is useful or not but ive turned the [lock](LOCK "wikilink")'s right audio channel into an image
>
> N25_CT13: i put every sample's value as a pixel color and have set the image width to the amount of samples between repeating noises

![audio_composites_wave.png](audio_composites_wave.png "audio_composites_wave.png")

## Compositing method

Discord user `Dom` explains the process:

> 1. Convert the audio samples to a black and white image, where sample height corresponds to pixel brightness
>
> 2. Shrink the image horizontally to about 1% of it's original size (we went from 19880 pixels to 200)
>
> 3. Use standard compositing tools to find the correct width
>
> Step #2 is also equivalent to speeding up the video 100x, we think. This is where resampling and interpolation come in.

It has been postulated that since YouTube's encoding would not preserve the exact fidelity of any data encoded in audio samples, it was necessary for UFSC to first slow down the audio before uploading the videos. As such, the audios have to be sped up again to return to their intended form. The exact factor by which the samples have been altered is unknown and different approaches to this step will produce varied qualities in the final result.

## Other composites

Unless stated otherwise, these are from ♐LOCK.

### By N25_CT13

![audio_composites_ball.png](audio_composites_ball.png "audio_composites_ball.png")
![audio_composites_stel.png](audio_composites_stel.png "audio_composites_stel.png")
![audio_composites_stel_long.png](audio_composites_stel_long.png "audio_composites_stel_long.png")
![audio_composites_flipped.png](audio_composites_flipped.png "audio_composites_flipped.png")
![audio_composites_cube.png](audio_composites_cube.png "audio_composites_cube.png")

> tukkek: these look nearly identical to some visual composites such as [♐FOND](FOND "wikilink") and [♐GOLDEN](GOLDEN "wikilink")

![audio_composites_poles.png](audio_composites_poles.png "audio_composites_poles.png")

> N25_CT13: also tried converting [the handshake](Handshake "wikilink")

![audio_composites_hsh1.png](audio_composites_hsh1.png "audio_composites_hsh1.png")

### By Dom

> Dom: Here are the first million samples (20.83 seconds) of LOCK's left channel, generated using the script I linked above. I used the composite tool to reshape it to a width of 1024 pixels. It's interesting to see so much periodicity at this width, since 1024 is a power of two
>
> Dom: There are exactly 1024 (2^10) samples between the peaks in the first section. Then, after about a second of noise in the middle, there are exactly 128 (2^7) samples between peaks. I believe there are 65536 (2^16) samples in each of the repeating clips at the end

![audio_composites_out3.png](audio_composites_out3.png "audio_composites_out3.png")

> Dom: No wonder so many people said LOCK sounds like a printer. The waveform is literally forming this image line by line

![audio_composites_LOCK_ball.png](audio_composites_LOCK_ball.png "audio_composites_LOCK_ball.png")

![audio_composites_out7.png](audio_composites_out7.png "audio_composites_out7.png")
![audio_composites_out9.png](audio_composites_out9.png "audio_composites_out9.png")

## See also

- [Composite visual overview](Composite_visual_overview "wikilink")
- [♐MOTH](MOTH "wikilink") and [⊕RATE](RATE "wikilink"), which Discord user `noxxy` suggests as potential targets for further investigation

## Python script by Dom

> It only works with WAV files and it only does audio->image conversion, not resampling or "squishing". If you use another program to speed up and convert the audio, and then put the output from this script into a composite tool, you may get some results.

```py
#!/usr/bin/env python3

import cv2
import numpy as np
import math
import sys
import wave

# audio_2_image.py
#
# Input file must be in WAV format!
#
# Usage: python3 audio_2_image.py [options] <input_file>
# Options:
#     -l          Select left channel
#     -r          Select right channel
#     -w <width>  Specify width

def main():
    input_file = None
    select_left = True
    select_right = True
    width = -1

    # Parse command line arguments
    if len(sys.argv) <= 1 or sys.argv[1] == '-h':
        print('Usage: python3 audio_2_image.py [options] <input_file>\n' + 
              'Options:\n' +
              '    -l          Select left channel\n' +
              '    -r          Select right channel\n' +
              '    -w <width>  Specify width')
        return
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '-l':
            select_right = False
            if select_left == False:
                print('ERROR: Cannot use both -l and -r at once')
                return
        elif arg == '-r':
            select_left = False
            if select_right == False:
                print('ERROR: Cannot use both -l and -r at once')
                return
        elif arg == '-w':
            i += 1
            if i == len(sys.argv):
                print('ERROR: Must specify a number after -w')
                return
            else:
                try:
                    width = int(sys.argv[i])
                except ValueError:
                    print('ERROR: Must specify a number after -w')
                    return
                if width <= 0:
                    print('ERROR: Width must be greater than 0')
                    return
        else:
            if input_file == None:
                input_file = arg
            else:
                print('ERROR: Unknown token or duplicate file name:', arg)
                return
        i += 1
    if input_file == None:
        print('ERROR: No input file given')
        return

    # Open input WAV file
    try:
        w = wave.open(input_file, 'rb')
    except wave.Error:
        print('ERROR: Input file must be in WAV format')
        return
    except FileNotFoundError:
        print('ERROR: File not found: ' + input_file)
        return
    number_of_channels = w.getnchannels()
    number_of_frames = w.getnframes()
    sample_width = w.getsampwidth()
    if number_of_channels > 1:
        print('%s: %d frames, %d channels' % (input_file.split('/')[-1], number_of_frames, number_of_channels))
    else:
        print('%s: %d frames' % (input_file.split('/')[-1], number_of_frames))

    # Calculate output array size
    if width == -1:
        width = math.ceil(math.sqrt(number_of_frames))
    height = math.ceil(number_of_frames / width)
    if width >= 32767 or height >= 32767:
        print('WARNING: Output dimension greater than 32,767. File might not save properly.')

    # Create output arrays
    left = None
    right = None
    if number_of_channels == 1:
        if select_left == False or select_right == False:
            print('Audio is mono, ignoring channel selection')
        select_left = True
        select_right = False
    if select_left:
        left = np.zeros(dtype=np.uint8, shape=(height, width, 1))
    if select_right:
        right = np.zeros(dtype=np.uint8, shape=(height, width, 1))

    # Print starting text
    if select_left and select_right:
        print('Writing to left.png AND right.png at %dx%d' % (width, height), end='', flush=True)
    elif select_left:
        print('Writing to left.png at %dx%d' % (width, height), end='', flush=True)
    else:
        print('Writing to right.png at %dx%d' % (width, height), end='', flush=True)
    tenth_interval = number_of_frames // 10

    # Read all audio samples to image array(s)
    for n in range(number_of_frames):
        frame = w.readframes(1)
        if select_left:
            left_sample = int.from_bytes(frame[0:2], byteorder='little', signed=True)
        if select_right:
            right_sample = int.from_bytes(frame[2:4], byteorder='little', signed=True)

        # Convert from 16-bit signed (-32,768 to 32,767) to 8-bit unsigned (0 to 255)
        if select_left:
            left_sample = int(((left_sample/32768) + 1.0)*128)
        if select_right:
            right_sample = int(((right_sample/32768) + 1.0)*128)

        x = n % width
        y = n // width
        if select_left:
            left[y, x] = left_sample
        if select_right:
            right[y, x] = right_sample

        if n % tenth_interval == 0:
            print('.', end='', flush=True)

    print('DONE')

    # Write image(s)
    if select_left:
        cv2.imwrite("left.png", left)
    if select_right:
        cv2.imwrite("right.png", right)

if __name__ == '__main__':
    main()
```
