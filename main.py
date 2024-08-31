import speech_recognition as sr
import pyttsx3
import webbrowser
from musicLibrary import musics
import requests


recognizer = sr.Recognizer();
engine = pyttsx3.init()

def sayCommand(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(command:str):

    if 'open youtube and search' in command.lower():
        search_query = command.split('search')[1].strip()
        print(search_query)
        sayCommand(f"Searching {search_query} on yoututbe")
        webbrowser.open_new(f'https://www.youtube.com/results?search_query={search_query.replace(' ','+')}')
    elif 'open youtube' in command.lower():
        sayCommand("opening youTube")
        webbrowser.open('https://www.youtube.com/')
    elif 'open facebook' in command.lower():
        sayCommand("Opening facebook")
        webbrowser.open('https://www.likdin.com/')
    elif command.lower().startswith('play'):
        song_req = command.split('play')[1].strip();
        serch_song = musics.get(song_req);
        webbrowser.open(serch_song)
        sayCommand(f"Playing {song_req}")
    elif command.lower().startswith('news'):
        news_req = command.split('news')[1].strip();
        news_from_API = 'https://newsapi.org/v2/top-headlines?country={}&apiKey=14dea05a5f53437e8c827a5577223a63';
        if news_req.lower() == 'us':
           news_from_API = news_from_API.format('us')
        else:
            news_from_API = news_from_API.format('in');
        print(news_from_API);
        response = requests.get(news_from_API);
        if response.status_code == 200:
            data = response.json();
            articles = data.get('articles')
            for article in articles:
                print(article.get('title'))
                sayCommand(article.get('title'))
        else:
            print(f"Request failed with status code {response.status_code}")
    else:
        pass

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
                    audio = r.listen(source,timeout=2,phrase_time_limit=3);
                    command = r.recognize_google(audio)
                    processCommand(command)


        except Exception as e:
            print("An error occured; {0}".format(e))


