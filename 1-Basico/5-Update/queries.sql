CREATE TABLE produtos (
   "id" INTEGER NOT NULL,
   "nome" TEXT NOT NULL,
   "quantidade" INTEGER NOT NULL,
   "preço" REAL NOT NULL,
   "total" REAL 
      ALWAYS GENERATED AS ("preço" * "quantidade") VIRTUAL
);

INSERT INTO produtos ("id", "nome", "quantidade", "preço") VALUES
(1, 'banana', 10, 5.50),
(2, 'pera', 5, 8.50),
(3, 'uva', 8, 3.50),
(4, 'maça', 3, 2.50),
(5, 'abacaxi', 15, 9),
(6, 'couve', 20, 10);

UPDATE produtos SET "preço" = 2 WHERE "nome" = 'couve';
UPDATE produtos SET "quantidade" = 35 WHERE "id" = 5;

SELECT * FROM produtos;
SELECT "nome", "preço" FROM produtos;

DROP TABLE produtos;


