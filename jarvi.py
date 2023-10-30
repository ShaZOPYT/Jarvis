import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

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
speak("hi i am voice assistant i was developed by Shakthi and Jayanth")
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
            # Add code to play the song using your preferred music player

        elif "what is the date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak("Today's date is " + current_date)

        elif command.startswith("who is"):
            topic = command.replace("who is", "").strip()
            try:
                explanation = wikipedia.summary(topic, sentences=2)  # Limit the summary to 2 sentences
                speak("Here is information about " + topic + ": " + explanation)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple search results. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak("I'm sorry, I couldn't find information about " + topic)

        elif "exit" in command or "quit" in command or "bye" in command:
            speak("Goodbye, " + name + "! Have a great day!")
            break

        else:
            speak("I'm sorry, " + name + ". I didn't understand that command.")

if __name__ == "__main__":
    main()
