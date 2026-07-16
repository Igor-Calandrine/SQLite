-- SELECT GERAL
SELECT * FROM produtos;
SELECT id, nome, estoque FROM produtos;

-- WHERE
SELECT id FROM produtos WHERE id > 10;
SELECT estoque FROM produtos WHERE estoque < 100;
SELECT id, nome, criado FROM produtos WHERE criado > '2049-07';

-- IS/IS NOT
SELECT id, nome, categoria FROM produtos WHERE categoria IS NULL;

-- LIKE
SELECT id, nome FROM produtos WHERE nome LIKE 'mouse%';
SELECT id, nome, estoque FROM produtos WHERE nome LIKE 'process%';
SELECT id, nome, preco FROM produtos WHERE nome LIKE 'pla__%';

-- BETWEEN
SELECT id, nome, preco FROM produtos WHERE preco BETWEEN 8000 AND 20000;
SELECT id, nome, taxa_importacao FROM produtos WHERE taxa_importacao BETWEEN 500 AND 5000;
SELECT id, nome, criado FROM produtos WHERE criado BETWEEN '2048-05' AND '2049-09';

-- IN/NOT IN
SELECT id, nome, categoria FROM produtos WHERE categoria IN ('audio', 'acessorio');
SELECT id, nome, categoria FROM produtos WHERE categoria IN ('periferico', 'hardware');







