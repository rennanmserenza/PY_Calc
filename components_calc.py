import tkinter as tk
from typing import List
from tkinter import Button, font


def make_root() -> tk.Tk:
    """Função que cria nossa GUI

    Returns:
        tk.Tk: retorno da nossa tela com as configurações que aplicamos, a saída é verificada para ser igual a tk.Tk
    """

    root = tk.Tk()                                      # define a variável root como sendo nossa tela
    
    root.title('Py_Calc')                               # definimos o nome da nossa janela
    
    root.resizable(False, False)                        # definimos que nossa janela não terá tamanho
                                                        # regulável pelo usuário, o primeiro argumento
                                                        # se refere ao ajuste de largura, o segundo se
                                                        # refere ao ajuste de altura
    
    root.config(padx=10, pady=10, background='#fff')    # define as configurações de estilo
                                                        # da nossa janela    

    return root                                         # retorno da nossa função sendo root -> tk.Tk
                                                        # e suas configurações
                                                        

def display_control_a(event):                           # função de evento de click
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    
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

    display.grid(row=0, column=0, 
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


def make_label(root) -> tk.Label:
    """Cria um espaço que será usado para exibir nossos resultado e contas
    Args:
        root : Nossa tela de exibição do tkinter

    Returns:
        tk.Label: Retorna tk.Label como sendo nossa label configurada e pronta para uso
    """
    label = tk.Label(
        root, text='Sem conta ainda', anchor='e',
         justify='right', background='#fff'
    )                                                   # função label, cria um espaço na nossa root
                                                        # onde ficarão nossos resultados de conta
                                                        # text define um texto de exibição na label,
                                                        # anchor='e' define o label como alinhado a direita
                                                        # justify ='right' define o alinhamento do texto a direita
                                                        # background='#fff' define como a cor de fundo sem branca
    
    label.grid(
        row=1, column=0, 
        columnspan=5, sticky="news"
    )                                                   # define o grid da label, linha 1, column 0
                                                        # columnspan recebe 5 espaços de coluna
                                                        # sticky define que ele irá preencher todos os espaços em todas as direções

    return label


def make_buttons(root) -> List[List[tk.Button]]:
    """Função para gerar nossos botões da calculadora

    Args:
        root : nossa tela com todos os elementos postos nela até o momento

    Returns:
        buttons -> List[List[tk.Button]]: Retorna botões com seus valores definidos em uma lista.
    """
    button_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '=']
    ]                                                   # button_texts é um mapa de botão que usaremos a seguir
                                                        # button_texts é uma váriavel que armazena strings
                                                        # dentro de listas, dentro de uma lista principal

    buttons: List[List[tk.Button]] = []                 # variável buttons, é uma lista com listas de botão do tipo
                                                        # tk.Button, e ela armazenará nossos valores de botões

    for r_index, r_value in enumerate(button_texts, start=2):
        button_row = []                                 # variável tipo lista para armazenar botão de cada linha
                                                        # variável é sempre limpa quando inicia-se uma nova linha

        for c_index, c_value in enumerate(r_value):
            btn = tk.Button(root, text=c_value)         # gera um botão com o valor contido na posição correspondente
                                                        # na matriz button_texts
            btn.grid(row=r_index, column=c_index,
             sticky='news', padx=5, pady=5)             # define o grid do botão tendo como base o indice da lista e
                                                        # o indice do texto presente na lista para posiciona-lo
                                                        # sticky define o batão sendo expandido para todos lados igualmente
                                                        # com padding de 5px na vertical e na horizontal

            btn.config(font=('Helvetica', 15, 'normal'),
                pady=40, width=1, background='#f1f2f3', border=0,
                cursor='hand2', highlightthickness=0, highlightcolor='#ccc',
                highlightbackground='#ccc', activebackground='#ccc'
            )                                           # configura os estilos dos botões, font Helvetica, 15px, normal(sem negrito)
                                                        # define um padding de 40px na vertical, todos com msm width, e cor de fundo
                                                        # sendo f1f2f3, sem bordas, tipo de cursor sendo hand 2, activebackgroun
                                                        # refere-se a cor de fundo ao ser clicado o botão.

            button_row.append(btn)                      # envia nosso botão para a lista button_row
        
        buttons.append(button_row)                      # ao final de cada listagem da nossa button_row enviamos essa lista para nossa
                                                        # lista de botões que é uma matriz declarada antes do nosso FOR

    return buttons                                      # retorna buttons sendo uma lista com strings dentro de uma lista
                                                        # configurado como decidido