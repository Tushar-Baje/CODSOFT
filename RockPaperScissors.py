import tkinter as tk
import random

def play(choice):
    global user_wins, computer_wins
    user_choice_text.set(f"You chose: {choice}")
    
    options = ["rock", "paper", "scissors"]
    computer_pick = random.choice(options)

    result_text.set(f"Computer picked: {computer_pick}.")

    if choice == computer_pick:
        result_text.set(result_text.get() + "\nIt's a tie!")
    elif (choice == "rock" and computer_pick == "scissors") or \
         (choice == "paper" and computer_pick == "rock") or \
         (choice == "scissors" and computer_pick == "paper"):
        user_wins += 1
        result_text.set(result_text.get() + "\nYou Win!")
    else:
        computer_wins += 1
        result_text.set(result_text.get() + "\nYou Lost!")

    score_text.set(f"You Won: {user_wins} times\nComputer Won: {computer_wins} times")
    
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)
    play_again_button.pack(pady=10)
    
def play_again():
    user_choice_text.set("You chose: ")
    result_text.set("Make your choice!")
    score_text.set(f"You Won: {user_wins} times\nComputer Won: {computer_wins} times")

    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)
    
    play_again_button.pack_forget()

def quit_game():
    root.destroy()

root = tk.Tk()
root.title("Rock Paper Scissors")

user_wins = 0
computer_wins = 0
user_choice_text = tk.StringVar()
user_choice_text.set("You chose: ")
result_text = tk.StringVar()
result_text.set("Make your choice!")
score_text = tk.StringVar()
score_text.set("You Won: 0 times\nComputer Won: 0 times")
rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
rock_button.pack(pady=10)
paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
paper_button.pack(pady=10)
scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))
scissors_button.pack(pady=10)
user_choice_label = tk.Label(root, textvariable=user_choice_text)
user_choice_label.pack(pady=10)
result_label = tk.Label(root, textvariable=result_text)
result_label.pack(pady=10)
score_label = tk.Label(root, textvariable=score_text)
score_label.pack(pady=10)
play_again_button = tk.Button(root, text="Play Again", command=play_again)
quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.pack(pady=20)


root.mainloop()
