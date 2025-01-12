import pyttsx3 


def speak(engine :pyttsx3.Engine, content : str) -> None:
    """
    Input: 
        - engine: pyttsx3 engine
        - content: string to be spoken
    Output: 
        - None
    Description: 
        speaks the content using the offline library pyttsx3, engine should be created before the call of speak
    """ 
    engine.say(content)
    engine.runAndWait()
  