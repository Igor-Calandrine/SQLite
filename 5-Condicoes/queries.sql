CREATE TABLE funcionarios (
   "id" INTEGER NOT NULL,
   "nome" TEXT NOT NULL,
   "cargo" TEXT NOT NULL,
   "salario" REAL NOT NULL
);

INSERT INTO funcionarios ("id", "nome", "cargo", "salario") VALUES 
(1, 'Igor', 'Desenvolvedor', 3000),
(2, 'Bianca', 'Desenvolvedor', 3000),
(3, 'Yuri', 'Professor', 4000),
(4, 'Ana', 'Professor', 5000);

SELECT * FROM funcionarios;

SELECT * FROM funcionarios WHERE "id" >=2;
SELECT * FROM funcionarios WHERE salario >= 3000 and "cargo" = 'Professor';
SELECT * FROM funcionarios WHERE salario >= 5000 or salario <= 3000;


