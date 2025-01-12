import msvcrt
import os

from .writing import paste


def clear_cmd():
    """
    Description: 
        clears cmd terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def takeInput(speaker_name: str, line_max_length: int = 50, padding: int = 8):
    """
    Input: 
        - speaker_name: name of the speaker who types the input
        - line_max_length: max number of char before a line break
        - padding: space between left border and text block
    Output: 
        - input_text: the str inputed by the user
        - beautiful_input_text: input_text with the format it has on terminal
    Description: 
        returns the input of a certain user taking into account the line breaks and the padding.
        this function gives the user the chance to backspace if they made an error.
        here we are able to go back to the previous line while erasing because the text is
        printed again on cmd when 'going to the previous line' is required 
    """ 
    clear_cmd() # clear terminal

    print('\n')  
    name_size = len(speaker_name) + 2 # size of name + the semicolumn + space

    # if the name_ is less than padding, start typing from padding distance to the left border
    if name_size < padding:
        print(f"{speaker_name}: " + " " * (padding - name_size), end='', flush=True)
        line_length = 0
    # if name_size is more than padding, start typing from name_size distance to the left border
    else:
        print(f"{speaker_name}: ", end='', flush=True)
        line_length = name_size - padding

    line_number = 0 # the index of the line we are currently at (starting from 0)
    input_text = '' # the inputed text to be returned
    all_lines_length = [] # a list of all the lines' lengths

    # keep on taking user input until Enter is pressed
    while True:
        char = msvcrt.getch().decode('utf-8') # read a character

        # if char is backspace and the cursor is near the speaker_name, do nothing (don't shift the cursor to the left)
        if char == '\b' and ( ((name_size > padding) and (line_length == name_size - padding) and line_number == 0) or (line_length == 0 and line_number == 0) ):
            continue

        # if char is Enter stop taking input
        if char == '\r':
            break

        # if char is backspace
        if char == '\b':
            # if we are not on the first line and we are on the left edge of the line
            if line_number > 0 and line_length == 0:
                line_number -=1
                line_length = all_lines_length[-1] - 1 # remove imaginary space in the end of previous line
                all_lines_length = all_lines_length[:-1] # remove previous length of what is now the current line
                input_text = input_text[:-1] # remove imaginary space in the end of previous line

                # rewrite the previous input, gaving deleted the space on the end of the previous line and having the cursor there
                paste(speaker_name, input_text, line_max_length, padding)
            else:
                line_length -= 1
                input_text = input_text[:-1]
                print('\b \b', end='', flush=True) # erase previous char and move back cursor
                   
        else:
            line_length += 1
            input_text += char
            print(char, end='', flush=True) # print the inputed char

        # line break if we reach line_max_length
        if char == ' ' and line_length >= line_max_length:
            print('\n' + ' ' * padding, end='', flush=True)
            line_number += 1
            all_lines_length.append(line_length)
            line_length = 0

    beautiful_input_text = paste(speaker_name, input_text, line_max_length, padding)
    return input_text.lower(), beautiful_input_text