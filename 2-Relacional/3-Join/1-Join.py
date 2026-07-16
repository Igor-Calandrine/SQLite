"""
-Join, Inner Join, (,)
   O JOIN permite combinar dados de duas ou mais tabelas com base em uam relação entre elas.
   Sem JOIN, um banco de dados relacional perderia uma de suas principais vantagens:
      
      *Manter os dados organizados em tabelas separadas e relaioná-los quando necessário

   Quando você escreve apenas JOIN, ele é interpretado como um INNER JOIN. Apenas a vírgula também pode ser usada, mas não recomendado o uso por questões de leitura.

   Observe as duas tabelas abaixo:

CLIENTES               PEDIDOS
_____________          ___________________________   
id   |   nome           id   | cliente_id  |  produto
1    |   João            1   |    1        |  Mouse
2    |   Maria           2   |    1        |  Teclado
3    |   Carlos          3   |    2        |  Monitor

Podemos identificar as tabelas com a seguinte sintaxe
?Não utilizei aspas duplas("") no nome das colunas por motivos didáticos, mas é o recomendado.

cliente.id             pedidos.id
cliente.nome           pedidos.cliente_id
                       pedidos.produto

   Agora observe que clientes.id e pedidos.cliente_id são uma dados relacionais, podemos utilizar o 
   JOIN para obter informações de ambas as tabelas

   *clientes.id = pedido.cliente_id

   Utilizando a seguinte sintaxe:

*      SELECT colunas FROM tabela1
*      JOIN tabela2
*      ON tabela1.coluna = taela2.coluna;

   No caso teremos

*      SELECT clientes.nome, pedidos.produto FROM clientes
*      JOIN pedidos
*      ON cliente.id = pedidos.cliente_id;

   Como resultado teremos o nome do cliente e o nome do produto pedido de quem tem o mesmo id. No caso Carlos ficará de fora, pois ele não realizaou pedidos.

   O ON informa qual coluna será usada para fazer a ligação.
   Podemos juntar várias tabelas dessa forma, mas a cada uma a busca será mais lenta, então é importante tomar cuidado com a eficiência.
   Caso as tabelas tenham o mesmo nome irá gerar um erro que facilmente pode ser resolvido com AS

-Left Join
   O LEFT JOIN é um tipo de junção que retorna todos os registros da tabela da esquerda, mesmo que não exista correspondência na tabela da direta.
   Quando não há correspondência, as colunas da tabela da direita são preenchidas com NULL
   
      *É um dos tipo de JOIN mais utilizados, principalmente para descobrir registros que não possuem relacionamento.

-Right Join
   O RIGHT JOIN é um tipo de junção utilizado para retornar todos os registros da tabela localizada à direita da junção, mesmo que não exista uma correspondência na tabela da esquerda.
   Quando não há correspondência, as colunas da tabela da esquerda são preenchidas com NULL

-Self Join
   O SELF JOIN é uma técnica em SQL na qual uma tabela é relacionada com ela mesma.
   Apesar do nome, não existe um comando chamado SELF JOIN. O que existe é um JOIN em que a mesma tabela aparece duas vezes com aliases diferentes.

   Assim por exemplo poderia filtrar da mesma tabela funcionários que tem o mesmo gerente

-Cross Join
   O CROSS JOIN é um tipo de junção utilizado para combinar todas as linhas de uma tabela com todas as linhas de outra tabela. Diferentemente do INNER JOIN, LEFT JOIN ou RIGHT JOIN, ele não utiliza uam condição de relacionamento (ON), pois seu objetivo é gerar as combinações possíveis entre os registros das tabelas envolvidas.
   
   Esse tipo de junção produz o chamado produto cartesiano, por ese motivo deve-se ter 
   
   !cuidado ao utilizá-lo em tabelas grandes,
   !pois a quantidade de registros pode crescer rapidamente.



"""