# Computer-Quiz

# 💻 Computer Quiz Game in Python

A simple, interactive **Computer Quiz Game** built with Python. Test your knowledge by answering questions about Python, India, and computer fundamentals while keeping track of your score.

This beginner-friendly project demonstrates Python's conditional statements, user input, string methods, and score tracking.

## ✨ Features

- 🎮 **Interactive Gameplay** — Choose whether to start the quiz.
- ❓ **Quiz Questions** — Answer four general knowledge and computer-related questions.
- ✅ **Answer Validation** — Checks your answers against the expected answers.
- 📊 **Score Tracking** — Keeps track of the number of correct answers.
- 🏁 **Final Score** — Displays your total correct answers at the end.
- 🔤 **Case-Insensitive Checking** — Accepts answers regardless of capitalization.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Interface:** Command Line / Terminal
- **Concepts:** Variables, `input()`, `if-else`, string methods, and score tracking.

## 📂 Project Structure

```text
Computer-Quiz-Game/
│
├── Computer_Quiz.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/rifazislam1/Computer-Quiz-Game.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Computer-Quiz-Game
   ```

3. Run the program:

   ```bash
   python Computer_Quiz.py
   ```

   If necessary, use `python3` instead of `python`.

## ▶️ How to Play

1. Run the program.
2. Enter `yes` when asked whether you want to play.
3. Answer each question by typing your response.
4. The program tells you whether each answer is correct.
5. At the end, view your total score.

Enter anything other than `yes` at the beginning to exit the game.

## ❓ Quiz Questions

The game currently includes these four questions:

| No. | Question | Expected Answer |
|---|---|---|
| 1 | Who is the inventor of Python? | Guido van Rossum |
| 2 | What is the capital of India? | Delhi |
| 3 | Who is the Prime Minister of India? | Narendra Modi |
| 4 | What is the full form of CPU? | Central Processing Unit |

*Note: The Prime Minister question reflects the answer currently hardcoded in the program and may need updating if the officeholder changes.*

## 💡 Example Output

```text
Can you want to play Computer Quiz Game? yes
Let's Play Computer Quiz Game!
Who is the inventor of python? Guido van Rossum
Correct answer!
What is the capital of India ? Delhi
Correct answer!
Who is the prime minister of India? Narendra Modi
Correct answer!
What is the full form of CPU? Central Processing Unit
Correct answer!
You got 4 answers correct.
```

## 🧠 How It Works

- **`input()`** — Collects the player's decision and answers.
- **`.lower()`** — Converts input to lowercase for case-insensitive comparison.
- **`if-else` statements** — Check whether each answer matches the expected answer.
- **`score` variable** — Increases by one for every correct answer.
- **`quit()`** — Exits the program if the player does not want to play.

## 🎯 Learning Objectives

This project helps beginners learn:

- How to accept user input in Python.
- How to use conditional statements.
- How to compare strings.
- How to use string methods such as `.lower()`.
- How to maintain and update a score.
- How to build a simple interactive command-line application.

## 🔮 Future Improvements

- Add more quiz questions and categories.
- Accept answers with extra spaces by using `.strip()`.
- Display the final score as a percentage.
- Allow users to replay the quiz.
- Randomize the order of questions.
- Add difficulty levels and a leaderboard.

## 🤝 Contributing

Suggestions and contributions are welcome!

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## 📄 License

This project is open-source. You can add an [MIT License](https://opensource.org/license/mit) if you want others to reuse and modify the code under its terms.

---

**If you find this project useful, consider giving the repository a ⭐ on GitHub!**

*Created as a beginner-friendly Python programming project.*
