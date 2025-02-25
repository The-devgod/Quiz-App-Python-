# Python Quiz Application

## Overview
The **Python Quiz Application** is a GUI-based quiz game developed using Tkinter and Matplotlib. The app presents users with multiple-choice questions and tracks their scores. It includes different difficulty levels, a timer, and a pie chart visualization of the final score.

## Features
- **User Interface:** Built using Tkinter with a structured UI layout.
- **Multiple Difficulty Levels:** Questions are categorized into different difficulty levels (Easy, Medium, Hard).
- **Countdown Timer:** Each question has a countdown timer to encourage quick responses.
- **Randomized Questions:** Questions are chosen randomly to ensure variation.
- **Score Tracking:** The app calculates and displays the user’s score at the end of the quiz.
- **Pie Chart Visualization:** Matplotlib is used to display a graphical representation of the user's performance.
- **Retry & Sign Out Options:** Users can re-attempt the quiz or exit the application.

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed on your system. You can download it from [Python’s official website](https://www.python.org/).

### Required Python Libraries
Install the required dependencies using pip:
```sh
pip install matplotlib
```
Tkinter is included by default in Python, so no separate installation is needed.

## How to Run the Application
1. **Clone the Repository (or Save the Script)**
   ```sh
   git clone https://github.com/The-devgod/Quiz-App-Python-.git
   cd Quiz-App-Python
   ```
2. **Run the Main Script**
   ```sh
   python main.py
   ```
3. **Interact with the UI**
   - Click "Start" to begin the quiz.
   - Choose answers within the time limit.
   - View your score and retry if needed.

## File Structure
```
quiz-app/
│── quiz.py               # Entry point of the application
and quiz functionality
│── db.py      # Database query for the application
│── output-onlinepngtools.png  # Logo used in UI
│── README.md             # Documentation
```

## How It Works
1. **Starting the Application:**
   - The user launches the app by running `quiz.py`.
   - A welcome screen is displayed with a "Start" button.

2. **Quiz Mechanics:**
   - A random question is displayed from the selected difficulty level.
   - The user selects an answer within the given time frame.
   - A countdown timer ensures users answer promptly.

3. **Scoring and Visualization:**
   - The score is calculated based on correct answers.
   - A pie chart (using Matplotlib) visually represents the performance.
   - Users can choose to "Re-attempt" the quiz or "Sign Out."

## Future Enhancements
- **Database Integration:** Store user scores for tracking progress.
- **More Question Categories:** Expand the question bank with different topics.
- **Leaderboard System:** Display top scores across multiple attempts.

## Contributors
- **The-devgod** – Developer & UI Designer

## License
This project is open-source and available under the **MIT License**.

pip install matplotlib