from pypdf import PdfReader
import pyttsx3
import sys

#stores the name of pdf file to be read from command line
filename = sys.argv[1]

#create PdfReader object
reader = PdfReader(filename)

#create a pyttsx3 object
engine = pyttsx3.init()

#obtain the speech rate value and set a new rate
rate = engine.getProperty("rate")
engine.setProperty("rate", rate + 50)

#iterate thru the pages of pdf and append the text from e/ page to a string
pdf_text = ""
for page in reader.pages:
    pdf_text += page.extract_text()
    
#save text to mp3 file 
engine.save_to_file(pdf_text, "tts_pdf.mp3")
engine.runAndWait() #execute all queued engine commands
