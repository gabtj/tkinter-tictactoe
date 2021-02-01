import tkinter as tk
from tkinter import messagebox


class Game:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.master.title("TicTacToe")

        self.master.resizable(False, False)

        self.lbl_header = tk.Label(text="TicTacToe",
                                   font=('Arial', 25, 'bold roman'))
        self.lbl_header.grid(row=0, columnspan=3, pady=10)

        self.total_moves = tk.IntVar() # Total moves made
        self.total_moves.set(0)
        self.lbl_total_moves_text = tk.Label(text="Total moves: ", font=('Arial', 15, 'bold roman'))
        self.lbl_total_moves_text.grid(row=1, columnspan=2, pady=5)
        self.lbl_total_moves = tk.Label(textvariable=self.total_moves, font=('Arial', 15, 'bold roman'))
        self.lbl_total_moves.grid(row=1, column=2)

        self.generate_buttons()

        self.lbl_player_turn = tk.Label(text="Player 1 turn", font=('Arial', 15, 'bold roman'))
        self.lbl_player_turn.grid(row=5, columnspan=3, pady=5)


    def button_click(self, b):
        """ Changes button to X or O based based on the move number. Evaluates
        moves to see if there is a winner.
        """
        value = int(self.lbl_total_moves["text"])
        if value in [0, 2, 4, 6, 8]:
            b.config(text="X", state="disabled", bg="#b8ffb8")
        elif value in [1, 3, 5, 7, 9]:
            b.config(text="O", state="disabled", bg="#ffb8b8")
        self.evaluate_move()


    def generate_buttons(self):
        """ Generates buttons for the game grid.
        """
        self.btn_1 = tk.Button(text=".", font=('Arial', 10, 'bold roman'), width=5, height=2, command=lambda: self.button_click(self.btn_1))
        self.btn_1.grid(row=2, column=0, ipady=15, ipadx=15)
        self.btn_2 = tk.Button(text=".", font=('Arial', 10, 'bold roman'), width=5, height=2, command=lambda: self.button_click(self.btn_2))
        self.btn_2.grid(row=2, column=1, ipady=15, ipadx=15)
        self.btn_3 = tk.Button(text=".", font=('Arial', 10, 'bold roman'), width=5, height=2, command=lambda: self.button_click(self.btn_3))
        self.btn_3.grid(row=2, column=2, ipady=15, ipadx=15)

        self.btn_4 = tk.Button(text=".", font=('Arial', 10, 'bold roman'), width=5, height=2, command=lambda: self.button_click(self.btn_4))
        self.btn_4.grid(row=3, column=0, ipady=15, ipadx=15)
        self.btn_5 = tk.Button(text=".", font=('Arial', 10, 'bold roman'), width=5, height=2, command=lambda: self.button_click(self.btn_5))
        self.btn_5.grid(row=3, column=1, ipady=15, ipadx=15)
        self.btn_6 = tk.Button(text=".", font=('Arial', 10, 'bold roman'), width=5, height=2, command=lambda: self.button_click(self.btn_6))
        self.btn_6.grid(row=3, column=2, ipady=15, ipadx=15)

        self.btn_7 = tk.Button(text=".", font=('Arial', 10, 'bold roman'), width=5, height=2, command=lambda: self.button_click(self.btn_7))
        self.btn_7.grid(row=4, column=0, ipady=15, ipadx=15)
        self.btn_8 = tk.Button(text=".", font=('Arial', 10, 'bold roman'), width=5, height=2, command=lambda: self.button_click(self.btn_8))
        self.btn_8.grid(row=4, column=1, ipady=15, ipadx=15)
        self.btn_9 = tk.Button(text=".", font=('Arial', 10, 'bold roman'), width=5, height=2, command=lambda: self.button_click(self.btn_9))
        self.btn_9.grid(row=4, column=2, ipady=15, ipadx=15)
        self.btn_9.rowconfigure(4, weight=1)
        self.btn_9.columnconfigure(2, weight=1)


    def change_player_turn(self):
        """
        Change text at the bottom of the application based on the player
        turn.
        """
        value = int(self.lbl_total_moves["text"])
        if value in [0, 2, 4, 6, 8]:
            self.lbl_player_turn.config(text="Player 1 turn")
        elif value in [1, 3, 5, 7, 9]:
            self.lbl_player_turn.config(text="Player 2 turn")


    def evaluate_move(self):
        """ Evaluate move to see if there is a winner.
        """
        value = int(self.lbl_total_moves["text"])
        if self.check_marker() is 1:
            messagebox.showinfo(title="Winner", message="Player 1 wins!")
            self.play_again()
        elif self.check_marker() is 2:
            messagebox.showinfo(title="Winner", message="Player 2 wins!")
            self.play_again()
        elif self.check_marker() is 0:
            messagebox.showinfo(message="Draw!")
            self.play_again()
        else:
            self.total_moves.set(value + 1)
            self.change_player_turn()


    def button_click(self, b):
        """ Changes button b to "X" or "O" based on player turn.
        """
        value = int(self.lbl_total_moves["text"])
        if value in [0, 2, 4, 6, 8]:
            b.config(text="X", state="disabled", bg="#b8ffb8")
        elif value in [1, 3, 5, 7, 9]:
            b.config(text="O", state="disabled", bg="#ffb8b8")
        self.evaluate_move()


    def play_again(self):
        """ Messageboxes that ask if user wants to play again.
        """
        msg = messagebox.askyesno(title="Play Again?",
                                  message="Would you like to play again?")
        if msg is True:
            messagebox.showinfo(title="Reset", message="Board reset!")
            self.total_moves.set(0)
            self.generate_buttons()
        else:
            self.quit()


    def check_marker(self):
        """ Checks if marker is "X" or "O" based on number of moves completed.
        """
        value = int(self.lbl_total_moves["text"])
        marker = '.'

        if value in [0, 2, 4, 6, 8]:
            marker = "X"
        elif value in [1, 3, 5, 7, 9]:
            marker = "O"

        return self.check_winner(marker)


    def check_winner(self, marker):
        """ Checks if the marker forms a completed row, col, or diagonal.

        Return 1 if player one has valid combination. Return 2 if player
        two has valid combination. Return 0 if draw.
        """
        # Rows
        if self.btn_1["text"] == marker and self.btn_2["text"] == marker and self.btn_3["text"] == marker:
            return self.return_winner(marker)
        if self.btn_4["text"] == marker and self.btn_5["text"] == marker and self.btn_6["text"] == marker:
            return self.return_winner(marker)
        if self.btn_7["text"] == marker and self.btn_8["text"] == marker and self.btn_9["text"] == marker:
            return self.return_winner(marker)

        # Col
        if self.btn_1["text"] == marker and self.btn_4["text"] == marker and self.btn_7["text"] == marker:
            return self.return_winner(marker)
        if self.btn_2["text"] == marker and self.btn_5["text"] == marker and self.btn_8["text"] == marker:
            return self.return_winner(marker)
        if self.btn_3["text"] == marker and self.btn_6["text"] == marker and self.btn_9["text"] == marker:
            return self.return_winner(marker)

        # Diagonal
        if self.btn_1["text"] == marker and self.btn_5["text"] == marker and self.btn_9["text"] == marker:
            return self.return_winner(marker)
        if self.btn_3["text"] == marker and self.btn_5["text"] == marker and self.btn_7["text"] == marker:
            return self.return_winner(marker)

        # Draw
        if int(self.lbl_total_moves["text"]) == 8:
            return 0


    def return_winner(self, marker):
        """ If a valid combination is detected in check_winner, this function
        returns 1 if winner is player 1, returns 2 if winner is player 2.
        """
        if marker == "X":
            return 1
        if marker == "O":
            return 2


    def quit(self):
        """ Prompts user to close the application.
        """
        msg = messagebox.askyesno(title='Quit', message="Quit?")
        if msg is True:
            self.master.destroy()
        else:
            self.play_again()


if __name__ == "__main__":
    window = tk.Tk()
    my_gui = Game(window)
    window.mainloop()
