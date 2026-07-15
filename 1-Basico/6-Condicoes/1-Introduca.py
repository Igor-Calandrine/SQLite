"""
-Condiçoes
   Para refinar suas consultas com o SELECT ou direcionar o seu DELETE, você precisa dominar as condiçoes, é aqui que entra o WHERE acompanhado dos operadores lógicos AND e OR.

   *WHERE
   Estabelece uma condição inicial, o SQLite analisa linhas por linhas da tabela e só devolve aquelas que correspondem a "verdadeiro" para a sua condição. Ex:

      SELECT nome, cargo FROM funcionarios WHERE cargo = 'Gerente';

   *AND
   Ele serve para juntar duas ou mais condições, e o registro só será exibido se passar em todas elas ao mesmo tempo. Se apenas uma das condições for falsa, a linhas será descartada. Ex:

      SELECT nome, salario FROM funcionarios
      WHERE cargo = 'Gerente'
      AND salario > 5000;

   *OR
   Ele serve para trazer registros que atendam a pelo menos uma das condições. Se qualquer uma das condições for verdadeira ele traz uma resposta. Ex:

      SELECT nome, departamento FROM funcionarios
      WHERE departamento = 'vendas'
      OR departamento = 'Marketing';

-Misturas
   Quando você começa a misturar AND e OR NA mesma frase, o SQLite pode se confundir com a ordem de leitura, ele dá prioridade para o AND. Para evitar resultados errados, nós usamos parênteses para isolar o que deve ser testado junto.

   No exemplo abaixo podemos ter um possível erro de interpretação. O SQLite vai entender:
   "Traga todo mundo de Marketing que ganha mais de 3000, mais qualquer pessa de Vendas (independente do salário)

*     SELECT nome FROM funcionarios
*     WHERE departamento = 'Vendas' OR departamento = 'Marketing'
*     AND salario > 3000;

   Para corrigir o erro devemos usar parênteses para dar prioridade. O SQLite primeiro junta os dois departamentos, e depois aplica o filtro de salário para ambos.

*     SELECT nome FROM funcionarios
*     WHERE (departamento = 'Vendas' OR departamento = 'Marketing')
*     AND salario > 3000;







"""