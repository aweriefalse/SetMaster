import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import constants as const
import windows as ws


def start_main_program():
    global main_window
    main_window = MainWindow()
    main_window.focus_force()

    def chapter1_start():
        main_window.destroy()
        ws.chapter1_start()

    style = ttk.Style()
    style.configure(
        "My.TFrame",
        background=const.BACKGROUND_COLOR,
        borderwidth=const.BORDER_WIDTH
    )

    text_style = ttk.Style()
    text_style.configure(
        "My.TLabel",
        background=const.BACKGROUND_COLOR,
        foreground="white",
        font=(const.DEFAULT_FONT, 15, "bold")
    )

    tabline = ttk.Notebook(main_window, height = 20, style="My.TLabel")

    main_menu = ttk.Frame(tabline, style="My.TFrame")
    theory_practice = ttk.Frame(tabline, style="My.TFrame")
    set_calc = ttk.Frame(tabline, style="My.TFrame")

    tabline.add(main_menu, text="Главное меню")
    tabline.add(theory_practice, text="Теория & Практика")
    tabline.add(set_calc, text="Калькулятор множеств")
    tabline.pack(expand=True, fill="both")

    info_label = tk.Label(
        main_menu,
        text=const.WELCOME.format(const.USERNAME),
        font=(const.DEFAULT_FONT2, 16, "bold"),
        bg=const.BACKGROUND_COLOR,
        fg="white",
        wraplength=const.MWINDOW_WIDTH - 40
    )
    info_label.pack(pady=10, anchor="n")

    made_by_label = tk.Label(
        main_menu,
        text=const.MADE_BY,
        font=(const.DEFAULT_FONT2, 14),
        bg=const.BACKGROUND_COLOR,
        fg="lightgrey"
    )
    made_by_label.place(relx=1, rely=1, anchor="se")

    intersection_img = Image.open("Images/intersection1.png")
    intersection_img = ImageTk.PhotoImage(intersection_img.resize((200, 132)))
    intersection_label = tk.Label(
        main_menu,
        image=intersection_img,
        bg=const.BACKGROUND_COLOR
    )
    intersection_label.image = intersection_img
    intersection_label.place(relx=0.5, rely=0.62, anchor="center")


    chapter1 = tk.Button(
        theory_practice,
        text="Глава 1.\nПонятие множества и базовые примеры.",
        font=(const.DEFAULT_FONT, 16),
        height = theory_practice.winfo_height() // 3,
        width = theory_practice.winfo_width() // 5,
        borderwidth=const.BORDER_WIDTH,
        bg="grey",
        fg="white",
        command=chapter1_start
    )
    chapter1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

    chapter2 = tk.Button(
        theory_practice,
        text="Глава 2.\nОперации со множествами. Примеры задач.",
        font=(const.DEFAULT_FONT, 16),
        height=theory_practice.winfo_height() // 3,
        width=theory_practice.winfo_width() // 5,
        borderwidth=const.BORDER_WIDTH,
        bg="grey",
        fg="white",
       # command=ws.chapter2_start
    )
    chapter2.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.2)

    main_window.bind("<F11>", main_window.max_minimize)
    main_window.bind("<Escape>", main_window.kill)

    main_window.mainloop()

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.resizable(True, True)
        size = f"{const.MWINDOW_WIDTH}x{const.MWINDOW_HEIGHT}"
        pos = f"+{screen_width // 2 - const.MWINDOW_WIDTH // 2}+{screen_height // 2 - const.MWINDOW_HEIGHT // 2}"
        self.geometry(f"{size}{pos}")

        self.config(
            bg=const.BACKGROUND_COLOR,
            relief="groove",
            borderwidth=const.BORDER_WIDTH,
            takefocus=False
        )
        self.minsize(width=const.MWINDOW_WIDTH, height=const.MWINDOW_HEIGHT)

        self.iconbitmap("Images/dialog_logo.ico")
        self.title("Set Master")

    def max_minimize(self, event):
        if event:
            if self.attributes("-fullscreen"):
                self.attributes("-fullscreen", False)
            else:
                self.attributes("-fullscreen", True)

    def kill(self, event):
        self.destroy()
        exit(0)

if __name__ == "__main__":
    ws.open_welcome_window()