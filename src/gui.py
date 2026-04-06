# CB 1st How to Make a GUI
import tkinter as tk





root = tk.Tk()

root.title("Testing")
root.configure(background="pink")
root.minsize(250, 250)
root.maxsize(1000,1000)
root.geometry("300x300+100+100")
label = tk.Label(root, text="This is currently working!", font = ("Times New Roman",14,"bold"))
label.config(background = "pink")
# stuff about button
root.count = 0
def add():
    root.count += 1
    show_count.pack()

show_count = tk.Label(root, text=root.count)
show_count.pack()
tk.Button(root, text = "ADD", command=add).pack()


label.pack()

root.mainloop()