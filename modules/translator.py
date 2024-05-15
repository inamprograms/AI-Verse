# Import necessary libraries
import requests  # Used for making HTTP requests
import json  # Used for working with JSON data

def speech_to_speech():

    # Define constants for the script
    CHUNK_SIZE = 1024  # Size of chunks to read/write at a time
    XI_API_KEY = ""  # Your API key for authentication
    VOICE_ID = "pNInz6obpgDQGcFmaJgB"  # ID of the voice model to use
    AUDIO_FILE_PATH = "D:/Git Hub Repos/AI-Verse/audio/ElevenLabs_2024-05-14T10_14_07_Adam_pre_s50_sb75_se0_b_m2.mp3"  # Path to the input audio file
    OUTPUT_PATH = "output.mp3"  # Path to save the output audio file

    # Construct the URL for the Speech-to-Speech API request
    sts_url = f"https://api.elevenlabs.io/v1/speech-to-speech/{VOICE_ID}/stream"

    # Set up headers for the API request, including the API key for authentication
    headers = {
        "Accept": "application/json",
        "xi-api-key": XI_API_KEY
    }

    # Set up the data payload for the API request, including model ID and voice settings
    # Note: voice settings are converted to a JSON string
    data = {
        "model_id": "eleven_english_sts_v2",
        "source_language": "en",
        "target_language": "en",
        "voice_settings": json.dumps({
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        })
    }

    # Set up the files to send with the request, including the input audio file
    files = {
        "audio": open(AUDIO_FILE_PATH, "rb")
    }

    # Make the POST request to the STS API with headers, data, and files, enabling streaming response
    response = requests.post(sts_url, headers=headers, data=data, files=files, stream=True)

    # Check if the request was successful
    if response.ok:
        # Open the output file in write-binary mode
        with open(OUTPUT_PATH, "wb") as f:
            # Read the response in chunks and write to the file
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
        # Inform the user of success
        print("Audio stream saved successfully.")
    else:
        # Print the error message if the request was not successful
        print(response.text)


import requests

def dub_radio_to_english(api_key, radio_file_path, name, source_url, source_lang='auto', num_speakers=0, watermark=False, start_time=None, end_time=None):
    url = "https://api.eleven-labs.com/dubbing"
    headers = {
        "xi-api-key": api_key
    }
    data = {
        "mode": "automatic",
        "file": open(radio_file_path, "rb"),
        "name": name,
        # "source_url": source_url,
        "source_lang": source_lang,
        "target_lang": "en",
        "num_speakers": num_speakers,
        "watermark": watermark
    }
    if start_time is not None:
        data["start_time"] = start_time
    if end_time is not None:
        data["end_time"] = end_time

    response = requests.post(url, headers=headers, files=data)

    if response.status_code == 200:
        dubbing_info = response.json()
        return dubbing_info
    else:
        print("Error:", response.status_code, response.text)
        return None



    