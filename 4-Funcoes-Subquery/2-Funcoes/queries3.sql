SELECT * FROM produtos;

SELECT categoria FROM produtos;
SELECT UPPER(categoria), * FROM produtos;
SELECT id, UPPER(nome), LOWER(categoria) FROM produtos;

SELECT LENGTH(nome) FROM produtos;
SELECT SUM(LENGTH(nome)) AS 'Total Letras' FROM produtos;
SELECT id, nome FROM produtos WHERE LENGTH(nome) < 14;

SELECT SUBSTR('notbook', 2, 2) FROM produtos;

INSERT INTO "produtos" ("nome","categoria","preco","taxa_importacao","estoque","lancamento","criado") VALUES
('            Fone Bluetooth       ','audio',19900,0,150,0,'2048-01-16 10:12:34');

INSERT INTO "produtos" ("nome","categoria","preco","taxa_importacao","estoque","lancamento","criado") VALUES
(TRIM('            Fone Bluetooth       '),'audio',19900,0,150,0,'2048-01-16 10:12:34');

SELECT  nome FROM produtos WHERE id = 24;
SELECT TRIM(nome) FROM produtos  WHERE id = 24;


