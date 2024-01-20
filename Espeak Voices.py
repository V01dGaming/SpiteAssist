import pyttsx3

# Initialize pyttsx3 with eSpeak as the TTS engine
engine = pyttsx3.init(driverName='espeak')

# List available eSpeak voices
voices = engine.getProperty('voices')

# Print available voices
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)

# Set a specific eSpeak voice
engine.setProperty('voice', voices[0].id)  # Choose the desired voice
