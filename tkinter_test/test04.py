import tkinter as tk
from tkinter import ttk

def switch_tab(notebook, tab_index):
    notebook.select(tab_index)

def create_app():
    root = tk.Tk()
    root.title("Tab Switcher App")
    root.geometry("400x300")

    # Notebook（タブ）を作成
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    # タブ1の内容
    tab1 = ttk.Frame(notebook)
    label1 = tk.Label(tab1, text="This is Tab 1", font=("Arial", 16))
    label1.pack(pady=50)
    notebook.add(tab1, text="Tab 1")

    # タブ2の内容
    tab2 = ttk.Frame(notebook)
    label2 = tk.Label(tab2, text="This is Tab 2", font=("Arial", 16))
    label2.pack(pady=50)
    notebook.add(tab2, text="Tab 2")
    button22 = tk.Button(tab2, text="Switch to Tab 2", command=lambda: switch_tab(notebook, 1))
    button22.pack(side="left", padx=10)

    # タブ3の内容
    tab3 = ttk.Frame(notebook)
    label3 = tk.Label(tab3, text="This is Tab 3", font=("Arial", 16))
    label3.pack(pady=50)
    notebook.add(tab3, text="Tab 3")

    # タブ切り替えボタン
    button_frame = tk.Frame(root)
    button_frame.pack(fill="x", pady=10)

    button1 = tk.Button(button_frame, text="Switch to Tab 1", command=lambda: switch_tab(notebook, 0))
    button1.pack(side="left", padx=10)

    button2 = tk.Button(button_frame, text="Switch to Tab 2", command=lambda: switch_tab(notebook, 1))
    button2.pack(side="left", padx=10)

    button3 = tk.Button(button_frame, text="Switch to Tab 3", command=lambda: switch_tab(notebook, 2))
    button3.pack(side="left", padx=10)

    root.mainloop()

if __name__ == "__main__":
    create_app()
