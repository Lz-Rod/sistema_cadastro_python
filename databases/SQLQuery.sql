/*
create table tbCadastros (
	id int IDENTITY(1,1) PRIMARY KEY,
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
);*/

select * from tbCadastros