CREATE TABLE funcionarios (
   "id" INTEGER NOT NULL,
   "nome" TEXT NOT NULL
) STRICT;

INSERT INTO funcionarios ("id", "nome") VALUES 
   (1, 'Igor'),
   (1, 'Bianca'),
   (2, 'Yuri');

SELECT "rowid", "id", "nome" FROM funcionarios;

CREATE TABLE valores (
   "id" INTEGER PRIMARY KEY,
   "valor" INTEGER
) STRICT;

INSERT INTO valores ("valor") VALUES
   (200),
   (500),
   (600);

SELECT * FROM valores;