import tkinter as tk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import webbrowser
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
                if len(username_inp.get()) > 15:
                    username = f"{username_inp.get()[:15]}..."
                else:
                    username = username_inp.get()
                const.USERNAME = username
                print(f"USERNAME: {const.USERNAME}")
                self.destroy()
                main.start_main_program()
            else:
                showinfo("Некорректные данные", "Минимальная длина имени:\n3 символа")

        def open_page(event=None):
            self.withdraw()
            try:
                webbrowser.open("https://estaldialog.edumsko.ru/")
                self.attributes("-topmost", 1)
                self.after(1000, lambda: self.attributes("-topmost", 0))
            except Exception as e:
                print(f"Request has not been completed due to error:\n{e}")

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

        img = Image.open("Images/dialog_logo.png")
        dialog_logo = ImageTk.PhotoImage(img.resize((50, 50)))
        welcome_logo_button = tk.Button(
            self,
            image=dialog_logo,
            bg=const.BACKGROUND_COLOR,
            borderwidth=const.BORDER_WIDTH,
            command=open_page
        )
        welcome_logo_button.image = dialog_logo
        welcome_logo_button.pack()

        ask_name_label = tk.Label(
            self,
            text="Как вас звать?",
            font=(const.DEFAULT_FONT, 16, "bold"),
            fg="lightgrey", bg=const.BACKGROUND_COLOR
        )
        ask_name_label.place(relx=0.05, rely=0.6)

        username_inp = tk.Entry(
            self,
            width=14,
            bg="lightgrey",
            fg=const.BACKGROUND_COLOR,
            font=(const.DEFAULT_FONT2, 15, "bold"),
            validate="focus"
        )
        username_inp.place(relx=0.05, rely=0.75)

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

        throw_username_button.place(relx=0.7, rely=0.715)
        self.bind("<Return>", throw_username)
        self.bind("<Escape>", kill)


class ReadWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        def fullscreen(event):
            if event:
                if self.attributes("-fullscreen"):
                    self.attributes("-fullscreen", False)
                else:
                    self.attributes("-fullscreen", True)

        def kill(event):
            self.destroy()
            main.start_main_program()

        self.iconbitmap("Images/dialog_logo.ico")
        self.title("Set Master")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.resizable(True, True)
        size = f"{const.MWINDOW_WIDTH}x{const.MWINDOW_HEIGHT}"
        pos = f"+{screen_width // 2 - const.MWINDOW_WIDTH // 2}+{screen_height // 2 - const.MWINDOW_HEIGHT // 2}"
        self.geometry(f"{size}{pos}")
        self.minsize(width=const.MWINDOW_WIDTH, height=const.MWINDOW_HEIGHT)

        self.config(
            bg=const.BACKGROUND_COLOR2
        )

        self.bind("<F11>", fullscreen)
        self.bind("<Escape>", kill)


def open_welcome_window():
    welcome_window = WelcomeWindow()
    welcome_window.mainloop()

def chapter1_start():
    chapt1_window = ReadWindow()

    text1 = ctk.CTkTextbox(
        chapt1_window,
        text_color="white",
        font=(const.DEFAULT_FONT2, 22),
        corner_radius=20,
        wrap="word"
    )
    text1.insert("0.0", const.INFO1)
    text1.configure(state="disabled")
    text1.place(relx=0.99, rely=0.01, relwidth=0.78, relheight=0.98, anchor="ne")

    chapt1_window.mainloop()