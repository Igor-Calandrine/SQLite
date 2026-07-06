CREATE TABLE Moradores (
   "id" INTEGER NOT NULL,
   "nome" TEXT NOT NULL,
   "sobrenome" TEXT NOT NULL,
   "nome_completo" TEXT 
      GENERATED ALWAYS AS ("nome" || ' ' || "sobrenome") STORED,
   "altura" REAL NOT NULL
);

INSERT INTO Moradores ("id", "nome", "sobrenome", "altura") VALUES 
(1, 'Igor', 'Guimarães', 1.65),
(2, 'Bianca', 'Rosshard', 1.60),
(3, 'Ana Cristina', 'Guimarães', 1.55);

DELETE FROM Moradores WHERE id = 2;

SELECT * FROM Moradores;
-- DROP TABLE Moradores;

