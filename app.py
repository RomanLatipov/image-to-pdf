import tkinter as tk
from tkinter import filedialog
import os

class imageToPdfConverter:
    def __init__(self, root):
        self.root = root

        self.initialize_ui()

def initialize_ui(self):
    title_label = tk.Label(self.root, text="image to pdf converter", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

def main():
    root = tk.Tk()
    root.title("image to pdf")
    root.geometry("400x600")
    root.mainloop()

if __name__ == "__main__":
    main()