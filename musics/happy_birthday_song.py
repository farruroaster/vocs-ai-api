import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

# Load the model
model = MusicGen.get_pretrained('facebook/musicgen-melody')

# Duration in seconds
model.set_generation_params(duration=10)

# Prompt for happy birthday vibe 🎂🎉🎹
description = ["a cheerful happy birthday melody with acoustic guitar, piano, upbeat drums, and festive party vibe"]

# Generate
wav = model.generate(description)

# Save
audio_write("happy_birthday_song", wav[0].cpu(), model.sample_rate, strategy="loudness")
