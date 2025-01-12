import os
import time
import speech_recognition as sr
# also install pyaudio

from .writing import type


def clear_cmd():
    """
    Description: 
        clears cmd terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def wakeup(wakeup_sentence : str) -> None:
    """
    Input: 
        - wakeup_sentence: key sentence to wake the bot up
    Output: 
        - None
    Description: 
        loops till the wakeup_sentence is heard
    """ 
    clear_cmd() # clear terminal

    rec = sr.Recognizer()
    with sr.Microphone() as source:     
        while True:
            try:
                rec.adjust_for_ambient_noise(source, duration=1) # adjust to background noise

                # apply STT
                audio = rec.listen(source, timeout=10)  # set a timeout of 10 seconds if speaker says nothing
                statement = rec.recognize_google(audio, language='en-in').lower()
                
                # if wakeup_sentence is heard, break the loop and exit the function
                if wakeup_sentence.lower() in statement:
                    break

            except Exception as e:
                # print(str(e))
                continue


def takeCommand(speaker_name : str, padding: int = 8) -> str|None:
    """
    Input: 
        - speaker_name: name of the speaker who said the content
        - padding: space between left border and text block
    Output: 
        - statement: the heard statement (str) if a statement has been captured | None if speaker waited too long to speak or a problem occured
        - beautiful_statement: statement with the format it has on terminal
    Description: 
        returns the command heard using the online speech_recognition library, if an Excpetion occurs or speaker says nothing for 10s it returns None
    """ 
    rec = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            clear_cmd() # clear terminal

            rec.adjust_for_ambient_noise(source, duration=1) # adjust to background noise
            
            # once ambient noise is adjusted, print speaker's name
            # speaker can now speak
            print('\n') 
            name_size = len(speaker_name) + 2 # size of name + the semicolumn + space
            # if the name_ is less than padding, start typing from padding distance to the left border
            if name_size < padding:
                print(f"{speaker_name}: " + " " * (padding - name_size), end='', flush=True)
            # if name_size is more than padding, start typing from name_size distance to the left border
            else:
                print(f"{speaker_name}: ", end='', flush=True)

            # apply STT
            audio = rec.listen(source, timeout=10) # set a timeout of 10 seconds if speaker says nothing
            statement = rec.recognize_google(audio, language='en-in').lower()

            beautiful_statement = type(speaker_name, statement) # type what speaker said
            time.sleep(2)

            return statement, beautiful_statement
        
    except Exception as e:
            # print(str(e))
            return None, f"\n\n*{speaker_name}'s voice failed to be recognized*"


  

