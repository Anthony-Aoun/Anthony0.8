import os

from time import sleep


def clear_cmd():
    """
    Description: 
        clears cmd terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def type(speaker_name : str, content : str, line_max_length : int = 50, padding : int = 8) -> None:
    """
    Input: 
        - speaker_name: name of the speaker who said the content
        - content: string to be typed
        - line_max_length: max number of char before a line break
        - padding: space between left border and text block
    Output: 
        - complete_string: all output as a string, with the right format
    Description: 
        prints content of a speaker with the typing effect, taking into account the pauses, the line breaks and the padding
    """ 
    clear_cmd() # clear terminal

    print('\n')
    complete_string = "\n\n"
    name_size = len(speaker_name)+2 # size of name + the semicolumn + space

    # if the name_ is less than padding, start typing from padding distance to the left border
    if name_size < padding:
        print(f"{speaker_name}: "+" "*(padding-name_size), end='')
        complete_string += f"{speaker_name}: "+" "*(padding-name_size)
        line_length = 0
    # if name_size is more than padding, start typing from name_size distance to the left border
    else :
        print(f"{speaker_name}: ", end='')
        complete_string += f"{speaker_name}: "
        line_length = name_size - padding 

    for char in content:
        sleep(0.01) # typing effect
        print(char, end='', flush=True)
        complete_string += char
        line_length += 1

        if char in ['.', '!', '?']:
            sleep(0.05) # longer pause when the sentence ends
        # line break if we reach line_max_length
        elif char == ' ' and line_length >= line_max_length:
            print('\n'+' '*padding, end='')
            complete_string += '\n'+' '*padding
            line_length = 0

    return complete_string


def paste(speaker_name : str, content : str, line_max_length : int = 50, padding : int = 8) -> None:
    """
    Input: 
        - speaker_name: name of the speaker who said the content
        - content: string to be printed
        - line_max_length: max number of char before a line break
        - padding: space between left border and text block
    Output: 
        - complete_string: all output as a string, with the right format
    Description: 
        prints content of a speaker without the typing effect, taking into account the line breaks and the padding
    """ 
    clear_cmd() # clear terminal

    print('\n')
    complete_string = "\n\n"
    name_size = len(speaker_name)+2 # size of name + the semicolumn + space

    # if the name_ is less than padding, start typing from padding distance to the left border
    if name_size < padding:
        print(f"{speaker_name}: "+" "*(padding-name_size), end='')
        complete_string += f"{speaker_name}: "+" "*(padding-name_size)
        line_length = 0
    # if name_size is more than padding, start typing from name_size distance to the left border
    else :
        print(f"{speaker_name}: ", end='')
        complete_string += f"{speaker_name}: "
        line_length = name_size - padding 

    for char in content:
        print(char, end='', flush=True)
        complete_string += char
        line_length += 1

        # line break if we reach line_max_length
        if char == ' ' and line_length >= line_max_length:
            print('\n'+' '*padding, end='')
            complete_string += '\n'+' '*padding
            line_length = 0

    return complete_string

