import speech_recognition as sr
from transformers import pipeline
import pyttsx3

# Initialize the SpeechRecognizer
recognizer = sr.Recognizer()

# Initialize the translation pipeline
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")
def translate_text(text):
    """
    Translate the given text from English to Hindi.
    """
    try:
        translation = translator(text)
        return translation[0]['translation_text']
    except Exception as e:
        print("Translation failed:", e)
        return None
def text_to_speech(text):
    """
    Convert the given text to speech.
    """
    try:
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech

        # Convert text to speech
        engine.say(text)

        # Wait for the speech to finish
        engine.runAndWait()
    except Exception as e:
        print("Text-to-speech conversion failed:", e)

# Replace "text-to-speech-command" with the function call


# Main loop for real-time speech recognition and translation
while True:
    try:
        # Listen for the user's speech in real-time
        with sr.Microphone() as source:
            print("Please speak...")
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source)

        # Recognize speech from the recorded audio
        text = recognizer.recognize_google(audio_data)
        print("Recognized speech:", text)

        # Translate recognized speech
        translated_text = translate_text(text)
        if translated_text is None:
            print("Translation failed.")
            continue

        print("Translated text:", translated_text)

    
        text_to_speech(translated_text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print("Error:", e)

