# 🪨📄✂️ Rock, Paper, Scissors - Markov Model (1st Order)

This is a Python project that implements a version of the classic **Rock, Paper, Scissors** game, where the computer tries to predict your next move using a **first order Markov model**. The goal is to simulate an opponent that “learns” from the user's move history to improve its performance over time.

## 📌 Features.

- Interactive console mode for playing against the computer.
- Automated test mode to simulate games with random moves.
- Implementation of a **First Order Markov** model to predict the user's next move.
- Recording and analysis of transitions between moves to build a **transition probability matrix**.

## 🧠 How does the Markov model work?

The model analyzes the transitions between the user's moves (`R`, `P`, `S`) and generates a **transition matrix** 3x3 that estimates the probability of the player's next move based on his previous move. Then, the computer uses this information to **anticipate** and launch the **optimal counterattack**.

## 🧪 Program execution.

### 1. Playing interactively or testing with random movements
````bash
python main.py