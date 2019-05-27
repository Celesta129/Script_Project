import tkinter as tk
import weather

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry:", entry)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5) #89c1ff <- 하늘색 색상
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entryX = tk.Entry(frame, bg='pink')
entryX.grid(row=30, column=1)

entryY = tk.Entry(frame, bg='pink')
entryY.grid(row=50, column=1)

button = tk.Button(frame, text="Input", bg='white', font=40, command=lambda:test_function(entryX.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

labelX = tk.Label(frame, text="X 좌표", bg='yellow')
labelX.grid(row=30, column=0)

labelY = tk.Label(frame, text="Y 좌표", bg='yellow')
labelY.grid(row=50, column=0)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

labelM = tk.Label(lower_frame)
labelM.place(relwidth=1, relheight=1)

root.mainloop()