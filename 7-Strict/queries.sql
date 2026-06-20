CREATE TABLE papelaria (
   id INTEGER NOT NULL,
   nome TEXT NOT NULL,
   qntd INTEGER NOT NULL,
   valor INTEGER NOT NULL
) STRICT;

INSERT INTO papelaria ("id", "nome", "qntd", "valor") VALUES
   ('1', 'papel', '10', '300'),
   (2, 'borracha', 5, 200);

SELECT * FROM papelaria;
SELECT typeof(id) FROM papelaria;

