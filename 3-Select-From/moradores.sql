CREATE TABLE Moradores (
   id INTEGER NOT NULL,
   Nome TEXT NOT NULL,
   idade INTEGER NOT NULL,
   altura REAL);



SELECT * FROM Moradores;

INSERT INTO Moradores (id, Nome, idade, altura) VALUES (1, 'Igor', 20, 1.65);

SELECT * FROM Moradores;

-- DROP TABLE Moradores;