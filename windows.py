import tkinter as tk
from tkinter.messagebox import showinfo
import constants as const
import main


class WelcomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.resizable(True, True)
        size = f"{const.WWINDOW_WIDTH}x{const.WWINDOW_HEIGHT}"
        pos = f"+{screen_width // 2 - const.WWINDOW_WIDTH // 2}+{screen_height // 2 - const.WWINDOW_HEIGHT // 2}"
        self.geometry(f"{size}{pos}")

        self.config(
            bg=const.BACKGROUND_COLOR,
            relief="groove",
            takefocus=True
        )
        self.resizable(False, False)

        self.overrideredirect(True)

        def throw_username(event=None):
            if len(username_inp.get()) >= 3:
                if len(username_inp.get()) > 12:
                    username = f"{username_inp.get()[:12]}..."
                else:
                    username = username_inp.get()
                const.USERNAME = username
                self.destroy()
                main.start_main_program()
            else:
                showinfo("Некорректные данные", "Минимальная длина имени:\n3 символа")

        def kill(event=None):
            self.destroy()
            exit(0)

        welcome_label = tk.Label(
            self,
            text="Мастер Множеств\nприветствует вас!",
            font=(const.DEFAULT_FONT, 16, "bold"),
            fg="white", bg=const.BACKGROUND_COLOR
        )
        welcome_label.pack(pady=10)

        dialog_logo = tk.PhotoImage(file="Images/dialog_logo.png", width=50, height=50, format="png")
        welcome_logo = tk.Label(
            self,
            image=dialog_logo
        )
        welcome_logo.pack(pady=5)

        ask_name_label = tk.Label(
            self,
            text="Как вас звать?",
            font=(const.DEFAULT_FONT, 16, "bold"),
            fg="lightgrey", bg=const.BACKGROUND_COLOR
        )
        ask_name_label.place(relx=0.05, rely=0.5)

        username_inp = tk.Entry(
            self,
            width=14,
            bg="lightgrey",
            fg=const.BACKGROUND_COLOR,
            font=(const.DEFAULT_FONT2, 15, "bold")
        )
        username_inp.place(relx=0.05, rely=0.65)

        throw_username_button = tk.Button(
            self,
            width=4,
            height=1,
            text="OK",
            font=(const.DEFAULT_FONT2, 16, "bold"),
            fg="lightgrey",
            bg=const.BACKGROUND_COLOR,
            command=throw_username
        )
        throw_username_button.place(relx=0.7, rely=0.615)

        self.bind("<Return>", throw_username)
        self.bind("<Escape>", kill)


def open_welcome_window():
    welcome_window = WelcomeWindow()
    welcome_window.mainloop()