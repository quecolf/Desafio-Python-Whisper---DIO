from recorder import record_audio
from transcriber import transcribe_audio
from summarizer import summarize_text

audio_file = record_audio()
text = transcribe_audio(audio_file)
summary = summarize_text(text)

print("\nResumo:\n", summary)