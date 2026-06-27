SELECT * FROM produtos;

SELECT COUNT(*) FROM produtos;

-- Os NULLs não irão contar dessa forma
SELECT COUNT(categoria) FROM produtos;
SELECT MAX(preco) FROM produtos;
SELECT MIN(PRECO) FROM produtos;

-- Assim pedimos as demais colunas
SELECT MAX(preco), * FROM produtos;
SELECT MIN(preco), id, nome FROM produtos;
SELECT MIN(criado), id, nome FROM produtos;

-- Podemos dar um nome com AS
SELECT id, nome, MIN(taxa_importacao) AS 'Menor Taxa' FROM produtos;

-- Para pegar todos os itens
SELECT id, nome, taxa_importacao AS 'Menor Taxa' FROM produtos
WHERE taxa_importacao = (SELECT MIN(taxa_importacao) FROM produtos);

SELECT ROUND(AVG(preco), 2) AS 'Preço Médio' FROM produtos;
SELECT ROUND(AVG(preco), 2) AS 'Preço Médio' FROM produtos
   WHERE nome LIKE 'Note%';

