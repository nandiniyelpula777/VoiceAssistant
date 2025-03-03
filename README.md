# VoiceAssistant

Voice Assistant (Babji)

Overview

Babji is a simple voice assistant built using Python. It listens to voice commands, recognizes speech, and responds with relevant information using text-to-speech synthesis. It can greet users, provide the current date and time, and fetch summaries from Wikipedia.

Features

Recognizes voice commands using speech_recognition.

Converts text to speech using pyttsx3.

Fetches Wikipedia summaries for general queries.

Provides the current date and time.

Responds to greetings.

Requirements

Ensure you have Python installed. It is recommended to use Python 3.10 for better compatibility.

Install Dependencies

Run the following command to install required Python libraries:

pip install speechrecognition wikipedia pyttsx3 pyaudio

If PyAudio fails to install, try:

pip install pipwin
pipwin install pyaudio

Usage

Run the script using:

python voiceassistant.py

When prompted, speak into the microphone. The assistant will process the command and respond accordingly.

Example Commands

"Hello" → Responds with a greeting.

"Current date" → Announces today's date.

"Current time" → Announces the current time.

"Who is Albert Einstein?" → Fetches a summary from Wikipedia.

Troubleshooting

If the assistant doesn't recognize your voice, ensure your microphone is working.

If PyAudio is missing, install it using pipwin.

If speech recognition fails, check your internet connection.

Future Enhancements

Add support for more commands (weather, news, reminders, etc.).

Improve accuracy with NLP techniques.

Integrate with other APIs for extended functionality.

License

This project is open-source and free to use. Contributions are welcome!

