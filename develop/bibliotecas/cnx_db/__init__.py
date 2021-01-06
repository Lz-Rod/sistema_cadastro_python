import pyodbc

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

def create(id, nome, sobrenome, nasc, sexo, alt, peso, prof, nacionalidade, paisRes, estMusical, estLivro, estGame):
    sql = "INSERT INTO tbPessoas VALUES('"+ nome +"', '"+ sobrenome +"', '"+ nasc +"', '"+ sexo +"', '"+ alt +"', '"+ peso +"', '"+ prof + "', '"+ nacionalidade +"', '"+ paisRes +"', '"+ estMusical +"', '"+ estLivro +"', '"+ estGame +"', '"+ id +"');"
    cursor.execute(sql)
    cnx.commit()

def read(item, val):
    sql = "SELECT * FROM tbPessoas WHERE "+ item +" = "+ val + ";"
    cursor.execute(sql)

    linhas = cursor.fetchall()#aqui ele exibirá todas as linhas do DB, o fetchone() exibe somente a primeira

    for linha in linhas:
        print(linha)

def update(id, item, alt):
    sql = "UPDATE tbPessoas SET " + item + " = '" + alt + "' WHERE id = '" + id + "';"
    cursor.execute(sql)
    cnx.commit()

def delete(id):
    sql = "DELETE FROM tbPessoas WHERE id = '"+ id +"';"
    cursor.execute(sql)
    cnx.commit()