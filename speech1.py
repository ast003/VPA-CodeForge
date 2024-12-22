import speech_recognition as sr

def speech_to_text():
    
    recognizer = sr.Recognizer()

   
    with sr.Microphone() as source:
        print("Speak something...")

        try:
            recognizer.adjust_for_ambient_noise(source)  
            audio = recognizer.listen(source, timeout=5)  

            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text

        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")
            return None

if __name__ == "__main__":
    recognized_text = speech_to_text()

    if recognized_text:
        print("Stored text:", recognized_text)
  
