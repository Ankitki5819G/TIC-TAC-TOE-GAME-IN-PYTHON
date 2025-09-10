import tkinter as tk
from tkinter import messagebox

# Player symbols
current_player = "X"

# Function to check winner
def check_winner():
    global current_player
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            messagebox.showinfo("Game Over", f"Player {buttons[row][0]['text']} Wins!")
            reset_game()
            return
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            messagebox.showinfo("Game Over", f"Player {buttons[0][col]['text']} Wins!")
            reset_game()
            return
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        messagebox.showinfo("Game Over", f"Player {buttons[0][0]['text']} Wins!")
        reset_game()
        return
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        messagebox.showinfo("Game Over", f"Player {buttons[0][2]['text']} Wins!")
        reset_game()
        return

    # Check for draw
    if all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_game()

# Function when button is clicked
def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        check_winner()
        current_player = "O" if current_player == "X" else "X"

# Reset game
def reset_game():
    global current_player
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""

# Main window
root = tk.Tk()
root.title("Tic Tac Toe 🎮")

buttons = [[None for _ in range(3)] for _ in range(3)]

for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                                  command=lambda r=r, c=c: on_click(r, c))
        buttons[r][c].grid(row=r, column=c)

reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 14), command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()