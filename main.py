from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import uuid
from kokoro.tts_model import TTSModel  # Ensure this import is correct

app = FastAPI()

# Load the TTS model
model = TTSModel.load_pretrained("kokoro-small")  # Adjust as necessary

@app.post("/tts")
async def tts_endpoint(request: Request):
    data = await request.json()
    text = data.get("text", "")
    if not text:
        return {"error": "Text is required"}

    output_file = f"/tmp/{uuid.uuid4()}.wav"
    model.synthesize(text, output_file)
    return FileResponse(output_file, media_type="audio/wav", filename="output.wav")
