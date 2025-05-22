from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from app.musicgen_utils import generate_music
import uuid

app = FastAPI()

@app.get("/")
def root():
    return {"message": "VOCS AI MusicGen API is live 🎶"}

@app.post("/generate")
def generate(prompt: str = Query(..., description="Describe your music")):
    filename = f"{uuid.uuid4().hex[:8]}.wav"
    path = generate_music(prompt, filename)
    return FileResponse(path, media_type="audio/wav", filename=filename)
