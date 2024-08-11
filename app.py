import tkinter as tk
from tkinter import filedialog
import os

class imageToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.image_path = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self):
        title_label = tk.Label(self.root, text="image to pdf converter", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        # command=self.select_images
        select_images_button = tk.Label(self.root, text="Select Images")
        select_images_button.pack(pady=(0, 10))

        self.selected_images_listbox.pack(pady=(0,10), fill=tk.BOTH, expand=True)

        label = tk.Label(self.root, text="Enter output PDF name:")
        label.pack()

        pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, width=40, justify='center')
        pdf_name_entry.pack()
        # command=self.convert_images_to_pdf
        convert_button = tk.Label(self.root, text="convert to pdf")
        convert_button.pack(pady=(20, 40))

def main():
    root = tk.Tk()
    root.title("image to pdf")
    converter = imageToPdfConverter(root)
    root.geometry("400x600")
    root.mainloop()

if __name__ == "__main__":
    main()