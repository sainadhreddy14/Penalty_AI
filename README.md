# Penalty Shootout Game

A fun, interactive web-based penalty shootout game where you play against an AI as both shooter and goalkeeper. Built with Flask (Python) for the backend and vanilla HTML/CSS/JS for the frontend.

---

## Features

- **Turn-based gameplay:** Alternate between shooting and saving against the AI.
- **AI Keeper & Shooter:** The AI adapts its strategy based on your previous choices.
- **Animated graphics:** Visual feedback for shots, saves, and goals.
- **Score tracking:** See live updates for rounds, player score, and AI score.
- **Game summary:** Get a final result and prompt to play again.

---

## Screenshots

### 1. Game Start: Your Turn to Shoot
![Game Start]
<img width="979" height="550" alt="image" src="https://github.com/user-attachments/assets/703b36ef-08e4-46c7-965a-fdaeb9e4e3c7" />

*You begin as the shooter. Choose your direction (Left, Middle, Right) to take your shot against the AI goalkeeper.*

### 2. Your Turn to Save
![Your Turn to Save]
<img width="973" height="548" alt="image" src="https://github.com/user-attachments/assets/b6e67c70-ee65-4565-bce4-d699cda27919" />

*Now, the AI is the shooter and you are the goalkeeper. Pick a direction to dive and try to save the shot!*

### 3. Game Over & Result
![Game Over]
<img width="977" height="549" alt="image" src="https://github.com/user-attachments/assets/c7e3021f-9667-4c2d-bfb5-47fef6975a26" />

*After 5 rounds, the game displays the final score and announces the winner. Refresh to play again!*

> **Note:** Place your screenshots in a folder named `screenshots/` at the project root. Update the image links if you use different filenames or locations.

---

## How to Play

1. **Start the game:** The game opens with you as the shooter.
2. **Take your shot:** Click "Left", "Middle", or "Right" to shoot.
3. **Switch roles:** Next, you become the goalkeeper. Choose a direction to dive and try to save the AI's shot.
4. **Alternate turns:** The game alternates between shooting and saving for 5 rounds.
5. **View results:** After 5 rounds, see who wins and play again by refreshing the page.

---

## Project Structure

```
PenaltyAI/
  app.py                # Flask backend logic
  static/
    ball.png            # Ball image
    goalpost.png        # Goalpost image
    human_keeper.png    # Human goalkeeper image
    robot_keeper.png    # Robot (AI) goalkeeper image
  templates/
    index.html          # Main game UI
```

---

## How it Works

- **Backend (Flask):**
  - Manages game state, scoring, and AI logic.
  - Receives player choices and returns results via JSON.
  - AI adapts its strategy based on your shot/save history.

- **Frontend (HTML/CSS/JS):**
  - Renders the game UI and handles user interactions.
  - Animates the ball and keepers based on game events.
  - Communicates with the backend using AJAX (fetch API).

---

## Running the Game Locally

1. **Install dependencies:**
   ```bash
   pip install flask
   ```

2. **Run the Flask app:**
   ```bash
   python app.py
   ```
   (Run this command inside the `PenaltyAI` directory.)

3. **Open your browser:**
   - Go to `http://127.0.0.1:5000/` to play the game.

---

## Credits

- Developed using [Flask](https://flask.palletsprojects.com/).
- Images: Custom or open-source assets (see `static/` folder).

---

## License

This project is for educational and personal use.

---

**Enjoy the game!** 
