PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;

CREATE TABLE Usuarios (
   "id" INTEGER PRIMARY KEY,
   "nome" TEXT NOT NULL,
   "email" TEXT NOT NULL UNIQUE
   ) STRICT;

INSERT INTO Usuarios ("nome", "email") VALUES 
   ('Igor', 'email1@email.com'),
   ('Bianca', 'email2@email.com'),
   ('Yuri', 'email3@email.com'),
   ('Cristina', 'email4@email.com'),
   ('Mário', 'email5@email.com');

CREATE TABLE Produtos (
   "id" INTEGER PRIMARY KEY,
   "produto" TEXT NOT NULL,
   "email_comprador" TEXT NOT NULL,
   FOREIGN KEY ("email_comprador") REFERENCES Usuarios ("email")
      ON UPDATE CASCADE
   ) STRICT;

INSERT INTO Produtos ("produto", "email_comprador") VALUES
   ('abacaxi', 'email1@email.com'),
   ('pera', 'email2@email.com'),
   ('morango', 'email3@email.com'),
   ('morango', 'email4@email.com'),
   ('maça', 'email5@email.com'),
   ('maça', 'email5@email.com'),
   ('melao', 'email2@email.com');

SELECT * FROM Usuarios;
SELECT * FROM Produtos;

PRAGMA foreign_keys = ON;
DELETE FROM Usuarios WHERE "id" = 1;
DROP TABLE Usuarios;
DROP TABLE Produtos;
