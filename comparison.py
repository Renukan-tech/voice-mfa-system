import librosa
import numpy as np
import os

def compare_voices(file1, file2):
    try:
        file1 = os.path.join("voices", file1)
        file2 = os.path.join("voices", file2)

        audio1, sr1 = librosa.load(file1)
        audio2, sr2 = librosa.load(file2)

        mfcc1 = np.mean(librosa.feature.mfcc(y=audio1, sr=sr1), axis=1)
        mfcc2 = np.mean(librosa.feature.mfcc(y=audio2, sr=sr2), axis=1)

        distance = np.linalg.norm(mfcc1 - mfcc2)

        print("Voice distance:", distance)

        return distance < 50

    except Exception as e:
        print("Error comparing voices:", e)
        return False
    