import speech_recognition as sr
import pyttsx3
import webbrowser
from musicLibrary import musics
import requests
from openaiChat import chatWithGPT,generateIMG
from gtts import gTTS
import pygame
import os
pygame.mixer.init()

recognizer = sr.Recognizer();       
engine = pyttsx3.init()

def say_old(text):
    engine.say(text)
    engine.runAndWait()
def say(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove('temp.mp3')
        
def processCommand(command:str):

    if 'open youtube and search' in command.lower():
        search_query = command.split('search')[1].strip()
        print(search_query)
        say(f"Searching {search_query} on yoututbe")
        webbrowser.open_new(f'https://www.youtube.com/results?search_query={search_query.replace(' ','+')}')
    elif 'open youtube' in command.lower():
        say("opening youTube")
        webbrowser.open('https://www.youtube.com')
    elif 'open facebook' in command.lower():
        say("Opening facebook")
        webbrowser.open('https://www.facebook.com')
    elif command.lower().startswith('play'):
        song_req = command.split('play')[1].strip();
        serch_song = musics.get(song_req);
        print(serch_song)
        webbrowser.open(serch_song)
        say(f"Playing")
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
                say(article.get('title'))
        else:
            print(f"Request failed with status code {response.status_code}")
    elif command.lower().startswith('create image'):
        say("creating image ...")
        output = generateIMG(command)
        webbrowser.open(output)
    else:
        output = chatWithGPT(command)
        print(output)
        say(output)

if __name__ == '__main__':
    say("Initializing alexa")
    
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening . . .")
                audio = r.listen(source,timeout=2,phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == 'alexa'):
                say("Yess boss")
                with sr.Microphone() as source:
                    print("Alexa Activated ...")
                    audio = r.listen(source,timeout=2,phrase_time_limit=3);
                    command = r.recognize_google(audio)
                    processCommand(command)


        except Exception as e:
            print("An error occured; {0}".format(e))


