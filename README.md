# Anthony0.8 Project

**Anthony0.8** is a Python-based English virtual assistant designed for use via the Windows Command Prompt (cmd). It supports both voice and keyboard input, responding in spoken and text forms. Using the OpenAI API, it understands natural language, executes various tasks, and offers customizable responses. Built-in commands and detailed documentation make Anthony0.8 a user-friendly and efficient tool for Windows users. 

After you run the [main.py](main.py) file, the assistant wakes up when you say 'Hello Anthony' and terminates when you say 'Goodbye Anthony'.

**Author**: [Anthony Aoun](https://www.linkedin.com/in/anthony-m-aoun/)

---

## Table of Contents

- [Project Overview](#project-overview)
  - [main.py](#mainpy)
  - [commands.py](#commandspy)
  - [bot/](#bot)
  - [results/](#results)
- [Requirements and Installation](#requirements-and-installation)
  - [Requirements](#requirements)
  - [Installation](#installation)
- [Running Anthony0.8](#running-anthony08)
- [License](#license)
- [Author](#author)

---

## Project Overview

This project consists of the following components:

### [main.py](main.py)
- **`manual_loop`**: Processes manual commands via keyboard input. Users can switch to voice input by typing `"vocal override"`. If `unmute` is `False`, press ENTER after each bot reply to continue.
- **`vocal_loop`**: Processes voice commands via microphone input. Users can switch to manual input by saying `"manual override"`. If `unmute` is `False`, press ENTER after each bot reply. After five failed recognition attempts, the bot automatically grants manual override.

### [commands.py](commands.py)
- **`_listened`**: Checks if specific word combinations exist in the input text and returns `True` or `False`.
- **`echo`**: Repeats the input text.
- **`chat_with_gpt`**: Uses the OpenAI API to respond to user prompts (requires an API key).
- **`respond_to`**: Main function for processing user input and generating bot responses.

### [bot/](bot)
#### [writing.py](bot/writing.py)
- **`clear_cmd`**: Clears the Command Prompt.
- **`type`**: Outputs text with typing effects, including pauses and formatting.
- **`paste`**: Outputs text without typing effects, maintaining formatting.

#### [reading.py](bot/reading.py)
- **`clear_cmd`**: Clears the Command Prompt.
- **`takeInput`**: Captures user input with support for corrections, reprints text when "going back to the previous line" is necessary.

#### [speaking.py](bot/speaking.py)
- **`speak`**: Converts text to speech using the `pyttsx3` library (requires pre-initialized engine).

#### [hearing.py](bot/hearing.py)
- **`clear_cmd`**: Clears the Command Prompt.
- **`wakeup`**: Waits until the wakeup phrase is detected.
- **`takeCommand`**: Captures spoken input using `speech_recognition`. Returns `None` if no input is detected within 10 seconds or if an error occurs.

### [results/](results)
Stores the history of the last conversation.

---

## Requirements and Installation

### Requirements
- Python 3.x
- Pip (Python package manager)
- Git (for cloning the repository)
- [Dependencies listed in `requirements.txt`](requirements.txt)

Ensure Python is installed and your environment meets these requirements before proceeding.

### Installation
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Anthony0.8
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd ANTHONY0.8
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

Anthony 0.8 should be ready to run on your Command Prompt (cmd).

## Running Anthony0.8

Run Anthony0.8 in the Command Prompt using one of the following options:

**Default usage - vocal input | vocal & typing output:**
```bash
python main.py
```

**Manual usage - typing input | vocal & typing output:**
```bash
python main.py -c manual
```

**Muted usage - vocal input | typing output:**
```bash
python main.py -s mute
```

**Manual & Muted usage - typing input | typing output:**
```bash
python main.py -c manual -s mute
```

Anthony0.8 should be running by now. Just say 'Hello Anthony' to wake him up. Enjoy your new companion!


## License
This project is licensed under the MIT License.

## Author
© 2025 [Anthony Aoun](https://github.com/Anthony-Aoun). All rights reserved.

This project is open-source and free to use for educational purpouses only.