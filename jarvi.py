import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize the speech recognition engine and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to set the voice to a male voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Changing index, changes voices. 0 for male voice.

# Function to speak out the given text
def speak(text):
    print("Jarvis: " + text)  # Print Jarvis' response to the console
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands and perform actions
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for voice commands

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()  # Recognize the voice command
            print("User said:", command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            command = ""
        except sr.RequestError as e:
            print("Could not request results; check your network connection.")
            command = ""
        return command

# Function to get user's name
def get_name():
    speak("May I know your name?")
    name = take_command().capitalize()
    speak("Hello, " + name + "! How can I assist you today?")
    return name

# Main function to execute the voice assistant
def main():
    name = get_name()  # Get user's name
    while True:
        command = take_command().lower()

        # Perform actions based on voice commands
        if "play" in command:
            song = command.replace("play", "")
            speak("Playing " + song)
            pywhatkit.playonyt(song)

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M %p")
            speak("Current time is " + current_time)

        elif "search" in command:
            query = command.replace("search", "")
            speak("Searching for " + query)
            try:
                result = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia, " + result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple search results. Please be more specific.")

        elif "joke" in command or "tell me a joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "google" in command:
            query = command.replace("google", "")
            speak("Searching on Google for " + query)
            pywhatkit.search(query)

        elif "exit" in command or "quit" in command or "bye" in command:
            speak("Goodbye, " + name + "! Have a great day!")
            break

        else:
            speak("I'm sorry, " + name + ". I didn't understand that command.")

if __name__ == "__main__":
    main()
