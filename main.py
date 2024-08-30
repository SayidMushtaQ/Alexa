import speech_recognition as sr
import pyttsx3
import webbrowser
recognizer = sr.Recognizer();
engine = pyttsx3.init()

def sayCommand(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(command:str):
    if 'open youtube and search' in command.lower():
        search_query = command.split('search')[1].strip()
        print(search_query)
        print(command)
        webbrowser.open_new(f'https://www.youtube.com/results?search_query={search_query.replace(' ','+')}')

if __name__ == '__main__':
    sayCommand("Initializing Jarvis")
    
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening . . .")
                audio = r.listen(source,timeout=2,phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == 'jarvis'):
                sayCommand("Yess boss!!")
                with sr.Microphone() as source:
                    print("Jarvis Activated ...")
                    audio = r.listen(source,timeout=2);
                    command = r.recognize_google(audio)
                    processCommand(command)


        except Exception as e:
            print("An error occured; {0}".format(e))
