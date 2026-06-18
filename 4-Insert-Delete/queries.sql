CREATE TABLE Moradores (
   "id" INTEGER NOT NULL,
   "nome" TEXT NOT NULL,
   "altura" REAL NOT NULL);

INSERT INTO Moradores ("id", "nome", "altura") VALUES 
(1, "Igor Guimarães", 1.65),
(2, "Bianca Rosshard", 1.60),
(3, "Ana Cristina", 1.55);

DELETE FROM Moradores WHERE id = 2;

SELECT * FROM Moradores;

