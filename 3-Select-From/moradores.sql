CREATE TABLE Moradores (
   "id" INTEGER NOT NULL,
   "Nome" TEXT NOT NULL,
   "idade" INTEGER NOT NULL,
   "altura" REAL
);

SELECT * FROM Moradores;

-- Comando inserido apenas para vizualização
INSERT INTO Moradores ("id", "Nome", "idade", "altura")
VALUES 
   (1, 'Igor', 20, 1.65),
   (2, 'Bianca', 19, 1.60),
   (3, 'Yuri', 19, 1.67);

SELECT * FROM Moradores;

SELECT "id" FROM Moradores;
SELECT "id", "Nome" FROM Moradores;
SELECT "Nome" FROM Moradores LIMIT 1;

-- DROP TABLE Moradores;