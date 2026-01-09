import tkinter as tk

root = tk.Tk()
root.title("ferestra")
root.geometry("300x200")

buton_inchide = tk.Button(root, text="inchide fereastra", command=root.destroy)
buton_inchide.pack(pady=50)

root.mainloop()
