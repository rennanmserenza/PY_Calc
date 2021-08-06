from components_calc import *
from classe_calculadora import Calculadora


def main():
    root = make_root()                  # chama a função que cria a janela

    
    label = make_label(root)            # define a variavel label com a função make_label
                                        # esta função recbe root como argumento
    
    display = make_display(root)        # atribui a váriavel display a função make_display 
                                        # que recebe root como argumento

    buttons = make_buttons(root)        # define a variável buttons como nosso ponto de
                                        # criação para os botões da nossa calculadora

    calculadora = Calculadora(
        root,
        label,
        display,
        buttons
        )                               # calculadora nossa váriavel que vai receber tudo que já foi criado
                                        # e iniciará nosso objeto calculadora.

    calculadora.start()                 # método start da nossa calculadora que vai executar nosso programa


if __name__ == "__main__":              
    # caso o parâmetro __name__ identifique que está sendo executado como main
    # e não como o nome do projeto em sí, ele irá executar esta função main,
    # isto é utilizado para você poder testar seu código sem ter que ficar apagando testes.
    main()
