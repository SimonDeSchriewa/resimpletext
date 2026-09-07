from ..file_manager.file_manager import *

class Controler:
    def __init__(self, view: 'GUI'):
        with open('PLAN.md', 'r') as f:
            text = f.read()
        view.raw.insert(1, text)
        view.view.load_html(convert_str_to_html(text))
