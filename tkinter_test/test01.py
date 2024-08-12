import tkinter as tk
from tkinter import ttk

def create_app():
    root = tk.Tk()
    root.title("タブ切り替えアプリ")
    
    notebook = ttk.Notebook(root)

    # タブ1の作成
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="タブ1")
    tk.Label(tab1, text="これはタブ1の内容です。").pack(padx=10, pady=10)

    # タブ2の作成
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="タブ2")
    tk.Label(tab2, text="これはタブ2の内容です。").pack(padx=10, pady=10)

    # Notebookをパックして配置
    notebook.pack(expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    create_app()
