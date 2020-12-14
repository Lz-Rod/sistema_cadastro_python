from bibliotecas import interface
from time import sleep
interface.titulo('SISTEMA DE CADASTRO')
interface.texto('Nesse sistema você pode criar, consultar e excluir cadastros em um database SQL.')

while True:
    escolha = interface.menu('Menu Principal', ['Criar cadastro', 'Ver cadastro', 'Excluir cadastro', 'Sair do sistema'])
    if escolha == 1:
        interface.titulo('Criar cadastro')
    elif escolha == 2:
        interface.titulo('Ver cadastros')
    elif escolha == 3:
        interface.titulo('Escluir cadastro')
    elif escolha == 4:
        interface.titulo('Saindo do sistema... Até logo!')
        break
    else:
        interface.erro('ERRO! Opção inválida.')
    sleep(0.5)