# main.py
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
import uuid
from kokoro.tts_model import TTSModel  # Assuming you have kokoro installed properly

app = FastAPI()
model = TTSModel.load_pretrained("kokoro-small")  # Customize as needed

@app.post("/tts")
async def synthesize(text: str):
    output_path = f"{uuid.uuid4()}.mp3"
    model.synthesize(text, output_path)
    return FileResponse(output_path, media_type="audio/mp3", filename="output.mp3")
