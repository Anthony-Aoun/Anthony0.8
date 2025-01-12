import pyttsx3
import random
import sys
import os
import getopt
import datetime

import commands
from bot import writing, speaking, reading, hearing



# create and initialize TTS engine
engine=pyttsx3.init('sapi5') # for Windows
voices=engine.getProperty('voices') # voices list
engine.setProperty('voice','voices[0].id') # select voice

# what bot says
GREETINGS = ["Hello Sir, how can I help you?", "Good day Sir! How may I be of service to you?", "Greetings Sir! Your commands are my priority. How can I assist you?",\
             "Welcome Sir! I stand ready to assist in any way you require", "Sir, I am at your service. What can I do to assist you?", "Greetings Sir! Your presence graces my virtual realm. How may I serve?",\
             "Good day Sir! Please allow me to assist you in any way possible", "At your service Sir. How may I assist you today?", "Welcome Sir! How can I help you?"]
GOODBYES = ["Have a good day Sir!", "Goodbye Sir, take care!", "See you soon, goodbye!", "It's been a pleasure assisting you Sir, take care!", "I'm here whenever you need assistance. Have a splendid day!"]
EXCUSES = ["I beg your pardon?", "Sorry but I didn't understand...", "Say that again?"]

# what bot should hear to start and shut down
START_COMMAND = "hello anthony"
END_COMMANDS = ["bye anthony", "see you anthony", "see you soon anthony", "see you later anthony", "take care anthony", "ciao anthony"]

# stored history
HISTORY_STRING = ""


def manual_lopp(speaker_name, bot_name, greet_user=True, unmute=True):
    """
    Input: 
        - speaker_name: name of the speaker who types the input
        - bot_name: name of the bot who responds to the speaker
        - greet_user: boolean to precise if bot should greet speaker or not
        - unmute: boolean to precise if bot should speak an type or only type
    Output: 
        - None
    Description: 
        function that takes manual commands from speaker by keyboard input. speaker can switch to vocal command by typing "vocal oerride".
        if unmute is False, the user should hit ENTER after each bot reply to be able to enter their next input.
    """ 
    # if windows change terminal color to yellow
    if os.name == "nt":  
        os.system("color e")

    end_loop = False
    global HISTORY_STRING

    # user greetings
    if greet_user:
        greetings = random.choice(GREETINGS)
        tmp_string = writing.type(bot_name, greetings)
        HISTORY_STRING += tmp_string
        if unmute:
            speaking.speak(engine, greetings)
        else:
            input()

    # main loop
    while True:
        input_text, tmp_string = reading.takeInput(speaker_name) # read user input
        HISTORY_STRING += tmp_string

        # check if the input is an END COMMAND to end the loop
        for end_command in END_COMMANDS:
            if end_command in input_text:
                goodbye = random.choice(GOODBYES)
                tmp_string = writing.type(bot_name, goodbye)
                HISTORY_STRING += tmp_string
                if unmute:
                    speaking.speak(engine, goodbye)
                else:
                    input()
                end_loop = True

        if end_loop:
            break

        # check if user wants to switch to vocal override
        if "vocal override" in input_text:
                tmp_string = writing.type(bot_name, "Vocal override granted")
                HISTORY_STRING += tmp_string
                if unmute:
                    speaking.speak(engine, "Vocal override granted")
                else:
                    input()
                try:
                    vocal_loop(speaker_name, bot_name, greet_user=False, unmute=unmute, wait_wakeup=False)
                    break
                except Exception as e:
                    tmp_string = writing.type(bot_name, "Vocal override failed")
                    HISTORY_STRING += tmp_string
                    if unmute:
                        speaking.speak(engine, "Vocal override failed")
                    else:
                        input()
                    continue
                
        # apply command
        response = commands.respond_to(input_text)
        tmp_string = writing.type(bot_name, response)
        HISTORY_STRING += tmp_string
        if unmute:
            speaking.speak(engine, response)
        else:
            input()


