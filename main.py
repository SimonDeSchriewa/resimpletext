"""Here is where everything begins!"""
from tkinter import *
from tkinter import ttk
from src.file_manager import file_manager as fm

def main():
    #root = Tk()
    #root.mainloop()
    content = fm.open_file('PLAN.md')
    print(fm.convert_str_to_html(content))


if __name__ == '__main__':
    main()
