import tkinter as tk
from tkinter import ttk

def create_app():
    root = tk.Tk()
    root.title("Notebook Example with LabelFrame")
    root.geometry("400x300")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    # LabelFrameを追加
    label_frame = ttk.LabelFrame(notebook, text="ラベル付きフレーム")
    notebook.add(label_frame, text="Tab with LabelFrame")
    
    # LabelFrame内にウィジェットを追加
    label = tk.Label(label_frame, text="Label inside LabelFrame")
    label.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_app()
