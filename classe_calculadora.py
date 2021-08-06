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

    
    def clear(self, event=None):            #Função de limpeza de display
        self.display.delete(0, 'end')


    def _config_buttons(self):
        buttons = self.buttons
        
        for r_value in buttons:
            for button in r_value:
                button_text = button['text']

                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)

    # def _config_display(self):
    #     pass


    def start(self):
        self._config_buttons()
        # self._config_display()
        self.root.mainloop()