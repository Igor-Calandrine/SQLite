PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;

CREATE TABLE Funcionarios (
   "id" INTEGER PRIMARY KEY,
   "nome" TEXT NOT NULL COLLATE NOCASE,
   "idade" INTEGER NOT NULL CHECK("idade" >= 18),
   "email" TEXT NOT NULL UNIQUE COLLATE NOCASE,
   "salario" REAL NOT NULL CHECK("salario" > 0),
   "endereço" TEXT DEFAULT 'Brasil',
   "registro" TEXT DEFAULT CURRENT_TIMESTAMP,
   "departamento" TEXT NOT NULL CHECK("departamento" IN ('Vendas', 'TI', 'RH'))
) STRICT;

CREATE TABLE RH (
   "id_RH" INTEGER PRIMARY KEY,
   "nome" TEXT NOT NULL COLLATE NOCASE,
   FOREIGN KEY ("nome") REFERENCES Funcionarios ("nome")
      ON UPDATE CASCADE
) STRICT;

INSERT INTO Funcionarios ("nome", "idade", "email", "salario", "departamento")
VALUES
   ('Igor', 20, 'email1@email.com', 2000, 'TI'),
   ('Bianca', 20, 'email2@email.com', 3000, 'RH'),
   ('Yuri', 22, 'email3@email.com', 3000, 'Vendas'),
   ('Ana', 25, 'email4@email.com', 3000, 'RH');

INSERT INTO Funcionarios ("nome", "idade", "email", "salario", "departamento")
VALUES
   ('Igor', 20, 'Email1@email.com', 2000, 'TI');

INSERT INTO RH ("nome") 
VALUES
   ('Bianca'),
   ('Ana');

SELECT * FROM Funcionarios;
PRAGMA foreign_keys = ON;
SELECT * FROM RH;

PRAGMA foreign_keys = ON;
DELETE FROM Funcionarios;


