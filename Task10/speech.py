
import pyttsx3 as pp

def speak(text):
    speech= pp.init()

    answer=f"The focal length is {text} mm"

    speech.say(answer)
    speech.runAndWait()

if __name__=="__main__":
    def __init__(self,focalpoint):
        speak(focalpoint)