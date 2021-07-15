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


def display_control_a(event):                           # função de evento de click
    event.widget.select_range(0, 'end')
    event.widget.incursor('end')
    
    return 'break'


def make_display(root) -> tk.Entry:
    """Cria o display de input da calculadora.

    Args:
        root: Janela da aplicação, domínio principal.

    Returns:
        tk.Entry: Retorna uma entrada de valores.
    """
    display = tk.Entry(root)                            # define display como portador da entrada
                                                        # é um input

    display.grid(row=1, column=0, 
    columnspan=5, sticky="news", pady=(0, 10))          # define o grid do display, começando na
                                                        # primeira linha ocupando a coluna 0
                                                        # e se expandindo por todas as colunas
                                                        # da calculadora nos sentidos definidos
                                                        # por sticky North, East, West e South 
                                                        # e com padding y de 0 top e 10 botton
    
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right', bd=1, relief='flat',
        highlightthickness=2, highlightcolor='#ccc'
    )                                                   # define as configurações de estilo da
                                                        # label, tendo font de 40px, tipo bold,
                                                        # texto justificado a direita, borda de 1px
                                                        # relief é o relevo quando clicamos na nossa label
                                                        # highlightthickness recebendo 2px, é o contorno da nossa label
                                                        # highlightcolor é a cor da nossa borda


    display.bind('<Control-a>', display_control_a)      # bind -> conecta a funcionalidade de um
                                                        # evento a uma função, neste caso o click do mouse

    return display                                      # retorno da função tk.Entry, configurado


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