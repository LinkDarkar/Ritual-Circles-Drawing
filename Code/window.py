import tkinter
import customtkinter
from PIL import ImageTk,Image

class MainWindow():
    def __init__(self):
        # window initialization
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.window = customtkinter.CTk()
        self.window.iconbitmap("./Assets/HeheHehe.ico")
        self.window.title("PAIN")
        self.window.geometry("1280x720")

        self.frame = customtkinter.CTkFrame(master=self.window)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # test code
        #self.label = customtkinter.CTkLabel(master=self.frame, text="UWU", font=('Roboto',24))
        self.imageTest = customtkinter.CTkImage(Image.open("./Assets/circle_test.jpg"), size=(598,571))
        self.label = customtkinter.CTkLabel(master=self.frame, image=self.imageTest)
        self.label.pack(pady=120, padx=100)
    
    def startWindow(self):
        self.window.mainloop()

    def killWindow(self):
        print("button pressed")
        self.window.destroy()

class UserInterface():
    def __init__(self, window: MainWindow):
        # initializes user interface separately from the window
        print("sadfiojghhjidsafggjfdhiaskp")
        self.closeButton = NormalButton(window, window.killWindow, "Quit", 0.5, 0.5, tkinter.SW)

class NormalButton():
    def __init__(self, window: MainWindow, function, buttonText, relX, relY, buttonAnchor):
        self.button = customtkinter.CTkButton(master=window.window, text=buttonText, command=function)
        self.button.place(relx=relX, rely=relY, anchor=buttonAnchor)

# So, we will need some kinds of buttons, for example we will have to need drop downs
# so maybe we can define classes so we can only give them the necessary info for 
# them to be initialized and do their shit without copying and pasting
# a hundred times for every button that we want???????