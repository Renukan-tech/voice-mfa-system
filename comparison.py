import librosa
import numpy as np

def compare_audio(file1, file2):
    # Load audio (no resampling issues)
    y1, sr1 = librosa.load(file1, sr=None)
    y2, sr2 = librosa.load(file2, sr=None)

    # Extract MFCC features
    mfcc1 = librosa.feature.mfcc(y=y1, sr=sr1, n_mfcc=20)
    mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2, n_mfcc=20)

    # Take mean for comparison
    mfcc1_mean = np.mean(mfcc1, axis=1)
    mfcc2_mean = np.mean(mfcc2, axis=1)

    # Euclidean distance
    distance = np.linalg.norm(mfcc1_mean - mfcc2_mean)

    return distance