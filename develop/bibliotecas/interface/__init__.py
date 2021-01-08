from textwrap import wrap

def sep(tam = 60):
    print('-' * tam)

def titulo(texto, tam = 60):
    """
    -> Cria a formatação automática para os títulos
    :param texto: texto para o título
    :param tam: determina o tamanho do titulo, valor padrão 50
    :return: sem retorno
    """
    sep()
    print(f'{texto.center(tam)}')
    sep()

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
    titulo(texto)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    sep()
    opc = leiaInt('Escolha uma opção digitando seu número: ')
    return opc