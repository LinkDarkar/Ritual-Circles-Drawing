import tkinter
import warnings
import customtkinter
from PIL import ImageTk,Image
from ritual import Ritual
from ritualObject import RitualObject

# I still don't know what any of this does... kinda... ?
# Maybe I should leave this in it's own file?
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
imageTest = customtkinter.CTkImage(Image.open("./Assets/circle_test.jpg"), size=(598,571))
window.iconbitmap("./Assets/HeheHehe.ico")      # I spent an hour just to be able to do this
window.title("PAIN")
window.geometry("1280x960")

frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#label = customtkinter.CTkLabel(master=frame, text="UWU", font=('Roboto',24))
label = customtkinter.CTkLabel(master=frame, image=imageTest)
label.pack(pady=120, padx=100)

window.mainloop()

# this will not start until the window finishes
ritualTest = Ritual()
ritualTest.printTest()
ritualObjectTest = RitualObject()
ritualTest.addRitualObject(ritualObjectTest)
if (ritualTest.ritualObjects):
    # Same concept as the first if statement in Ritual.addRitualObject()
    # but it checks if the list even has something in the first place
    # again, wouldn't it be exhausting to have this everytime we want to do something?
    # tho we might not even use this in the end...
    # I think I'm getting ahead of myself here
    print("TEST")
    ritualTest.ritualObjects[0].printTest()

# A
if (__name__ == '__main__'):
    print("shit has been done")