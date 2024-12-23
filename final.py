#import statements
#PDF scraping
import PyPDF2
import re
# Pdf to Audio
import pyttsx3

# ---- This section takes the words in the pdf and scrapes it so that it is a string of words ----
# pip install PyPDF2

def extractTextFromPdf(pdfFile: str):
    #extractTexrFromPdf function adapted from https://www.youtube.com/watch?v=RULkvM7AdzY
    # this functions takes in pdf file and returns string with the text from the PDF
    with open(pdfFile, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict = False)
        pdfText = []

        for page in reader.pages:
            content = page.extract_text()
            pdfText.append(content)

        return pdfText


# ---- This section takes the text converted and converts it into an audio ----
# pip3 install pyttsx3
class TextToSpeech:
    # TextToSpeechnclass from https://www.youtube.com/watch?v=XLdL0A_lsgU
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


extractedText = extractTextFromPdf("N21_Networking_v1.pdf")
tts = TextToSpeech('com.apple.voice.compact.en-GB.Daniel', 175, 1.0)
for text in extractedText:
    splitMessage = re.split(r'\s+|[,;?!.-]\s*', text.lower()) # take out punctuation
    print(text)
    tts.textToSpeech(text) 
#tts.listAvailableVoices()
