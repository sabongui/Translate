"""Transcribe a 16 kHz mono WAV with Whisper large-v3 (sherpa-onnx build).

Usage: python3 transcribe.py speech.wav MODEL_DIR 0,25,46,69.3,86 [ar|en]

Whisper only sees 30 s at a time, so the audio is cut at the given
boundaries (seconds); pick them at pauses found with ffmpeg silencedetect.
"""
import sys

import sherpa_onnx
import soundfile as sf

wav, mdir = sys.argv[1], sys.argv[2]
cuts = [float(x) for x in sys.argv[3].split(',')]
lang = sys.argv[4] if len(sys.argv) > 4 else "ar"

audio, sr = sf.read(wav, dtype='float32')
rec = sherpa_onnx.OfflineRecognizer.from_whisper(
    encoder=f"{mdir}/large-v3-encoder.int8.onnx",
    decoder=f"{mdir}/large-v3-decoder.int8.onnx",
    tokens=f"{mdir}/large-v3-tokens.txt",
    language=lang, task="transcribe", num_threads=4)
for a, b in zip(cuts, cuts[1:]):
    s = rec.create_stream()
    s.accept_waveform(sr, audio[int(a * sr):int(b * sr)])
    rec.decode_stream(s)
    print(f"[{a:5.1f}-{b:5.1f}] {s.result.text.strip()}", flush=True)
