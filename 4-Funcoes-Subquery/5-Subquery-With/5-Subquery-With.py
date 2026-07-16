"""
-Subquery
   Uma Subquery, ou consulta aninhada, é uma consulta SQL escrita dentro de outra consulta. Ela permite utilizar o resultado de um SELECT como entrada para outro comando SQL.
   É um recurso que permite criar consultas inteligentes sem  precisar dividir o processamento em várias etapas. Ex:

      SELECT * FROM produtos 
      WHERE preco > (SELECT AVG(preco) FROM produtos);

      SELECT categoria, AVG(preco) FROM (SELECT * FROM produtos
      WHERE estoque > 0) GROUP BY categoria;

      SELECT nome, preco, (SELECT AVG(preco) FROM produtos) AS media FROM produtos;

      INSERT INTO produtos_caros 
      SELECT * FROM produtos 
      WHERE preco > (SELECT AVG(preco) FROM produtos);

      UPDATE produtos SET preco = preco * 1.10 
      WHERE categoria = (SELECT categoria FROM produtos WHERE id = 5);

-With As
   O comando WITH, também conhecido como Common Table Expression (CTE), permite criar uma tabela temporária nomeada que exite apenas durante a execução de uma consulta SQL.
   Em vez de escrever subconsultas grandes e difíceis de entender, você pode dividir a consulta em partes menores, mais organizadas e reutilizáveis. 
   
   ?São como funções na linguagem de programação, a diferença é que uma função pode ser chamada várias vezes em diferentes partes do programa, enquanto a CTE só existe durante a execução da instrução SQL em que foi definida.

      WITH produtos_caros AS 
      (SELECT * FROM produtos WHERE preco > 500)

      SELECT * FROM produtos_caros;

"""