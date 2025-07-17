from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

DIRECTIONS = ['left', 'middle', 'right']
MAX_ROUNDS = 5

class PenaltyShootoutGame:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.round = 1
        self.player_score = 0
        self.ai_score = 0
        self.player_turn = True
        self.game_over = False
        self.player_history = []          # Track player's shot directions
        self.human_keeper_history = []    # Track player's save directions

    def play_round(self, player_choice):
        if self.game_over:
            return {'error': 'Game is over. Please refresh to play again.'}

        if player_choice not in DIRECTIONS:
            return {'error': f'Invalid choice: {player_choice}'}

        if self.player_turn:
            # Player shoots
            shooter_choice = player_choice

            # AI Keeper Prediction
            if len(self.player_history) >= 3:
                ai_save = max(set(self.player_history), key=self.player_history.count)
            else:
                ai_save = random.choice(DIRECTIONS)

            self.player_history.append(shooter_choice)
            goal = shooter_choice != ai_save

            if goal:
                self.player_score += 1
                message = f"You shot {shooter_choice}! Goal!"
            else:
                message = f"You shot {shooter_choice}! Saved by AI!"

            self.player_turn = False

            return {
                'message': message,
                'player_turn': self.player_turn,
                'round': self.round,
                'player_score': self.player_score,
                'ai_score': self.ai_score,
                'ai_choice': ai_save,
                'last_shot': shooter_choice,
                'game_over': self.game_over
            }

        else:
            # AI shoots

            # AI strategy: avoid player's most common save direction
            if len(self.human_keeper_history) >= 3:
                most_saved = max(set(self.human_keeper_history), key=self.human_keeper_history.count)
                choices = [d for d in DIRECTIONS if d != most_saved]
                ai_shot = random.choice(choices) if choices else random.choice(DIRECTIONS)
            else:
                ai_shot = random.choice(DIRECTIONS)

            player_save = player_choice
            self.human_keeper_history.append(player_save)

            goal = ai_shot != player_save

            if goal:
                self.ai_score += 1
                message = f"AI shot {ai_shot}! Goal!"
            else:
                message = f"AI shot {ai_shot}! You saved it!"

            self.player_turn = True
            self.round += 1

            if self.round > MAX_ROUNDS:
                self.game_over = True
                message += f" Final Score — You: {self.player_score} | AI: {self.ai_score}."
                if self.player_score > self.ai_score:
                    message += " You win! 🎉"
                elif self.player_score < self.ai_score:
                    message += " AI wins! 🤖"
                else:
                    message += " It's a draw!"

            return {
                'message': message,
                'player_turn': self.player_turn,
                'round': min(self.round, MAX_ROUNDS),
                'player_score': self.player_score,
                'ai_score': self.ai_score,
                'ai_choice': player_save,
                'last_shot': ai_shot,
                'game_over': self.game_over
            }



game = PenaltyShootoutGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    choice = data.get('choice')

    # On first request or if game over, reset game
    if game.game_over:
        game.reset_game()

    result = game.play_round(choice)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
