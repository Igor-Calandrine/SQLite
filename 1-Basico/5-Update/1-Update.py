"""
-Update
   O UPDATE é o comando que usamos para modificar ou atualizar dados que já estão salvos dentro de uma tabela. Para que ele funcione, ele sempre trabalha em dupla com a cláusula SET, que define o objeto. 
   
   *Update
      Diz ao banco de dados qual a tabela será modificada
   *Set
      Diz o nome da coluna que quer mudar
   *Where
      Diz exatamente a linhas, ou linhas que deve receber o novo valor
   Ex:

*     UPDATE nome_da_tabela
*     SET coluna1 = novo_valor1, coluna2 = novo_valor2
*     WHERE condição;

   !Assim como no DELETE, nunca esqueça o WHERE no seu comando UPDATE, se não ele vai rodar todos os usuários da sua tabela no SET para o novo valor.Ex:

!     UPDATE usuarios SET status = 'inativo'

   !Todos os usuários teriam o status de 'inativo'

-Returning
   A cláusula é um recutso do SQLite que permite retornar informações sobre as linhas afetadas por uma instrução de modificcação de dados, como 
      
      *INSERT
      *UPDATE
      *DELETE
   
   Em vez de executar uma consulta adicional para descobrir quais valores foram inseridos, atualizados ou removidos, o próprio comando pode devolver essas informações imediatamente aós sua execução.

   O recurso foi introduzido em 2021, e tornou o banco de dados mais prático para plicações que precisam manipular registros e obter seus dados na mesma operação.

   O RETURNING é um dos recursos mais úteis das versões modernas do SQLite. Ele simplifica o desenvolvimento, reduz a quantidade de consultas ao banco e torna as operações de inserção, atualização e exclusão mais eficientes, permitindo que a aplicação obtenha imediatamente as informações dos registros modificados em uma única instrução SQL.

   Sua sintaxe é:

*   INSERT INTO tabela (...colunas)
*   VALUES (...valores)
*   RETURNING colunas...;

*   UPDATE tabela
*   SET coluna = valor
*   WHERE condição
*   RETURNING ...colunas;

   Basta adicionar no final quais colunas são desejadas.


"""