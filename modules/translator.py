# Import necessary libraries

import requests
import whisper
import os
from dotenv import load_dotenv
load_dotenv()


def audio_to_text():
    
    model = whisper.load_model("base")
    result = model.transcribe("D:/Git Hub Repos/AI-Verse/audio/ElevenLabs_2024-05-14T10_14_07_Adam_pre_s50_sb75_se0_b_m2.mp3")
    print(result["text"])
    return result["text"]


def text_to_audio(text:str):
    
    xi_api_key = os.getenv("XI_API_KEY")
    voice_id = "pNInz6obpgDQGcFmaJgB"
    output_path = "output.mp3" 
    chunk_size = 1024
    
    print(xi_api_key) 
    
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice_id
    print(url)
    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": xi_api_key
    }

    data = {
    "text": text,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
    }

    response = requests.post(url, json=data, headers=headers)
    
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
    print("Done")


def translate(source_lang, text):
    
    x_rapid_api_key = os.getenv("X_RAPID_API_KEY")
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": text,
        "target": "en",
        "source": source_lang
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": x_rapid_api_key,
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())