from textwrap import wrap

cr = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',   # 1 - fundo vermelho, texto branco
     '\033[0;30;42m',   # 2 - fundo verde, texto branco
     '\033[0;30;43m',   # 3 - fundo amarelo, texto branco
     '\033[0;30;44m',   # 4 - fundo azul, texto branco
     '\033[0;30;45m',   # 5 - fundo roxo, texto branco
     '\033[0;30;46m',   # 6 - fundo ciano, texto branco
     '\033[7:30m',      # 7 - fundo branco, texto preto
     )

def sep(tam = 60):
    print('-' * tam)

def titulo(texto, tam = 60, cor=0):
    """
    -> Cria a formatação automática para os títulos
    :param texto: texto para o título
    :param tam: determina o tamanho do titulo, valor padrão 50
    :return: sem retorno
    """
    print(cr[cor], end='')
    sep()
    print(f'{texto.center(tam)}')
    sep()
    print(cr[0])

def texto(texto, tam = 60):
    """
    -> Cria um texto com quebra de linha automática
    :param texto: texto a ser quebrado
    :param tam: tamanho para quebra de linha, valor padrão 50
    :return: sem retorno
    """
    for linha in wrap(texto, width=tam):
        print(linha)

def erro(texto):
    print(f'\033[31m{texto}\033[m')

def sucesso(texto):
    print(f'\033[32m{texto}\033[m')

def leiaInt(texto):
    """
    -> Permite criar um imput de int para usar a opção numérica
    no menu principal
    :param texto: Receberá uma string para transformar em int
    :return: retorna o valor convertido para int
    """
    while True:
        try:
            n = int(input(texto))
        except(ValueError, TypeError):
            erro('ERR0! Digite uma opção válida.')
            continue
        except(KeyboardInterrupt):
            erro('Usuário preferiu não escolher nenhuma opção.')
            return 0
        else:
            return n

def menu(texto, lista):
    """
    -> Cria um menu numérico baseado em uma lista
    :param texto: título para o menu
    :param lista: lista de itens que o menu terá
    :return: retorna o numero digitado do menu pelo usuário
    """

    titulo(texto, cor=5)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    sep()
    opc = leiaInt('Escolha uma opção digitando seu número: ')
    return opc