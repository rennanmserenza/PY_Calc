from components_calc import *
from classe_calculadora import Calculadora


def main():
    root = make_root()                  #chama a função que cria a janela
    
    # display = make_display(root)
    # label = make_label(root)
    # buttons = make_buttons(root)

    calculadora = Calculadora(root)
    #  label, display, buttons)
    calculadora.start()


if __name__ == "__main__":
    main()
