import sounddevice as sd


def callback(indata, frames, time, status):
    print(frames)

stream = sd.RawInputStream(channels=2, samplerate=48000, callback=callback)
with stream:
    sd.sleep(5 * 1000)
