
# receive.py
import customtkinter as ctk
from tkinter import messagebox
import socket
import time
from PIL import Image

class Module2:
    def __init__(self, master):
        self.master = master
        self.SenderId = None
        self.incomingfile = None

        # Create the receive window
        self.receive_win = ctk.CTkToplevel(master)
        self.receive_win.title("Receive")
        self.receive_win.resizable(0, 0)
        self.receive_win.geometry("500x400")

        # Background Image
        bg_img = ctk.CTkImage(light_image=Image.open("./b.png"), dark_image=Image.open("./b.png"), size=(500, 400))
        bg_image = ctk.CTkLabel(self.receive_win, image=bg_img, text="")
        bg_image.place(x=0, y=0)

        imge=ctk.CTkImage(dark_image=Image.open("./trans.png"),light_image=Image.open("./trans.png"),size=(500,180))
        image=ctk.CTkLabel(self.receive_win,image=imge,height=180,width=500)
        image.place(x=0,y=0)

        # Input for Sender ID
        label = ctk.CTkLabel(self.receive_win, text="Enter Sender ID",fg_color="#002477", font=("algerian", 12), text_color="white")
        label.place(x=10, y=150)

        self.SenderId = ctk.CTkEntry(self.receive_win)  # Initialize the Entry widget
        self.SenderId.place(x=10, y=180)
        self.SenderId.focus()

        # Input for Incoming File Name
        lab = ctk.CTkLabel(self.receive_win, text="Filename for the incoming file:", font=("algerian", 12),fg_color="#002477", text_color="white")
        lab.place(x=10, y=220)

        self.incomingfile = ctk.CTkEntry(self.receive_win, width=220)  # Initialize the Entry widget
        self.incomingfile.place(x=10, y=250)

        # Receive button
        rr = ctk.CTkButton(self.receive_win, text="Receive", width=100,bg_color="#39c790",font=("arial",14,"bold"),command=self.receiver)
        rr.place(x=20, y=300)

        self.receive_win.protocol("WM_DELETE_WINDOW", self.on_close)

    def receiver(self):
        Id = self.SenderId.get()  # Get the sender's ID from the entry
        filename1 = self.incomingfile.get()  # Get the filename for the incoming file

        s = socket.socket()
        port = 8080
        s.connect((Id, port))

        total_bytes_received = 0
        start_time = time.time()

        with open(filename1, "wb") as file:
            file_data = s.recv(1024)
            while file_data:
                file.write(file_data)
                total_bytes_received += len(file_data)
                file_data = s.recv(1024)

        s.close()
        end_time = time.time()
        elapsed_time = end_time - start_time

        transfer_speed = (total_bytes_received / elapsed_time) / (1024 * 1024)  # in MB/s
        print("File has been received successfully")
        messagebox.showinfo("Done", f"File {filename1} has been received successfully\nTransfer Speed: {transfer_speed:.2f} MB/second")
        self.on_close()

    def on_close(self):
        self.receive_win.destroy()  # Close the receive window
