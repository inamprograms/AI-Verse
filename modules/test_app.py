import whisper
import os
import numpy as np
import torch
# sizeMmodel = whisper.load_model("medium")

# transcriptionIT = sizeMmodel.transcribe("D:/Git Hub Repos/AI-Verse/audio/Recording.m4a")

# print(transcriptionIT['text'])

def test():
    
    # print(torch.cuda.is_available())
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    
    
    model = whisper.load_model("base", device=DEVICE)
    
    print(
    f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
    )
    
    # audio = whisper.load_audio("D:/Git Hub Repos/AI-Verse/audio/ElevenLabs_2024-05-14T10_14_07_Adam_pre_s50_sb75_se0_b_m2.mp3")
    # audio = whisper.pad_or_trim(audio)
    # mel = whisper.log_mel_spectrogram(audio).to(model.device)
    
    # _, probs = model.detect_language(mel)
    # print(f"Detected language: {max(probs, key=probs.get)}")
    
    # result = model.transcribe("D:/Git Hub Repos/AI-Verse/audio/Recording.m4a")
    # print(result)
    # print(result["text"])
    # f = open("text.txt", "a")
    # f.write(result["text"])
    # f.close()
test()