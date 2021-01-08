import pyodbc
from bibliotecas import interface

def cnx_sql():
    """
    -> Cria a conexão entre o programa e o DB SQL server
    :return: retorna a conexão
    """
    server = 'ODYSSEY-LZ\SQLEXPRESS'
    database = 'dbCadastroPython'
    string_conexao = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;'
    return pyodbc.connect(string_conexao)

#variáveis do cursor
cnx = cnx_sql()
cursor = cnx.cursor()

def create(nome, sobrenome, nasc, sexo, altura, peso, profissao, nacionalidade, paisRes, comidaFav, genMusical, genLivro, genGame):

    sql = f"INSERT INTO tbCadastros VALUES('{nome}', '{sobrenome}', '{nasc}', '{sexo}', {altura}, {peso}, '{profissao}', '{nacionalidade}', '{paisRes}', '{comidaFav}', '{genMusical}', '{genLivro}', '{genGame}')"
    cursor.execute(sql)
    cnx.commit()

def read(item, val):
    sql = f"SELECT * FROM tbCadastros WHERE {item} = '{val}'"
    cursor.execute(sql)

    linhas = cursor.fetchall()#aqui ele exibirá todas as linhas do DB, o fetchone() exibe somente a primeira

    if len(linhas) > 0:
        if item != 'id':
            interface.sep()
            print(f'Registros encontrados com a busca {val}: {len(linhas)}')
            interface.sep()
        else:
            interface.sep()

        for coluna in linhas:
            print(f'{"ID:":<15} {coluna[0]}')
            print(f'{"Nome:":<15} {coluna[1]} {coluna[2]}')
            print(f'{"Nasc.:":<15} {coluna[3]}')
            print(f'{"Sexo:":<15} {coluna[4]}')
            print(f'{"Altura:":<15} {coluna[5]}')
            print(f'{"Peso:":<15} {coluna[6]}')
            print(f'{"Profissão:":<15} {coluna[7]}')
            print(f'{"Nacionalidade:":<15} {coluna[8]}')
            print(f'{"País Res.:":<15} {coluna[9]}')
            print(f'{"Comida Fav.:":<15} {coluna[10]}')
            print(f'{"Gen. Musical:":<15} {coluna[11]}')
            print(f'{"Gen. Leitura:":<15} {coluna[12]}')
            print(f'{"Gen. Game:":<15} {coluna[13]}')
            interface.sep()

        if item != 'id':
            print(f'Registros encontrados com a busca {val}: {len(linhas)}')
            interface.sep()

    else:
        interface.erro("ERRO! A busca não retornou resultados.")

def validarUpdate():
    """
    -> Valida a existencia de algum registro com o ID buscado, em caso positivo executa a função update
    :return: retorna o valor atualizado no DB
    """
    while True:
        interface.titulo('Atualizar cadastro')
        idAlterar = str(input('Informe o ID do cadastro que deseja alterar: '))
        while True:
            sql = f"SELECT * FROM tbCadastros WHERE id= '{idAlterar}'"
            cursor.execute(sql)
            linhas = cursor.fetchall()

            if len(linhas) == 0:
                interface.erro(f'ERRO! ID:{idAlterar} inexistente, tente outro.')
                break

            else:
                read('id', idAlterar)
                print(
                    'Opções que você pode alterar:\n1 - Profissão\n2 - País de residência\n3 - Comida Favorita\n4 - Genero Musical Favorito\n5 - Gerero de livro favorito\n6 - Genero de game favorito\n7 - Cancelar alteração')
                escolhaAlt = int(input('Escolha a opção acima pelo seu número: '))
                if escolhaAlt == 7:
                    break
                else:
                    alteracao = str(input('Informe a alteração: '))
                    itemAlterar = {1: 'profissao', 2: 'paisresidencia', 3: 'comidaFavorita', 4: 'estiloMusicalFavorito',
                                   5: 'estiloLivroFavorito', 6: 'estiloGameFavorito'}
                    update(idAlterar, itemAlterar[escolhaAlt], alteracao)
                    continuar = str(input(f'Deseja alterar algo mais do cadastro de ID {idAlterar}? [S/N]: ')).upper()
                    if continuar == 'N':
                        break
        continuarNovo = str(input(f'Deseja alterar outro cadastro? [S/N]: ')).upper()
        if continuarNovo == 'N':
            break


def update(id, item, alt):
    sql = f"UPDATE tbCadastros SET {item} = '{alt}' WHERE id = '{id}';"
    cursor.execute(sql)
    cnx.commit()

def validarDelete():
    """
    -> Valida a existencia de algum registro com o ID buscado, em caso positivo executa a função update
    :return: remove o registro do DB
    """
    while True:
        interface.titulo('Escluir cadastro')
        escolhaId = str(input('Informe o ID do cadastro que deseja excluir: '))

        sql = f"SELECT * FROM tbCadastros WHERE id= '{escolhaId}'"
        cursor.execute(sql)
        linhas = cursor.fetchall()

        if len(linhas) == 0:
            interface.erro(f'ERRO! ID:{escolhaId} inexistente, tente outro.')

        else:
            while True:
                read('id', escolhaId)
                decisao = str(input('Tem certeza que deseja excluir esse cadastro? [S/N]: ')).upper()
                if decisao == 'S':
                    delete(escolhaId)
                    print(f'ID: {escolhaId} removido com sucesso!')
                    break
                else:
                    break
        excluirMais = str(input('Deseja excluir mais algum registro? [S/N]: ')).upper()
        if excluirMais == 'N':
            break

def delete(id):
    sql = f"DELETE FROM tbCadastros WHERE id = '{id}';"
    cursor.execute(sql)
    cnx.commit()