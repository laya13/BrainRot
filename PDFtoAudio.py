#This section takes the text converted and converts it into an audio
# pip3 install pyttsx3
# code from https://www.youtube.com/watch?v=XLdL0A_lsgU

import pyttsx3

class TextToSpeech:
    engine: pyttsx3.Engine

    def __init__(self,voice,rate:int,volume:float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice',voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume',volume)

    def listAvailableVoices(self):
        voices: list = [self.engine.getProperty('voices')]

        for i, voice in enumerate(voices[0]):
            print(f'{i+1} {voice.name} {voice.age}: {voice.languages[0]} {voice.gender} {voice.id}')

    def textToSpeech(self, text: str, save: bool = False, fileName = 'output.mp3'):
        self.engine.say(text)
        print ('I am speaking...')

        if save:
            self.engine.save_to_file(text, fileName)

        self.engine.runAndWait()



#if __name__ == '__main__':
tts = TextToSpeech('com.apple.voice.compact.en-GB.Daniel', 175, 1.0)
#tts.listAvailableVoices()
tts.textToSpeech("hello there Laya Satish!")
#com.apple.voice.compact.nl-NL.Xander
#com.apple.voice.compact.en-GB.Daniel
#com.apple.voice.compact.ar-001.Maged
#com.apple.voice.compact.fr-FR.Thomas