
# Speech Recognition with Noise Robustness

## Overview

This project is a **Speech Recognition System** that converts speech to text with enhanced **noise robustness**. It reduces background noise and transcribes speech using Google's speech recognition API. The system listens to audio input, processes it to remove noise, and then converts the processed audio into text.

### Key Features:
- **Noise Reduction**: Uses the `noisereduce` library to clean audio before transcription.
- **Speech-to-Text**: Converts processed speech audio into text with the help of Google’s Speech API.
- **Real-Time**: Designed to work with live microphone input, allowing transcription of real-time speech.

## Technologies Used

- **Python 3.x**: The primary programming language for the project.
- **speech_recognition**: Google’s Speech-to-Text API for audio transcription.
- **noisereduce**: Noise reduction for clearer transcription in noisy environments.
- **numpy**: For handling audio data in numerical format.
- **wave**: To handle audio file operations.

## Usage

### Prerequisites

Before running the project, you need to install the necessary Python packages:

```bash
pip install SpeechRecognition noisereduce numpy pydub
```

Additionally, make sure to install `ffmpeg` for audio file conversion (MP3, M4A, etc. to WAV format).

### Running the Project

1. Clone the repository to your local machine or use the provided files.
2. Open your terminal/command prompt.
3. Run the Python script by navigating to the project directory and typing the following:

```bash
python speech_to_text.py
```

4. You will be prompted to enter the following:

    - **Output File Path**: Path where the transcribed text will be saved.
    - **Language Code**: Language code (e.g., `en-US` for English).

5. The program will start listening to your microphone input, process the speech, and provide the transcription output.
