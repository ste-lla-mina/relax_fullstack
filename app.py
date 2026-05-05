from flask import Flask, render_template, request
import random

app = Flask(__name__)

game_state = {"user_score": 0, "computer_score": 0, "last_result": "Make your move!"}

@app.route("/", methods=["GET", "POST"])  
def index():
    options = ["rock", "paper", "scissors"]

    if request.method == "POST":
        user_choice = request.form.get("choice")
        computer_choice = random.choice(options)

        if user_choice == computer_choice:
            res = f"It's a tie! Both chose {user_choice}."
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            res = f"You won!"
            game_state["user_score"] += 1
        else:
            res = f"You lost!"
            game_state["computer_score"] += 1
        
        game_state["last_result"] = res

    return render_template("index.html", state=game_state)

@app.route("/reset")
def reset():
    global game_state
    game_state = {"user_score": 0, "computer_score": 0, "last_result": "Scores reset! Make your move."}
    return render_template("index.html", state=game_state)

if __name__ == "__main__":   
     app.run(debug=True)