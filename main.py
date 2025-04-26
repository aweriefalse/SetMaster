import tkinter as tk
import constants as const
import windows as ws


def focus(event):
    if event:
        main_window.config(takefocus=True)

def start_main_program():
    global main_window
    main_window = MainWindow()
    main_window.focus_force()

    main_window.bind("<F11>", main_window.max_minimize)
    main_window.bind("<Escape>", main_window.kill)

    main_window.after(250, focus, 1)
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
