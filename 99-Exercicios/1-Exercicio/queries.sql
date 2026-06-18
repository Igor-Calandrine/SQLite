CREATE TABLE produtos (
   "id" INTEGER NOT NULL,
   "nome" TEXT NOT NULL,
   "preço" REAL NOT NULL
);

CREATE TABLE clientes (
   "id" INTEGER NOT NULL,
   "nome" TEXT NOT NULL,
   "email" TEXT NOT NULL
);

CREATE TABLE compras (
   "cliente_id" INTEGER NOT NULL,
   "produto_id" INTEGER NOT NULL,
   "data" TEXT NOT NULL
);

INSERT INTO produtos ("id", "nome", "preço") VALUES
   (1, 'Notebook', 1000),
   (2, 'Smartphone', 500),
   (3, 'Tablet', 300);

INSERT INTO clientes ("id", "nome", "email") VALUES 
   (1, 'Maria', 'maria@email.com'),
   (2, 'João', 'joao@email.com');

INSERT INTO compras ("cliente_id", "produto_id", "data") VALUES
   (1, 23, '2049-01-01'),
   (2, 30, '2049-01-02'),
   (1, 50, '2049-01-03');

SELECT * FROM produtos;
SELECT * FROM clientes;
SELECT * FROM compras;

SELECT "nome" FROM produtos WHERE "preço" > 400;
SELECT "produto_id" FROM compras WHERE "cliente_id" = 1;