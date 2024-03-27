import tkinter as tk
from tkinter import filedialog
import pyqrcode

def generate_qr():
    link = entry.get()
    qr_code = pyqrcode.create(link)
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    qr_code.png(save_path, scale=5)
    status_label.config(text="QR Code generated sucessfully!")

root = tk.Tk()
root.title("QR Code Generator")

label = tk.Label(root, text="Insert the link:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
