import re
import math
import tkinter as tk
from typing import List

class Calculadora():
    
    def __init__(                                                               # Parâmetros iniciais do nosso objeto
        self, root: tk.Tk, display: tk.Entry,
        label: tk.Label, buttons: List[List[tk.Button]]
        ):
        
        self.root = root
        self.display = display
        self.label = label
        self.buttons = buttons

    
    def clear(self, event=None):                                                # Função de limpeza de display
        self.display.delete(0, 'end')


    def add_text_to_display(self, event=None):                                  # Função de adição de conteúdo no display por clique no botão
        self.display.insert('end', event.widget['text'])


    def _fix_text(self, text):                                                  # Filtro do display com expressões regulares
        # Substitui tudo que não for 0123456789.+-/*()^ para nada
        text = re.sub(r'[^\d\.\/\*\-\+\(\)\^e]', r'', text, 0)

        # Substitui sinais repetidos para apenas um sinal
        text = re.sub(r'([\.\/\*\-\+\^])\1', r'\1', text, 0)
        
        #Substitui () ou *() para nada ''
        text = re.sub(r'\*?\(\)', '', text)

        return text


    def _get_equations(self, text):                                             # Faz segmentação dos calculos onde houver uma potenciação
        return re.split(r'\^', text, 0)


    def calculate(self, event=None):
        fixed_text = self._fix_text(self.display.get())
        equations = self._get_equations(fixed_text)
        print(equations)


    def _config_buttons(self):                                                  # Configuração do que cada botão faz
        buttons = self.buttons
        
        for r_value in buttons:
            for button in r_value:
                button_text = button['text']

                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)

                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)

                if button_text == '=':
                    button.bind('<Button-1>', self.calculate)


    def _config_display(self):
        ...   


    def start(self):
        self._config_buttons()
        self._config_display()
        self.root.mainloop()