

# main.py
import customtkinter as ctk
from send import Module1
from receive import Module2
from PIL import Image

class MainApplication(ctk.CTk):

    
    def switcher(self):
            if (self.switch_variable.get()=="off"):
                ctk.set_appearance_mode("light")
                ctk.set_default_color_theme("green")
            else:
                ctk.set_appearance_mode("dark")
                ctk.set_default_color_theme("green")
    
    def __init__(self):
        super().__init__()

        # Initialize the main window
        self.title("File Transfer")
        self.resizable(0, 0)
        self.geometry("500x400")

        #switch function for window themes
        self.switch_variable=ctk.StringVar(value="off")

        # Background Image
        bg_img = ctk.CTkImage(light_image=Image.open("./b.png"), dark_image=Image.open("./b.png"), size=(500, 400))
        bg_image = ctk.CTkLabel(self, image=bg_img, text="")
        bg_image.place(x=0, y=0)

        # Header

        frameTop=ctk.CTkFrame(self)
        frameTop.pack(fill="y")
        txt=ctk.CTkLabel(frameTop,text="Transfer Files",font=("algerian",20,"italic"),width=500,fg_color=("#002477","black"),height=40)
        txt.grid(row=0,column=0)
        switch=ctk.CTkSwitch(txt,text="Theme",command=self.switcher,variable=self.switch_variable,onvalue="on",offvalue="off",width=3)
        switch.place(x=410,y=10)

        # Buttons for sending and receiving
        frame = ctk.CTkFrame(self)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        img=ctk.CTkImage(dark_image=Image.open("./SEND1.png"),light_image=Image.open("./SEND1.png"),size=(40,30))
        send_image=ctk.CTkButton(frame,image=img,text="SEND",corner_radius=20,hover_color="purple",height=100,command=self.open_send_module)
        send_image.grid(row=0,column=0)
        
        img2=ctk.CTkImage(dark_image=Image.open("./recieve.png"),light_image=Image.open("./recieve.png"),size=(40,30))
        recieve_image=ctk.CTkButton(frame,image=img2,text="RECIEVE",corner_radius=20,hover_color="violet",height=100,command=self.open_receive_module)
        recieve_image.grid(row=0,column=1)

    def open_send_module(self):
        Module1(self)

    def open_receive_module(self):
        Module2(self)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

