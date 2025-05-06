import whisper
import tempfile

model = whisper.load_model("small")

def transkrybuj_audio(audio_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name
    result = model.transcribe(tmp_path, language="pl")
    return result["text"]
