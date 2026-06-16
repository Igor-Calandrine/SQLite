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

-Palavras reservadas
   Existem palavras que pertencem à própria linguagem em que servem para dar ordens ao sistema, essas palavras são chamadas de Palavras Reservadas, como: CREATE, DROP, TABLE, SELECTED, WHERE.
   O problema surge quado você quer dar o nome de uma coluna ou de uma tabela usando uma dessas palavras, para resolver esse conflite e avisar ao banco de dados que aquilo é apenas o nome de uma couna (um identificador) e não um comando, nós usamos o recurso de delimitação por aspas.

   No SQLite, a forma padrão e mais recomendada pela linguagem para envolver nomes de tabelas ou colunas é o uso de aspas duplas (" ")

-Textos
   Sempre que você quiser inserir, atualizar ou pesquisar uma informação que seja composta por letras, palavras ou frases, você deve envolver esse conteúdo com aspas simples. Elas avisam ao SQLite onde o seu texto começa e onde ele termina.

"""