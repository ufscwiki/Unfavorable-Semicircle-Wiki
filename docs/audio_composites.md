# Audio composites

**Audio-sample compositing** is a technique pioneered by Discord user `N25_CT13` in December, 2023 that involves converting the stereo audio channels of Unfavorable Semicircle's videos into images similar to [visual composites](Video_Composites "wikilink") - the core difference being that they are sourced from audio-samples rather than video-frames.

Some of the iconography unveiled through this process has been entirely novel to UFSC's body-of-work, while others seem more familiar.

The discovery of these composites seems to contradict the [♐️ANSWERS](ANSWERS "wikilink") tweet that claimed no major discoveries were left to be made in the UFSC investigation.


Discord user `noxxy` suggests [♐MOTH](MOTH "wikilink") and [⊕RATE](RATE "wikilink") as potential targets for further investigation.

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

### Python script by Dom

```py
import cv2
import numpy as np
import wave

def main():
    # Open WAV file
    w = wave.open('LOCK.wav', 'rb')
    number_of_channels = w.getnchannels()
    number_of_frames = w.getnframes()
    #print(number_of_channels, number_of_frames)

    # Set desired size of output images (width, height)
    size = (120, 657901)

    # Create arrays to hold left and right samples
    left = np.zeros(dtype=np.uint8, shape=(size[1], size[0], 1))
    right = np.zeros(dtype=np.uint8, shape=(size[1], size[0], 1))

    # Skip frames
    #w.readframes(18480)

    for n in range(size[0]*size[1]):
        # Read left and right audio samples
        frame = w.readframes(1)
        sample1 = int.from_bytes(frame[0:2], byteorder='little', signed=True)
        sample2 = int.from_bytes(frame[2:4], byteorder='little', signed=True)

        # Convert from 16-bit signed (-32,768 to 32,767) to 8-bit unsigned (0 to 255)
        sample1 = int(((sample1/32768) + 1.0)*128)
        sample2 = int(((sample2/32768) + 1.0)*128)

        # Write samples to arrays
        left[n // size[0], n % size[0]] = sample1
        right[n // size[0], n % size[0]] = sample2

    cv2.imwrite("left.png", left)
    cv2.imwrite("right.png", right)

if __name__ == '__main__':
    main()
```

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
