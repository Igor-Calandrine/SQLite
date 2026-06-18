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
"""