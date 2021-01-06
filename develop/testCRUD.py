import pyodbc

# Funçãod e retornar a conexão ao database
def conectar_sql():
    server = 'ODYSSEY-LZ\SQLEXPRESS'
    database = 'dbCadastroPython'
    string_conexao = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;'
    return pyodbc.connect(string_conexao)

#variável do cursor
conexao = conectar_sql()
cursor = conexao.cursor()

#CRUD


#CREATE
'''sql = "INSERT INTO tbPessoas VALUES('Otavio', 'Rodrigues', '2000-03-24', 'M', 1.80, 105.00, 'Estagiário TI', 'Brasil', 'Brasil', 'Lasanha', 'POP', 'Fantasia', 'FPS')"
cursor.execute(sql)
conexao.commit()'''

#READ
sql = "SELECT * FROM tbPessoas"
cursor.execute(sql)

#linha = cursor.fetchone()
#linhas = cursor.fetchone()
linhas = cursor.fetchall()#aqui ele exibirá todas as linhas do DB, o fetchone() exibe somente a primeira

for linha in linhas:
    print(linha)

#UPDATE
'''sql = "UPDATE tbPessoas SET sobrenome = 'Rodrigues' WHERE nome = 'Otavio';"
cursor.execute(sql)
conexao.commit()'''

#DELETE
'''sql = "DELETE FROM tbPessoas WHERE nome = 'Otavio'"
cursor.execute(sql)
conexao.commit()'''