import os
import speech_recognition as sr
import noisereduce as nr
import numpy as np
import time

def reduce_noise_from_audio(audio_data, sample_rate):
    """
    Reduces noise from the given audio data.
    """
    audio_array = np.frombuffer(audio_data, dtype=np.int16)
    reduced_audio = nr.reduce_noise(y=audio_array, sr=sample_rate)
    return reduced_audio.astype(np.int16).tobytes()

def transcribe_audio(audio_data, sample_rate, language):
    """
    Transcribes audio data to text using Google's speech recognition API.
    """
    recognizer = sr.Recognizer()
    audio = sr.AudioData(audio_data, sample_rate, 2)  # 2 bytes per sample (16-bit)
    return recognizer.recognize_google(audio, language=language)

def real_time_transcription(language: str, output_path: str):
    """
    Captures speech from the microphone, applies noise reduction, and transcribes it.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone(sample_rate=16000) as source:
        print("Listening... Please speak clearly into the microphone.")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            start_time = time.time()
            audio_data = recognizer.listen(source, timeout=10)
            end_time = time.time()
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            return
        except KeyboardInterrupt:
            print("\nStopped by user.")
            return

    duration = round(end_time - start_time, 2)
    print(f"Captured speech duration: {duration} seconds")
    print("Processing audio...")

    try:
        raw_audio = audio_data.get_wav_data()
        reduced_audio = reduce_noise_from_audio(raw_audio, 16000)
    except Exception as e:
        print("Noise reduction failed. Using raw audio.")
        reduced_audio = audio_data.get_wav_data()

    try:
        text = transcribe_audio(reduced_audio, 16000, language)
    except sr.UnknownValueError:
        print("Could not understand the audio. Please try again.")
        return
    except sr.RequestError as e:
        print(f"API request failed: {e}")
        return

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Transcription saved to: {output_path}")
    print("Transcription: ", text)

if __name__ == "__main__":
    output_path = input("Enter the output file path (e.g., result.txt): ").strip()
    language = input("Enter the language code (e.g., en-US): ").strip()

    try:
        real_time_transcription(language, output_path)
    except Exception as e:
        print("An error occurred:", e)
