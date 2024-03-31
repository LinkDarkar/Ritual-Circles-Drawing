import tkinter
import warnings
import customtkinter
from PIL import ImageTk,Image

from ritual import Ritual
from ritualObject import RitualObject
from window import MainWindow, UserInterface

mainWindow = MainWindow()
userInterface = UserInterface(mainWindow)
mainWindow.startWindow()

# this will not start until the window finishes
ritualTest = Ritual()
ritualTest.printTest()
ritualObjectTest = RitualObject()
ritualTest.addRitualObject(ritualObjectTest)

if (ritualTest.ritualObjects):
    print("TEST")
    ritualTest.ritualObjects[0].printTest()

# A
if (__name__ == '__main__'):
    print("shit has been done")

# TEST