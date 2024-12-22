# VPA-Codeforge
# Virtual Personal Assistant
## Start by running main.py

## Necessary Libraries:
- spacy: 3.7.2
- number-parser: 0.3.2
- dateparser: 1.2.0
- python-date-util: 2.8.2
- SpeechRecognition: 3.10.1

- Python version: 3.9.17
  
## Introduction
Welcome to our Virtual Personal Assistant! This application is designed to assist users in managing their events and reminders seamlessly. It incorporates features such as text recognition, event scheduling, meeting identification, and speech-to-text conversion.

## Features
### 1. Text Recognition and Action Execution
The Virtual Personal Assistant uses text recognition to understand user input. Based on the identified actions in the text, the assistant can add, reschedule, or cancel events at specified times.

#### Example:- User Input: "Schedule a meeting with Sherlock and Watson at 3 PM tomorrow."
- Assistant Action: Adds a meeting event with Sherlock and Watson at 3 PM the next day.

### 2. Meeting Identification and Notification
The system can identify meetings involving registered users and automatically send email notifications to them about the upcoming event. This enhances communication and ensures all participants are well-informed.

#### Example:- Assistant identifies a meeting between Sherlock and Watson.
- Sends email notifications to both Sherlock and Watson about the scheduled event.

### 3. Reminder List with Event History
The assistant maintains a comprehensive list of reminders, including past events. Users can review their history, providing a complete overview of scheduled activities and completed tasks.

#### Example:- User can view a list of reminders, including past events and upcoming tasks.

### 4. Speech-to-Text Conversion
The application supports speech-to-text conversion, allowing users to interact with the assistant verbally. This feature adds convenience and accessibility to the user experience.

### 5. Data Authentication and User Security
To ensure data security, the assistant requires users to log in. Only registered users can access the features and functionalities of the application. This authentication mechanism protects user data and maintains privacy.

#### Example:
- User attempts to access the assistant features.
- If not logged in, the system prompts the user to sign in before proceeding.

## Getting Started
1. Clone the repository to your local machine.
2. Install the required dependencies by running npm install or pip install -r requirements.txt.
3. Set up a database for user authentication and event storage.
4. Configure email settings for notification functionality.
5. Run the application using npm start or python app.py.

