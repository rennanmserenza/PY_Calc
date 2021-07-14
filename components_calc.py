import tkinter as tk
from typing import List
from tkinter import Button, font


def make_root() -> tk.Tk:
    """Função que cria nossa GUI

    Returns:
        tk.Tk: retorno da nossa tela com as configurações que aplicamos, a saída é verificada para  
               ser igual a tk.Tk
    """

    root = tk.Tk()                              # define a variável root como sendo nossa tela
    
    root.title('Py_Tk_Calculadora')             # definimos o nome da nossa janela
    
    root.resizable(False, False)                # definimos que nossa janela não terá tamanho
                                                # regulável pelo usuário, o primeiro argumento
                                                # se refere ao ajuste de largura, o segundo se
                                                # refere ao ajuste de altura
    
    root.config(padx=10, pady=10, background='#fff')    # define as configurações de estilo
                                                        # da nossa janela    

    return root                                         # retorno da nossa função sendo root -> tk.Tk
                                                        # e suas configurações
                                                        


# def make_label(root) -> tk.Label:
#     label = tk.Label(
#         root, text='Sem conta ainda',
#         anchor='e', justify='right', background='#fff'
#     )
#     label.grid(row=0, column=0, columnspan=5, sticky="news")

#     return label


# def display_control_a(event):
#     event.widget.select_range(0, 'end')
#     event.widget.incursor('end')
    
#     return 'break'


# def make_display(root) -> tk.Entry:
#     display = tk.Entry(root)
#     display.grid(row=1, column=0, columnspan=5, sticky="news", pady=(0, 10))
    
#     display.config(
#         font=('Helvetica', 40, 'bold'),
#         justify='right', bd=1, relief='flat',
#         highlightthickness=1, highlightcolor='#ccc'
#     )
#     display.bind('<Control-a>', display_control_a)

#     return display


# def make_buttons(root) -> List[List[tk.Button]]:
#     button_texts: List[List[str]] = [
#         ['7', '8', '9', '+', 'C'],
#         ['4', '5', '6', '-', '/'],
#         ['1', '2', '3', '*', '^'],
#         ['0', '.', '(', ')', '='],
#     ]

#     buttons: List[List[tk.Button]] = []

#     for row_index, row_value in enumerate(button_texts, start=2):
#         button_row = []
#         for collum_index, collum_value in enumerate(row_value):
#             btn = tk.Button(root, text=collum_value)
#             btn.grid(row=row_index, column=collum_index, sticky='news', padx=5, pady=5)

#             btn.config(font=('Helvetica', 15, 'normal'),
#                 pady=40, width=1, background='#d1e2f3', border=0,
#                 cursor='hand2', highlightthickness=0, highlightcolor='#ccc',
#                 highlightbackground='#ccc', activebackground='#ccc'
#             )

#             button_row.append(btn)
        
#         buttons.append(button_row)

#     return buttons