# Generated with the help of ChatGPT.
import os
import librosa
import numpy as np
import pyworld as pw
import soundfile as sf

src_folder = "./input"
dst_folder = "./output"

semitone = 1

for file_name in os.listdir(src_folder):
    if file_name.endswith(".wav"):
        # Load the WAV file
        file_path = os.path.join(src_folder, file_name)
        wav, sr = librosa.load(file_path, sr=None, dtype=np.float64)

        # Convert the data type to double
        wav = np.double(wav)

        # Extract the f0, sp, and ap using PyWorld
        f0, sp, ap = pw.wav2world(wav, sr)

        # Shift the f0 by one semitone
        f0_shifted = f0 * 2 ** (semitone / 12)

        # Resynthesize the pitch-shifted signal
        wav_shifted = pw.synthesize(f0_shifted, sp, ap, sr)

        # Save the pitch-shifted WAV file
        dst_file_name = file_name.split(".")[0] + ".wav"
        dst_file_path = os.path.join(dst_folder, dst_file_name)
        sf.write(dst_file_path, wav_shifted, sr)
