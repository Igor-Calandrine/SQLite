SELECT * FROM produtos;

SELECT estoque, "categoria" FROM produtos;
SELECT SUM(estoque), "categoria" FROM produtos GROUP BY "categoria";

-- Agora quem tem a mesma categoria será somado, quem tem a mesma categoria será contado
-- Lembrando que COUNT() em NULL sempre será 0

SELECT SUM(estoque) AS 'TOTAL ESTOQUE', "categoria", COUNT("categoria") AS 'TOTAL CATEGORIA' 
FROM produtos GROUP BY "categoria" ORDER BY SUM("estoque");

SELECT SUM(estoque) AS 'TOTAL ESTOQUE', "categoria", COUNT("categoria") AS 'TOTAL CATEGORIA' 
FROM produtos GROUP BY "categoria" 
ORDER BY COUNT("categoria");

------------------------------

SELECT "nome", "preco", "categoria" FROM produtos;

-- O preço médio será dado de quem tem a mesma categoria

SELECT "categoria", AVG("preco") FROM produtos GROUP BY "categoria";

SELECT "categoria", AVG("preco") AS 'preco médio' FROM produtos GROUP BY "categoria";

SELECT "categoria", ROUND(AVG("preco"), 2) AS 'preco médio' FROM produtos GROUP BY "categoria" 
ORDER BY AVG("preco") DESC;

-----------------------------

SELECT criado, categoria FROM produtos;

-- Os grupos serão dados por quem tem o mesmo ano e mês, depois contado no mesmo grupo;

SELECT "criado", COUNT("criado")AS 'TOTAL/ANO' FROM produtos GROUP BY STRFTIME('%Y%m' ,"criado");

SELECT "criado", COUNT("criado")AS 'TOTAL/ANO' FROM produtos GROUP BY STRFTIME('%Y%m' ,"criado")
ORDER BY STRFTIME('%Y%m' ,"criado") DESC;

----------------------------- 

SELECT MIN("preco"), categoria, nome FROM produtos;

-- Agora temo o menor preço por categoria 

SELECT MIN(preco), categoria FROM produtos GROUP BY categoria;

SELECT MIN(preco), categoria FROM produtos GROUP BY categoria
ORDER BY MIN(preco);


----------------------------- HAVING

SELECT SUM(estoque) AS 'TOTAL ESTOQUE', "categoria", COUNT("categoria") AS 'TOTAL CATEGORIA' 
FROM produtos 
GROUP BY "categoria" HAVING SUM(estoque) > 100
ORDER BY COUNT("categoria");

SELECT "categoria", AVG("preco") AS 'preco médio' FROM produtos 
GROUP BY "categoria" HAVING AVG("preco") < 20000
ORDER BY AVG("preco") DESC;

SELECT MIN(preco), categoria FROM produtos 
GROUP BY categoria HAVING MIN(preco) < 50000
ORDER BY MIN(preco);