def vocal_loop(speaker_name, bot_name, greet_user=True, unmute=True, wait_wakeup=True):
    """
    Input: 
        - speaker_name: name of the speaker who types the input
        - bot_name: name of the bot who responds to the speaker
        - greet_user: boolean to precise if bot should greet speaker or not
        - unmute: boolean to precise if bot should speak an type or only type
        - wait_wakeup: boolean to precise if bot should wait for START_COMMAND to wakeup or directly wakeup if program is lauched
    Output: 
        - None
    Description: 
        function that takes vocal commands from speaker by microphone input. speaker can switch to manual command by saying "manual oerride".
        if unmute is False, the user should hit ENTER after each bot reply to be able to speak their next input.
        if bot fails to hear user's input for 5 times in a row, bot automatically grants manual override.
    """   
    # if windows change terminal color to blue
    if os.name == "nt":  
        os.system("color b")

    end_loop = False
    global HISTORY_STRING

    # bot waits till START_COMMAND is heard
    if wait_wakeup:
        hearing.wakeup(START_COMMAND)

    # user greetings
    if greet_user:
        greetings = random.choice(GREETINGS)
        tmp_string = writing.type(bot_name, greetings)
        HISTORY_STRING += tmp_string
        if unmute:
            speaking.speak(engine, greetings)
        else:
            input()

    tries_to_hear = 0
    # main loop
    while True:
        input_text, tmp_string = hearing.takeCommand(speaker_name) # hear user input
        HISTORY_STRING += tmp_string

        # if input_text is not None
        if input_text:
            tries_to_hear = 0
            # check if the input is an END COMMAND to end the loop
            for end_command in END_COMMANDS:
                if end_command in input_text:
                    goodbye = random.choice(GOODBYES)
                    tmp_string = writing.type(bot_name, goodbye)
                    HISTORY_STRING += tmp_string
                    if unmute:
                        speaking.speak(engine, goodbye)
                    else:
                        input()
                    end_loop = True

            if end_loop:
                break

            # check if user wants to switch to manual override
            if "manual override" in input_text:
                tmp_string = writing.type(bot_name, "Manual override granted")
                HISTORY_STRING += tmp_string
                if unmute:
                    speaking.speak(engine, "Manual override granted")
                else:
                    input()

                manual_lopp(speaker_name, bot_name, greet_user=False, unmute=unmute)
                break

            # apply command
            response = commands.respond_to(input_text)
            tmp_string = writing.type(bot_name, response)
            HISTORY_STRING += tmp_string
            if unmute:
                speaking.speak(engine, response)
            else:
                input()

        # if input_text is None
        else:
            if tries_to_hear < 3:
                # ask the user to speak again
                excuses = random.choice(EXCUSES)
                tmp_string = writing.type(bot_name, excuses)
                HISTORY_STRING += tmp_string
                if unmute:
                    speaking.speak(engine, excuses)
                else:
                    input()
                tries_to_hear += 1
            else:
                # automatically switch to manual commands
                tmp_string = writing.type(bot_name, "I find it difficult to hear you at the moment. I granted you manual override")
                HISTORY_STRING += tmp_string
                if unmute:
                    speaking.speak(engine, "I find it difficult to hear you at the moment. I granted you manual override")
                else:
                    input()

                manual_lopp(speaker_name, bot_name, greet_user=False, unmute=unmute)
                break





if __name__ == '__main__':
    SPEAKER_NAME = "Anthony"
    BOT_NAME = "Anthony0.8"


    # create or clear history file
    with open("results/last_conversation.txt", "w") as file:
        current_datetime = datetime.datetime.now() # current date and time
        formatted_datetime = current_datetime.strftime("%Y-%m-%d AT %H:%M:%S")
        
        file.write(f"HISTORY OF THE CONVERSATION ON THE {formatted_datetime}\n\n")


    # default values for python file parameters
    option_c = "vocal" # c for command: vocal|manual
    option_s = "unmute" # s for sound: unmute|mute

    # check for parameters existence
    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:s:", ["option_c=", "option_s="])
    except getopt.GetoptError:
        sys.exit(2)

    # check id parameters have the correct values
    for opt, arg in opts:
        if opt in ("-c", "--option_c"):
            if arg == "manual":
                option_c = arg
        elif opt in ("-s", "--option_s"):
            if arg == "mute":
                option_s = arg

    # set sound to mute or unmute
    if option_s == "unmute":
        UNMUTE = True
    else:
        UNMUTE = False

    # set command to manual or vocal
    if option_c == "vocal":
        vocal_loop(SPEAKER_NAME, BOT_NAME, unmute=UNMUTE)
        os.system("taskkill /F /IM cmd.exe")
    else:
        manual_lopp(SPEAKER_NAME, BOT_NAME, unmute=UNMUTE)
        os.system("taskkill /F /IM cmd.exe")

    with open("results/last_conversation.txt", "a") as file:
        file.write(HISTORY_STRING)