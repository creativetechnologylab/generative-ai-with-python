# Whisper

While not generative AI, whisper is a useful library that allows you to process and transcribe speech. Whisper can also be used to detect language from audio.

## Detecting Language

Make sure the `gen-ai` conda environment has been activated. In the code-examples/whisper folder, there will be some audio files containing speech in German, Russian, and Japanese.

To start with, we need to import some libraries and setup whisper.

```python
import whisper
import os
import numpy as np

model = whisper.load_model("turbo")
```

Whisper needs to process the audio files it's given to produce the best results. Because we'll be repeating this process for multiple files, we're better off placing this code in a function.

```python
def prepare_audio_and_detect_language(audio):

    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=128).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    detected_language = max(probs, key=probs.get)
    print(f"Detected language: {detected_language}")
    return detected_language
```

Whisper has a `pad_or_trim` command that can clear any silence that we have in our files. Then, using the model that was chosen earlier, we can ask it to detect language. It will likely give several guesses, which is why we use `max` to see which one was deemed to be the most likely languauge. Whisper assigns a likelihood to each of its guesses, so we're trying to find which one came out on top. Then we simply return the detected language.

Now we can simply write a simple loop to go through our audio files and determine their language.

```python
files = ["japanese", "russian", "german"]

for audio_file in files:

    # load audio and pad/trim it to fit 30 seconds
    file_path = os.path.join(os.getcwd(), audio_file + ".m4a")
    audio = whisper.load_audio(file_path)
    prepare_audio_and_detect_language(audio)
```

Because all the audio files have the same filetype, I can simply look through the words "japanese", "russian" and "german" and then throw ".m4a" on the end to create a string that has the filename. Then I tell whisper to load this audio file, and pass it to the function we just created.

Running this will then show the languages that these audio files have.