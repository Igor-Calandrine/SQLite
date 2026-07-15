"""
-Alter Table
   O ALTER TABLE é o comando utilizado para modificar a estrutura de uma tabela existente, sem precisar apagá-la e criá-la novamente. Nas versões atuais do SQLite, ele permite:
      
      *Renomear uma tabela
      *Renomear uma coluna
      *Adicionar uma coluna
      *Remover uma coluna
   
   !Ele não permite:
      Alterar diretamente o tipo de uma coluna
      Alterar uma chave primária existente
      Adicionar uma restrição a uma coluna já criada
      Alterar a posição de uma coluna

   Para esses casos, normalmente é necessário criar uma nova tabela, copiar os dados e substituir a antiga.

   Sua sintaxe é:

*   ALTER TABLE tabela_antiga
*   RENAME TO tabela_nova;

*   ALTER TABLE tabela
*   RENAME COLUMN coluna_antiga TO coluna_nova;

*   ALTER TABLE tabela
*   ADD COLUMN coluna tipo;

*   ALTER TABLE tabela
*   DROP column tipo;

   Ao remover uma colunas, o SQLite recria a tabela internamente, copia os dados restantes e substitui a tabela antiga. Por isso, essa operação pode ser muais demorada em tabelas grandes.




"""