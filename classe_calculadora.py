import tkinter as tk
from typing import List

class Calculadora():
    
    def __init__(
        self, root: tk.Tk, display: tk.Entry,
        label: tk.Label, buttons: List[List[tk.Button]]
        ):
        

        self.root = root
        self.display = display
        self.label = label
        self.buttons = buttons

    
    # def _config_buttons(self):
    #     pass


    # def _config_display(self):
    #     pass


    def start(self):
        # self._config_buttons()
        # self._config_display()
        self.root.mainloop()