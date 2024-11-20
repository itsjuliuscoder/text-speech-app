# Text-to-Speech App

This is a simple Text-to-Speech (TTS) application built using Python. The app allows users to input text and convert it to speech using the Google Text-to-Speech (gTTS) library. The generated speech is saved as an audio file and played back to the user.

## Features

- Convert text input to speech
- Save the generated speech as an MP3 file
- Play the generated MP3 file

## Requirements

- Python 3.x
- gTTS library
- tkinter library (usually included with Python)
- An audio player (e.g., `afplay` on macOS)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/text-speech-app.git
    cd text-speech-app
    ```

2. Install the required libraries:
    ```sh
    pip install gtts
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. Enter the text you want to convert to speech in the input field.

3. Click the "Start" button to generate and play the speech.

## Code Overview

The main components of the application are:

- `app.py`: The main script that creates the GUI and handles text-to-speech conversion.
- `README.md`: This file, providing an overview and instructions for the app.

## Example

1. Enter text in the input field:
    ```
    Hello, world!
    ```

2. Click "Start".

3. The app will generate an audio file named [`audio.mp3`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fjulius.olajumoke%2FDesktop%2Fcoding%2Fpython-training%2FpythonProject%2Fpython-projects%2Ftext-speech-app%2Faudio.mp3%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/julius.olajumoke/Desktop/coding/python-training/pythonProject/python-projects/text-speech-app/audio.mp3") and play it.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) - Python library and CLI tool to interface with Google Translate's text-to-speech API.
- [tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI package.