# 🔐 Password Guessing Game

## 📌 About the Project

The Password Guessing Game is an interactive web application developed using Python and Streamlit. Players must guess a randomly selected secret word based on the chosen difficulty level.

The game provides hints after incorrect guesses and allows players a maximum of five attempts to guess the correct word. It also displays the time taken during the game.

This project is useful for beginners who want to practice Python programming and learn how to build interactive web applications using Streamlit.

## ✨ Features

- 🎮 Simple and interactive user interface
- 🎯 Three difficulty levels: Easy, Medium, and Hard
- 🔀 Random secret word selection
- ❤️ Maximum of five guessing attempts
- 💡 Hints showing correctly positioned letters
- ⏱ Game timer to track elapsed time
- 🎉 Celebration animation when the word is guessed correctly
- 🔄 Option to start a new game
- 🎨 Custom styling using CSS

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Streamlit** — Web application framework
- **Random** — Random selection of secret words
- **Time** — Tracking elapsed time
- **CSS** — Customizing the application's appearance

## 📂 Project Structure

```text
Password_Guessing_Game/
│
├── main.py          # Main application code
└── README.md        # Project documentation
```

## ⚙️ Installation and Setup

### Step 1: Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

### Step 2: Download the Project

Clone the repository using Git:

```bash
git clone https://github.com/YOUR-USERNAME/Password-Guessing-Game.git
```

Navigate to the project folder:

```bash
cd Password-Guessing-Game
```

Replace `Shekhda06` with your GitHub username.

Alternatively, download the repository as a ZIP file and extract it.

### Step 3: Install Streamlit

Open a terminal in the project folder and run:

```bash
pip install streamlit
```

### Step 4: Run the Application

Execute the following command:

```bash
streamlit run main.py
```

Streamlit will start the application and provide a local URL, usually:

```text
http://localhost:8501
```

Open this URL in your web browser to play the game.

## 🎮 How to Play

1. Open the application in your browser.
2. Select a difficulty level: Easy, Medium, or Hard.
3. Click **Start Game** to begin.
4. Enter your guessed word in the input field.
5. Click **Submit Guess** to check your answer.
6. If your guess is incorrect, use the hint to identify correctly positioned letters.
7. Try to guess the secret word within five attempts.
8. Click **New Game** to play again.

## 🧠 Difficulty Levels

| Level | Description |
|---|---|
| Easy | Guess a word from the easy word list. |
| Medium | Guess a word from the medium word list. |
| Hard | Guess a word from the hard word list. |

## 📚 Concepts Learned

This project demonstrates several fundamental programming concepts:

- Variables and data types
- Lists and random selection
- Conditional statements (`if`, `elif`, `else`)
- Loops and string manipulation
- User input and button interactions
- Session state management in Streamlit
- Basic CSS styling
- Time tracking using Python
- Building interactive web applications

## 🚀 Future Improvements

Possible improvements include:

- Add a leaderboard and score system.
- Store player scores and game history.
- Add sound effects and animations.
- Improve the hint system.
- Add a restart confirmation and a dedicated exit screen.
- Make the timer update automatically.
- Improve input validation and prevent guesses after the game ends.

## 👨‍💻 Author

**Shekhda Kashyap**

BCA Student | Python Developer | Aspiring AI/ML Developer

## 📄 License

This project is available for learning and educational purposes. You may add an MIT License if you want to permit reuse and modification under its terms.
