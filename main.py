import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer();
engine = pyttsx3.init()

def sayCommand(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    sayCommand("Initializing Jarvis . . .")
    
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Say something...")
                audio = r.listen(source,timeout=2)
            command = r.recognize_google(audio)
            print(command)
            sayCommand(command)
        except Exception as e:
            print("An error occured; {0}".format(e))
