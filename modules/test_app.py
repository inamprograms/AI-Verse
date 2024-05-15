import whisper
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
    
    
test()