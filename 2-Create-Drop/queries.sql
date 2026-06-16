-- Criando Tabela Cursos
CREATE TABLE Cursos (
   "id" INTEGER NOT NULL, 
   "Nome" TEXT NOT NULL, 
   "aula" INTEGER NOT NULL);

CREATE TABLE Moradores (
   "id" INTEGER NOT NULL,
   "Nomes" TEXT NOT NULL,
   "sexo" TEXT,
   "altura" REAL);

DROP TABLE Cursos;
DROP TABLE Moradores;