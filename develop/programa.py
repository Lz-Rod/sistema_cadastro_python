from bibliotecas import interface, cnx_db
from time import sleep
interface.titulo('SISTEMA DE CADASTRO')
interface.texto('Nesse sistema você pode criar, consultar e excluir cadastros em um database SQL.')

cnx_db.cnx_sql()

while True:
    escolha = interface.menu('Menu Principal', ['Criar cadastro', 'Ver cadastro', 'Atualizar cadastro', 'Excluir cadastro', 'Sair do sistema'])
    if escolha == 1:
        interface.titulo('Criar cadastro')
    elif escolha == 2:

        while True:
            interface.titulo('Ver cadastros')
            print('Parâmetros:\n1 - ID\n2 - nome\n3 - País de Residência')
            escolhaVerCadastro = int(input("Escolha o parâmetro para realizar a busca: "))
            valorVerCadastro = str(input("Digite o valor da busca: "))
            if escolhaVerCadastro == 1:
                cnx_db.read('id', valorVerCadastro)
                continuar = str(input('Deseja fazer uma nova busca? [S/N]')).upper()
                if continuar == 'N':
                    break
            elif escolhaVerCadastro == 2:
                cnx_db.read('nome', "'" + valorVerCadastro + "'")#necessário aspas simples na string para reconhecer o DB
                continuar = str(input('Deseja fazer uma nova busca? [S/N]')).upper()
                if continuar == 'N':
                    break
            elif escolhaVerCadastro == 3:
                cnx_db.read('paisResidencia', "'" + valorVerCadastro + "'")
                continuar = str(input('Deseja fazer uma nova busca? [S/N]')).upper()
                if continuar == 'N':
                    break
            else:
                print(f"ERRO! {escolhaVerCadastro} não é um parâmetro válido!")

    elif escolha == 3:
        interface.titulo('Atualizar cadastro')
    elif escolha == 4:
        interface.titulo('Escluir cadastro')
    elif escolha == 5:
        interface.titulo('Saindo do sistema... Até logo!')
        break
    else:
        interface.erro('ERRO! Opção inválida.')
    sleep(0.5)