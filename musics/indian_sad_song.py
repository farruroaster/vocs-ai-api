import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

model = MusicGen.get_pretrained('facebook/musicgen-melody')
model.set_generation_params(duration=10)  # you can increase to 15 or more

description = ["a slow and emotional Indian song with sitar, tabla, and sad female vocals, cinematic Bollywood vibe"]

wav = model.generate(description)

audio_write("indian_sad_song", wav[0].cpu(), model.sample_rate, strategy="loudness")
