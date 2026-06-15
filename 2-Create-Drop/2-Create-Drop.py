"""
-CREATE TABLE
   Criar uma tabela é um dos atos mais fundamentais ao trabalhar com banco de dados. É nesse momento que você define a estrutura que vai organizar seus dados. A sintaxe básica é:

*   CREATE TABLE nome_da_tabela (coluna1 TIPO RESTRIÇÕES, coluna1 TIPO RESTRIÇÕES, coluna1 TIPO RESTRIÇÕES);

-Tipo de Dados
   O SQLite funciona de forma diferente dos outros banco de dados. Ele usa uma sistema chamado tipagem dinâmica, o que significa que o tipo é um sugestão ao banco, não uma regra rígida. Ele se resume a 5 tipos de armazenamentos.

   *INTEGER
      Armazena números inteiros, positivos ou negativos, sem casas decimais

   *REAL
      Armazena números com casas decimais, usando ponto flutuante

   *TEXT
      Armazena qualquer texto, de qualquer tamanho

   *BLOB
      Armazena dados binários exatamente como foram inseridos, sem nanhuma conversão

   *NULL
      Representa a ausência de valor. Toda coluna pode conter NULL. Você pode restringir a possibilidade com NOT NULL


-DROP TABLE
   É um comando usado para deletar uma tabela completamente do banco de dados. Isso inclui a estrutura da tabela, todos os seus dados, índices e triggers associados a ela.
   !É uma operação permanente e irreversível, uma vez executada, não há como desfazer

*   DROP TABLE nome_da_tabela;

"""