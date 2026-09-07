"""The gui of the program."""
from tkinter import *
from tkinter import ttk
from tkinterweb import HtmlFrame


class GUI:
    """This class holds the definitions of the gui's widgets."""

    def __init__(self, master: Tk, padding=0) -> None:
        self.master = master
        # The Top Frame with the open and the switch buttons
        self.top_frame = ttk.Frame(master, padding=padding)
        self.top_frame.grid(column=0, row=0, sticky='we')

        # Widgets on Top Frame
        self.open_btn = ttk.Button(self.top_frame)
        self.open_btn.grid(column=0, row=0)
        self.open_btn.grid_anchor('w')
        self.open_btn['text'] = 'open'

        self.switch_btn = ttk.Button(self.top_frame)
        self.switch_btn.grid(column=1, row=0)
        self.switch_btn.grid_anchor('center')
        self.switch_btn['text'] = 'switch'
        self.switch_btn['command'] = self.switch

        # The Middle Frame with the view and raw widget
        self.mid_frame = ttk.Frame(master, padding=padding)
        self.mid_frame.grid(column=0, row=1)

        # True=view is above, False=view is not above and None= none is above
        self.switch_state = True

        # The Middle Frame widgets
        self.raw = ttk.Entry(self.mid_frame)
        self.raw.grid(column=0, row=0, sticky='nsew')
        self.raw.grid_anchor('w')
        #self.raw['state'] = 'readonly'

        self.view = HtmlFrame(self.mid_frame)
        self.view.grid(column=0, row=0)
        self.view.grid_anchor('e')
        self.view.load_html('<p>Hello!<p/>')

        # True=view is above, False=view is not above and None= none is above
        self.switch_state = True

    def switch(self):
        if self.switch_state is None:
            self.view.grid(column=0)
            self.view.lift()
            self.switch_state = True
        elif self.switch_state is True:
            self.raw.lift()
            self.switch_state = False
        else:
            self.view.grid(column=1)
            self.switch_state = None

