import torch
import torchaudio
from audiocraft.models import MusicGen

def generate_music(prompt: str, filename: str = "output.wav", duration: int = 15) -> str:
    model = MusicGen.get_pretrained('facebook/musicgen-small')
    model.set_generation_params(duration=duration, temperature=1.0, top_k=250, top_p=0.95)

    wav = model.generate([prompt])
    output_path = f"app/static/outputs/{filename}"
    torchaudio.save(output_path, wav[0].cpu(), sample_rate=32000)
    return output_path
