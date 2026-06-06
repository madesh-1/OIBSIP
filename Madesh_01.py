import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150) 
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"Assistant: {text}")  # Also prints the response
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def respond(command):
    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {date}")

    elif "search" in command:
        speak("What do you want to search for?")
        query = listen()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")
            
    elif "whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp")
    
    elif "bye" in command or "exit" in command:
        speak("Goodbye!")
        return False

    else:
        speak("I'm not sure how to help with that.")

    return True

# Main loop
speak("Voice Assistant ready!")
running = True
while running:
    command = listen()
    if command:
        running = respond(command)
