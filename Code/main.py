from tkinter import *
import customtkinter
from PIL import ImageTk,Image
from ritual import Ritual
from ritualObject import RitualObject

# I still don't know what any of this does... kinda... ????????????
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
imageTest = ImageTk.PhotoImage(Image.open("./Assets/circle_test.jpg"))
window.iconbitmap("./Assets/HeheHehe.ico")      # I spent an hour just to be able to do this
window.title("PAIN")
window.geometry("1280x960")

frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#label = customtkinter.CTkLabel(master=frame, text="UWU", font=('Roboto',24))
label = customtkinter.CTkLabel(master=frame, image=imageTest)
label.pack(pady=12, padx=10)

window.mainloop()

ritualTest = Ritual()
ritualTest.printTest()
ritualObjectTest = RitualObject()
ritualObjectTest.printTest()

# A
if __name__ == '__main__':
    print("shit has been done")