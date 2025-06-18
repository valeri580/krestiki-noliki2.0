import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.geometry("300x400")
        self.window.resizable(False, False)

        self.current_player = "X"
        self.buttons = []
        self.player_choice = None

        self.setup_menu()
        self.setup_buttons()
        self.setup_reset_button()

        self.window.mainloop()

    def setup_menu(self):
        menu_frame = tk.Frame(self.window)
        menu_frame.pack(pady=10)

        tk.Label(menu_frame, text="Выберите символ:", font=("Arial", 12)).pack()

        choice_frame = tk.Frame(menu_frame)
        choice_frame.pack()

        tk.Button(choice_frame, text="X", font=("Arial", 12), width=3,
                  command=lambda: self.set_player("X")).pack(side=tk.LEFT, padx=5)
        tk.Button(choice_frame, text="O", font=("Arial", 12), width=3,
                  command=lambda: self.set_player("O")).pack(side=tk.LEFT, padx=5)

    def set_player(self, choice):
        self.player_choice = choice
        self.current_player = "X"  # X всегда ходит первым
        messagebox.showinfo("Начало игры", f"Вы играете за {choice}. X ходит первым.")

    def setup_buttons(self):
        game_frame = tk.Frame(self.window)
        game_frame.pack()

        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(game_frame, text="", font=("Arial", 24), width=3, height=1,
                                bg="#f0f0f0", activebackground="#e0e0e0",
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def setup_reset_button(self):
        reset_frame = tk.Frame(self.window)
        reset_frame.pack(pady=10)

        tk.Button(reset_frame, text="Новая игра", font=("Arial", 12),
                  command=self.reset_game, bg="#4CAF50", fg="white").pack()

    def check_winner(self):
        # Проверка строк
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True

        # Проверка столбцов
        for i in range(3):
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True

        # Проверка диагоналей
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True

        return False

    def check_draw(self):
        for row in self.buttons:
            for btn in row:
                if btn["text"] == "":
                    return False
        return True

    def on_click(self, row, col):
        if self.player_choice is None:
            messagebox.showwarning("Выбор символа", "Пожалуйста, выберите символ (X или O) сначала!")
            return

        if self.buttons[row][col]["text"] != "":
            return

        self.buttons[row][col]["text"] = self.current_player
        self.buttons[row][col]["fg"] = "red" if self.current_player == "X" else "blue"

        if self.check_winner():
            messagebox.showinfo("Игра окончена", f"Игрок {self.current_player} победил!")
            self.reset_game()
            return

        if self.check_draw():
            messagebox.showinfo("Игра окончена", "Ничья!")
            self.reset_game()
            return

        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for row in self.buttons:
            for btn in row:
                btn["text"] = ""
                btn["fg"] = "black"

        self.current_player = "X"
        self.player_choice = None


if __name__ == "__main__":
    TicTacToe()
