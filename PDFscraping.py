#This section takes the words in the pdf and scrapes it so that it is a string of words
# pip install PyPDF2
#code from https://www.youtube.com/watch?v=RULkvM7AdzY

import PyPDF2
import re

def extractTextFromPdf(pdfFile: str):
    with open(pdfFile, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict = False)
        pdfText = []

        for page in reader.pages:
            content = page.extract_text()
            pdfText.append(content)

        return pdfText
    

if __name__ == '__main__':
    extractedText = extractTextFromPdf("N21_Networking_v1.pdf")
    for text in extractedText:
        splitMessage = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        print(text) 