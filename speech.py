#speech recognition program in python (version 1)
import speech_recognition as speechr
recog=speechr.Recognizer()
with speechr.Microphone() as source:
    print("Speak Anything :")
    audio=recog.listen(source)
    try:
        text=recog.recognize_google(audio)
        print("Text Form : {}".format(text))
    except:
        print("Sorry unable to recognize your voice")
