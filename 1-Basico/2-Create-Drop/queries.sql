-- Criando Tabela Cursos
CREATE TABLE Cursos (
   "id" INTEGER NOT NULL, 
   "Nome" TEXT NOT NULL, 
   "aula" INTEGER NOT NULL
);

CREATE TABLE Moradores (
   "id" INTEGER NOT NULL,
   "Nomes" TEXT NOT NULL,
   "sexo" TEXT,
   "altura" REAL);

-- Dados inserido apenas para vizualização
INSERT INTO  Cursos(id, Nome, aula) 
VALUES (1, 'Igor', 0);
-- 

ALTER TABLE Cursos
RENAME TO Cursos1;

ALTER TABLE Cursos1
RENAME COLUMN 'Nome' TO 'Nome1';

ALTER TABLE Cursos1
ADD COLUMN 'email' TEXT;

ALTER TABLE Cursos1
DROP COLUMN 'email';

SELECT *  FROM Cursos1;

DROP TABLE Cursos;
DROP TABLE Moradores;