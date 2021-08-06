import re
import math
import tkinter as tk
from typing import List

class Calculadora():
    
    def __init__(                                                               # Parâmetros iniciais do nosso objeto
        self, root: tk.Tk, label: tk.Label,
        display: tk.Entry, buttons: List[List[tk.Button]]
        ):                                                                      # Definimos tbm a ordem de execução de parâmetros.
        
        self.root = root
        self.label = label
        self.display = display        
        self.buttons = buttons

    
    def clear(self, event=None):                                                # Função de limpeza de Display e Label com botão C
        self.display.delete(0, 'end')
        self.label.config(text='Digite uma operação!')


    def add_text_to_display(self, event=None):                                  # Função de adição de conteúdo no display
                                                                                # por clique no botão, ou teclado
        self.display.insert('end', event.widget['text'])


    def _fix_text(self, text):                                                  # Filtro do display com expressões regulares
                                                                                # impede a repetição ou inserção de valores inválidos.
        # Substitui tudo que não for 0123456789.+-/*()^ para nada
        text = re.sub(r'[^\d\.\/\*\-\+\(\)\^e]', r'', text, 0)

        # Substitui sinais repetidos para apenas um sinal
        text = re.sub(r'([\.\/\*\-\+\^])\1', r'\1', text, 0)
        
        #Substitui () ou *() para nada ''
        text = re.sub(r'\*?\(\)', '', text)

        return text


    def _get_equations(self, text):                                             # Faz segmentação dos calculos onde houver uma potenciação
        return re.split(r'\^', text, 0)


    def calculate(self, event=None):                                            # Lógica da calculadora, efetua operações básicas
                                                                                # efetua operações de potenciação com a lib Math
                                                                                # possuí tratamento para alguns erros
        fixed_text = self._fix_text(self.display.get())
        equations = self._get_equations(fixed_text)
        
        try:
            if len(equations) == 1:
                result = eval(self._fix_text(equations[0]))

            else:
                result = eval(self._fix_text(equations[0]))

                for equation in equations[1:]:
                    result = math.pow(result, eval(self._fix_text(equation)))

            self.display.delete(0, 'end')                                       # Limpa o display após realizar a conta
            self.display.insert('end', result)                                  # Insere no display limpo o resultado
            self.label.config(text=f'{fixed_text} = {result}')                  # Insere no Label a expressão executada e resultado

        except OverflowError:
            self.label.config(text='Não consigo realizar essa conta!')
        except Exception:
            self.label.config(text='Error! Não consigo fazer isso!')


    def _config_buttons(self):                                                  # Configuração do que cada botão faz
        buttons = self.buttons
        
        for r_value in buttons:
            for button in r_value:
                button_text = button['text']

                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)
                    button.config(bg='#EA4335', fg='#fff')

                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)

                if button_text == '=':
                    button.bind('<Button-1>', self.calculate)
                    button.config(bg='#4785F4', fg='#fff')


    def _config_display(self):                                                  # Funções de limpeza de display com tecla return
                                                                                # Função de botão igual com a tecla enter
        self.display.bind('<Return>', self.calculate)
        self.display.bind('<KP_Enter>', self.calculate) 


    def start(self):
        self._config_buttons()
        self._config_display()
        self.root.mainloop()