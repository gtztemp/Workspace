import pyttsx3
text = input("Enter the text - ")
engine = pyttsx3.init()
engine.setProperty('rate',125)
engine.say (text)
engine.runAndWait()