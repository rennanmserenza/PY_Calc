import tkinter as tk
from typing import List

class Calculadora():
    
    def __init__(
        self, root: tk.Tk 
        # label: tk.Label, display: tk.Entry, 
        # buttons: List[List[tk.Button]]
        ):
        """[summary]

        Args:
            root (tk.Tk): [description]
        """

        self.root = root
        # self.label = label
        # self.display = display
        # self.buttons = buttons

    
    # def _config_buttons(self):
    #     pass


    # def _config_display(self):
    #     pass


    def start(self):
        # self._config_buttons()
        # self._config_display()
        self.root.mainloop()