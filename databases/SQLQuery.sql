/*
	Nova base de dados
	CREATE DATABASE dbCadastroPython;
*/


/* 
	Criar tabela

	CREATE TABLE tbPessoas (
		nome VARCHAR(30) NOT NULL,
		sobrenome VARCHAR(100) NOT NULL,
		nascimento DATE NOT NULL,
		sexo VARCHAR(1),
		altura DECIMAL(3,2),
		peso DECIMAL(5,2),
		profissao VARCHAR(30),
		nacionalidade VARCHAR(30) NOT NULL,
		paisResidencia VARCHAR(30) NOT NULL,
		comidaFavorita VARCHAR(30),
		estiloMusicalFavorito VARCHAR(30),
		estiloLivroFavorito VARCHAR(30),
		estiloGameFavorito VARCHAR(30)
	);
*/

/* 
	Inserir dado de teste
	INSERT INTO tbPessoas (nome, sobrenome, nascimento, sexo, altura, peso, profissao, nacionalidade, paisResidencia, comidaFavorita, estiloMusicalFavorito, estiloLivroFavorito, estiloGameFavorito)
	VALUES('Vitor', 'Rogsdorf', '1940-06-26', 'M', '2.30', '345.20', 'Desenvolvedor Senior', 'Maia', 'Brasil', 'Pizza', 'MPB', 'Ficção Cientifica', 'RPG');
*/

/* 
	Consultar dado de teste
	SELECT * FROM tbPessoas;
*/

