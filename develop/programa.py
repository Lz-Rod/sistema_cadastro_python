from bibliotecas import interface, cnx_db
from time import sleep

interface.titulo('SISTEMA DE CADASTRO', cor=6)
interface.texto('Nesse sistema você pode criar, consultar, atualizar e excluir cadastros em um database SQL.')

cnx_db.cnx_sql()

while True:
    escolha = interface.menu('Menu Principal', ['Criar cadastro', 'Ver cadastro', 'Atualizar cadastro', 'Excluir cadastro', 'Sair do sistema'])

    #criar cadastros
    if escolha == 1:
        while True:
            interface.titulo('Criar cadastro', cor=2)
            nome = str(input('Informe o nome: '))
            sobrenome = str(input('informe o sobrenome: '))
            nasc = str(input('informe a data de nascimento [AAAA-MM-DD]: '))
            sexo = str(input('Informe o sexo [M/F]: '))
            altura = str(input('Informe a altura em MTs, com separador ponto para CM ex: [1.70]: '))
            peso = str(input('Informe o peso em KG com separador ponto para GR ex: [95.50]: '))
            profissao = str(input('Informe a profissão: '))
            nacionalidade = str(input('Informe a nacionalidade: '))
            paisRes = str(input('Informe o país de residência: '))
            comidaFav = str(input('Informe a comida favorita: '))
            genMusical = str(input('Informe o gênero musical favorito: '))
            genLivro = str(input('Informe o gênero de livro favorito: '))
            genGame = str(input('Informe o gênero de game favorito: '))

            cnx_db.create(nome, sobrenome, nasc, sexo, altura, peso, profissao, nacionalidade, paisRes, comidaFav, genMusical, genLivro, genGame)

            continuar = str(input('Deseja fazer um novo cadastro? [S/N]')).upper()
            if continuar == 'N':
                break

    #ver cadastros
    elif escolha == 2:
        while True:
            interface.titulo('Ver cadastros', cor=4)
            print('Parâmetros:\n1 - ID\n2 - nome\n3 - País de Residência')
            escolhaVerCadastro = int(input("Escolha o parâmetro para realizar a busca: "))
            valorVerCadastro = str(input("Digite o valor da busca: "))

            if escolhaVerCadastro == 1:
                cnx_db.read('id', valorVerCadastro)
                continuar = str(input('Deseja fazer uma nova busca? [S/N]')).upper()
                if continuar == 'N':
                    break
            elif escolhaVerCadastro == 2:
                cnx_db.read('nome', valorVerCadastro)
                continuar = str(input('Deseja fazer uma nova busca? [S/N]')).upper()
                if continuar == 'N':
                    break
            elif escolhaVerCadastro == 3:
                cnx_db.read('paisResidencia', valorVerCadastro)
                continuar = str(input('Deseja fazer uma nova busca? [S/N]')).upper()
                if continuar == 'N':
                    break
            else:
                print(f"ERRO! {escolhaVerCadastro} não é um parâmetro válido!")



    #Atualizar cadastros
    elif escolha == 3:
        cnx_db.validarUpdate()

    #excluir cadastros
    elif escolha == 4:
        cnx_db.validarDelete()

    elif escolha == 5:
        interface.titulo('Saindo do sistema... Até logo!')
        break
    else:
        interface.erro('ERRO! Opção inválida.')
    sleep(0.5)