"""A simple live digital clock built with Python's Tkinter library."""

from datetime import datetime
import tkinter as tk
from tkinter import ttk


def main() -> None:
    root = tk.Tk()
    root.title("Digital Clock")
    root.resizable(False, False)
    root.configure(padx=24, pady=20)

    time_label = ttk.Label(
        root,
        font=("Segoe UI", 40, "bold"),
        anchor="center",
    )
    time_label.pack()

    date_label = ttk.Label(
        root,
        font=("Segoe UI", 14),
        anchor="center",
    )
    date_label.pack(pady=(4, 0))

    def update_clock() -> None:
        now = datetime.now()
        time_label.configure(text=now.strftime("%H:%M:%S"))
        date_label.configure(text=now.strftime("%A, %B %d, %Y"))
        root.after(200, update_clock)

    update_clock()
    root.mainloop()


if __name__ == "__main__":
    main()