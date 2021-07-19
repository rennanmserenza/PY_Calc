from components_calc import *
from classe_calculadora import Calculadora


def main():
    root = make_root()                  # chama a função que cria a janela
    
    display = make_display(root)        # atribui a váriavel display a função make_display 
                                        # que recebe root como argumento

    label = make_label(root)            # define a variavel label com a função make_label
                                        # esta função recbe root como argumento

    # buttons = make_buttons(root)

    calculadora = Calculadora(root, display, label)
    #  buttons)
    calculadora.start()


if __name__ == "__main__":
    main()
