"""Here is where everything begins!"""
from tkinter import *
from tkinter import ttk
from tkinterweb import HtmlFrame
from src.file_manager import file_manager as fm
from src.gui import gui
from src.controler.controler import Controler

def main():
    root = Tk()

    view = gui.GUI(root, 20)
    control = Controler(view)

    root.mainloop()


if __name__ == '__main__':
    main()
