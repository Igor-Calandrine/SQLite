"""
-Group By
   É um dos comandos mais importantes do SQLite, ele é utilizado para agrupar registros que possuem o mesmo valor em uma ou mais colunas, sendo normalmente combinado com funções de agregação como COUNT(), SUM(), AVG(), MIN() E MAX()

   A GROUP BY é frequentemente utilizado em relatórios, estatísticos e consultas analíticas, permitindo resumir grandes quantidades de dados de forma organizada.
   A sintaxe básica é:

*      SELECT coluna, função_agregação(coluna) FROM tabela 
*      GROUP BY coluna;

-Order By
   É utilizada para ordenar os resultados de uma cosulta. Por padrão, o SQLite retorna os registros na ordem em que eles estão armazenados, o que nem sempre é a ordem desejada. Com o ORDER BY, é possível organizar os dados em ordem crescente, decrescente ou por múltiplas colunas.
   Temos:

      *ASC 
         Padrão de comportamento, ordena em sentido crescente

      *DESC
         Ordena em sentido decrescente

   Temos como sintaxe:

*      SELECT * FROM produtos ORDER BY nome;
*      SELECT * FROM produtos ORDER BY nome ASC;
   ou
*      SELECT * FROM produtos ORDER BY nome DESC;

"""