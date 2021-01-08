from bibliotecas import interface, cnx_db
from time import sleep
interface.titulo('SISTEMA DE CADASTRO')
interface.texto('Nesse sistema você pode criar, consultar e excluir cadastros em um database SQL.')

cnx_db.cnx_sql()

while True:
    escolha = interface.menu('Menu Principal', ['Criar cadastro', 'Ver cadastro', 'Atualizar cadastro', 'Excluir cadastro', 'Sair do sistema'])

    #criar cadastros
    if escolha == 1:
        while True:
            interface.titulo('Criar cadastro')
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
        '''
        #tentativa anterior ao tratamento de erros
        while True:
            interface.titulo('Atualizar cadastro')
            idAlterar = str(input('Informe o ID do cadastro que deseja alterar: '))
            cnx_db.read('id', idAlterar)
            while True:
                print('Opções que você pode alterar:\n1 - Profissão\n2 - País de residência\n3 - Comida Favorita\n4 - Genero Musical Favorito\n5 - Gerero de livro favorito\n6 - Genero de game favorito')
                escolhaAlt = int(input('Escolha a opção acima pelo seu número: '))
                alteracao = str(input('Informe a alteração: '))
                itemAlterar = {1:'profissao', 2:'paisresidencia', 3:'comidaFavorita', 4:'estiloMusicalFavorito', 5:'estiloLivroFavorito', 6:'estiloGameFavorito'}
                cnx_db.update(idAlterar, itemAlterar[escolhaAlt], alteracao)
                continuar = str(input(f'Deseja alterar algo mais do cadastro de ID {idAlterar}? [S/N]: ')).upper()
                if continuar == 'N':
                    break
            continuarNovo = str(input(f'Deseja alterar outro cadastro? [S/N]: ')).upper()
            if continuarNovo == 'N':
                break'''

    #excluir cadastros
    elif escolha == 4:
        cnx_db.validarDelete()
        '''
        #Tentativa anterior ao tratamento de erros
        while True:
            interface.titulo('Escluir cadastro')
            escolhaId = str(input('Informe o ID do cadastro que deseja excluir: '))
            cnx_db.read('id', escolhaId)
            decisao = str(input('Tem certeza que deseja excluir esse cadastro? [S/N]: ')).upper()
            if decisao == 'S':
                cnx_db.delete(escolhaId)
            else:
                break
            excluirMais = str(input('Deseja exluir mais algum registro? [S/N]: ')).upper()
            if excluirMais == 'N':
                break'''

    elif escolha == 5:
        interface.titulo('Saindo do sistema... Até logo!')
        break
    else:
        interface.erro('ERRO! Opção inválida.')
    sleep(0.5)