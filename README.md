# LinkedIn Bot

This LinkedIn automation bot, built with Python, automates tasks such as logging into LinkedIn, searching for specific keywords, and sending connection requests with personalized messages. It features a graphical user interface (GUI) created with **PySimpleGUI** and uses **Selenium** for browser automation.

## Features
- Logs into LinkedIn using user-provided credentials.
- Searches for users based on a given keyword or term.
- Sends customizable connection requests with a message.
- Limits the number of requests to avoid spamming.

## Requirements
1. **Python 3.7+**
2. Libraries:
   - `selenium`
   - `PySimpleGUI`
   - `pyautogui`
3. **Geckodriver**:
   - Download from [Mozilla Geckodriver](https://github.com/mozilla/geckodriver/releases).
   - Update the `executable_path` in the script with the correct path to Geckodriver.

## Installation
1. Clone or download this repository.
2. Install the required dependencies:
   ```bash
   pip install selenium PySimpleGUI pyautogui

3.Download and configure Geckodriver for Selenium.

## Usage Run the script:
```bash
python BotLinkedin.py
```
if you had python 3.0 or above use:
```bash
python3 BotLinkedin.py
```

#### In the GUI, provide the following inputs:
1. Email: Your LinkedIn email.
2. Password: Your LinkedIn password.
3. Search Term: The term to search for "Python Developer".
4. Message: A personalized message to send with connection requests.
5. Number of Connections: Number of requests to send (1–100).
6. Click Enter to start the automation.

### Example
To connect with Python developers:

Enter your LinkedIn credentials in the GUI.
Set the search term to Python Developer.
Provide a message like:
```bash
"Hi, I’m expanding my network of Python professionals and would love to connect!"
```
+ Choose a number from 1-100 for the connection requests.
+ Start the bot. It will log in, search, and send requests automatically.

### Notes
Use responsibly to comply with LinkedIn's Terms of Service.
Avoid sending too many requests in a short time to prevent account restrictions.
Ensure the Geckodriver path is correctly set in the script.
Disclaimer
This project is intended for educational purposes only. Use at your own risk and ensure compliance with LinkedIn policies.
