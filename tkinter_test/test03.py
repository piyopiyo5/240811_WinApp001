import tkinter as tk

def create_landscape(canvas):
    # 空の描画
    canvas.create_rectangle(0, 0, 800, 400, fill="skyblue", outline="")
    
    # 太陽の描画
    canvas.create_oval(600, 50, 700, 150, fill="yellow", outline="orange", width=2)
    
    # 山の描画
    canvas.create_polygon(100, 400, 300, 150, 500, 400, fill="darkgreen", outline="black")
    canvas.create_polygon(300, 400, 500, 100, 700, 400, fill="forestgreen", outline="black")
    
    # 川の描画
    canvas.create_polygon(0, 400, 800, 400, 800, 600, 0, 600, fill="blue", outline="blue")
    
    # 木の描画
    for x in range(100, 800, 150):
        draw_tree(canvas, x, 350)
    
    # 草の描画
    for x in range(10, 800, 20):
        canvas.create_line(x, 400, x + 10, 380, fill="green", width=2)

def draw_tree(canvas, x, y):
    # 幹の描画
    canvas.create_rectangle(x-10, y, x+10, y+50, fill="saddlebrown", outline="")
    
    # 葉の描画 (三層の楕円)
    canvas.create_oval(x-30, y-50, x+30, y+10, fill="darkgreen", outline="")
    canvas.create_oval(x-25, y-70, x+25, y-10, fill="forestgreen", outline="")
    canvas.create_oval(x-20, y-90, x+20, y-30, fill="green", outline="")

def create_app():
    root = tk.Tk()
    root.title("Advanced Canvas Drawing")
    root.geometry("800x600")

    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack()

    create_landscape(canvas)

    root.mainloop()

if __name__ == "__main__":
    create_app()
