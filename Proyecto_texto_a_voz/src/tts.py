from gtts import gTTS
import os


def text_to_mp3(text: str, filename: str = "audio.mp3"):
    os.makedirs("output", exist_ok=True)

    tts = gTTS(text=text, lang="es")
    output_path = os.path.join("output", filename)
    tts.save(output_path)
    return output_path