import librosa
import numpy as np
import soundfile as sf

def merge_with_librosa(vocal_path, music_path, output_path="output.mp3"):
    # Load audio files
    vocal, sr1 = librosa.load(vocal_path, sr=None)
    music, sr2 = librosa.load(music_path, sr=None)
    
    # Use common sample rate
    target_sr = max(sr1, sr2)
    
    if sr1 != target_sr:
        vocal = librosa.resample(vocal, orig_sr=sr1, target_sr=target_sr)
    if sr2 != target_sr:
        music = librosa.resample(music, orig_sr=sr2, target_sr=target_sr)
    
    # Make same length
    min_len = min(len(vocal), len(music))
    vocal = vocal[:min_len]
    music = music[:min_len]
    
    # Mix
    mixed = vocal + music
    
    # Save
    sf.write(output_path, mixed, target_sr)
    
    return output_path

# Use it
merge_with_librosa("/workspaces/music/transpose-0-model-53556-20260110.mp3", "/workspaces/music/dhurandhar  [music].mp3", "final.mp3")