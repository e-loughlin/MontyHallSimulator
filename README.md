Here’s a `README.md` for your Monty Hall Simulator repository:

---

# Monty Hall Simulator

This Python script simulates the famous Monty Hall problem, allowing you to experience and understand the probability behind this classic puzzle. The Monty Hall problem illustrates why switching doors gives you a better chance of winning the prize in the game show scenario.

## Monty Hall Problem

In the Monty Hall problem, you are a contestant on a game show with three doors. Behind one door is a car (the prize), and behind the other two doors are goats. You choose one door, and the host (who knows what's behind each door) opens another door, revealing a goat. The host then gives you the option to switch your choice to the remaining unopened door or stick with your original choice.

The puzzle: Should you switch or stay to maximize your chances of winning the car?

**Solution:** You should always switch. By switching, your probability of winning the car increases to 2/3, whereas staying with your original choice gives you only a 1/3 chance of winning.

## Features

- Simulates the Monty Hall problem.
- Allows the player to choose a door, watch Monty reveal a goat, and decide whether to switch or stay.
- Keeps track of wins, losses, and win percentage over multiple games.
- Provides a clear and interactive experience of the Monty Hall problem.

## Installation

To get started with the Monty Hall Simulator, clone the repository:

```bash
git clone https://github.com/e-loughlin/MontyHallSimulator.git
cd MontyHallSimulator
```

## Usage

Run the script to start the simulation:

```bash
python monty_hall_simulator.py
```

The game will guide you through the process:

1. Choose a door (1, 2, or 3).
2. The host will open another door, revealing a goat.
3. Decide whether to switch to the remaining unopened door or stick with your original choice.
4. The game will reveal whether you've won or lost.
5. The script will keep track of your wins, losses, and win percentage as you play multiple rounds.

### Example Output

```
Monty Hall Simulator!
Select door 1, 2, or 3!
 1   2   3 
[?] [?] [?] 
2
OK! You've made selection 2. But wait! I'll open a different door...
 1   2   3 
[?] [ ] [?] 
Would you like to switch doors? (y/n)
y
Ok! Open door 3!
 1   2   3 
[ ] [ ] [$] 
You WIN!
=========
Wins: 1
Losses: 0
Games Played: 1
Win Percentage: 1.0
=========
Keep playing? (y/n)
```

## Understanding the Simulation

This script is designed to help you understand the probability behind the Monty Hall problem by simulating it multiple times. By playing several rounds, you can observe how switching doors leads to a win roughly 2/3 of the time, demonstrating the counterintuitive nature of the problem.

## Repository

The full code for the Monty Hall Simulator is available on GitHub: [Monty Hall Simulator](https://github.com/e-loughlin/MontyHallSimulator)

Feel free to explore, modify, and contribute to the project!
