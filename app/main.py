from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from musicgen_utils import generate_music
import uuid
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "VOCS AI MusicGen API is live 🎶"}

@app.post("/generate")
def generate(prompt: str = Query(..., description="Describe your music")):
    filename = f"{uuid.uuid4().hex[:8]}.wav"
    path = generate_music(prompt, filename)
    return FileResponse(path, media_type="audio/wav", filename=filename)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
