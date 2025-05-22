import torch
import torchaudio
from audiocraft.models import MusicGen
import threading
import time

# Spinner animation during generation
def show_spinner(done_event):
    spinner = ['|', '/', '-', '\\']
    idx = 0
    while not done_event.is_set():
        print(f"\r{spinner[idx % len(spinner)]} Generating...", end="", flush=True)
        idx += 1
        time.sleep(0.1)

# Load fast model
print("🎧 Loading fast model...")
model = MusicGen.get_pretrained('facebook/musicgen-small')
model.set_generation_params(duration=15, temperature=1.0, top_k=250, top_p=0.95)

# Prompt
descriptions = ["a romantic Indian song featuring soft violin, flute, and gentle percussion"]

# Start spinner thread
spinner_done = threading.Event()
spinner_thread = threading.Thread(target=show_spinner, args=(spinner_done,))
spinner_thread.start()

# Generate audio
print("🎼 Generating... please wait ✨")
wav = model.generate(descriptions)

# Stop spinner
spinner_done.set()
spinner_thread.join()

# Save output
print("\n💾 Saving output...")
torchaudio.save("romantic_violin_indian_song.wav", wav[0].cpu(), sample_rate=32000)
print("✅ Done! Saved as 'romantic_violin_indian_song.wav'")

