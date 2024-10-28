
# send.py
import customtkinter as ctk
from tkinter import filedialog, messagebox
import socket
import os
import time
from PIL import Image

class Module1:
    global host
    host = socket.gethostname()
    def __init__(self, master):
        self.master = master
        self.filename = None
        self.x = 0

        # Create the send window
        self.send_win = ctk.CTkToplevel(master)
        self.send_win.title("Send")
        self.send_win.resizable(0, 0)
        self.send_win.geometry("500x400")

        # Background Image
        bg_img = ctk.CTkImage(light_image=Image.open("./b.png"), dark_image=Image.open("./b.png"), size=(500, 400))
        bg_image = ctk.CTkLabel(self.send_win, image=bg_img, text="")
        bg_image.place(x=0, y=0)

        # File Selection Label
        label = ctk.CTkLabel(self.send_win, text="BROWSE FILES", font=('Arial', 20, 'bold'),bg_color="#002477", text_color="white")
        label.place(x=160, y=10)

        imge=ctk.CTkImage(dark_image=Image.open("./antena.png"),light_image=Image.open("./antena.png"),size=(500,200))
        image=ctk.CTkLabel(self.send_win,image=imge,height=200,width=500,text=f"Host Id: {host}",text_color=("white"))
        image.place(x=0,y=150,anchor="nw")

        # Button to select file
        button = ctk.CTkButton(self.send_win, text="Select File", font=('Arial', 20, 'bold'),bg_color="#002477",text_color="white",width=100,height=30, command=self.select)
        button.place(x=130, y=100)

        # Button to send file
        button1 = ctk.CTkButton(self.send_win, text="Send", font=('Arial', 20, 'bold'),bg_color="#002477",text_color="white",width=70,height=30,corner_radius=10,border_color="black",
                          border_width=5,fg_color="#002447", command=self.sendfile)
        button1.place(x=250, y=100)

        self.send_win.protocol("WM_DELETE_WINDOW", self.on_close)

    def select(self):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                                    title="Select File",
                                                    filetypes=(("Text files", ".txt"), 
                                                               ("Image files", "*.png;*.jpg"), 
                                                               ("Video files", "*.mp4"), 
                                                               ("All files", "*.*")))
        if self.filename:  # Check if a file was selected
            self.x = 1

    def sendfile(self):
        if self.x == 0:
            messagebox.showwarning("Warning", "Select a file first")
            return

        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(f"Waiting for incoming connection at {host}:{port}...")
        conn, addr = s.accept()
        print(f"Connected to {addr}")

        total_bytes_sent = 0
        start_time = time.time()

        with open(self.filename, "rb") as file:
            file_data = file.read(1024)
            while file_data:
                conn.send(file_data)
                total_bytes_sent += len(file_data)
                file_data = file.read(1024)

        conn.close()
        end_time = time.time()
        elapsed_time = end_time - start_time

        transfer_speed = (total_bytes_sent / elapsed_time) / (1024 * 1024)  # in MB/s
        print("File has been transmitted successfully")
        messagebox.showinfo("Done", f"File transmitted successfully\nTransfer Speed: {transfer_speed:.2f} MB/second")
        self.on_close()

    def on_close(self):
        self.send_win.destroy()  # Close the send window
