"""
-Modo Estrito
   Para resolver o problema e aproximar o SQLite dos bancos de dados tradicionais, como PostgreSQL e MySQL, foi introduzido o suporte ao Modo Estrito.
   Ao criar uma tabela, você pode adicionar a palavra-chave STRICT no final da definião, isso muda completamente as regras do jogo.

   *Tipos Rígidos
      Você só pode usar os tipos de dados oficiais e o tipo genérico NUMERIC não é permitido da mesma forma flexível.

   *Validação Obrigatória
      O SQLite passa a validar o conteúdo, se você tentar inserir um texto que não pode ser convertido em uma coluna INTEGER, o SQLite rejeitará a inserção e retornará um erro.

   Agora teremos dois novo tipo de dados:

   *INT
      A maioria dos outros bancos de dados do mercado (como MySQL, PostgreSQL, SQL Server e Oracle) usa a palavra INT como padrão para números inteiros.
      Se você está escrevendo um códgo SQL que precisa rodar tanto no SQLite quanto em outros bancos de dados sem precisar alterar a sintaxe, usar INT facilita a portabilidade do seu código.
      Exite um caso específico para se usar INTEGER, o qual veremo a seguir.

   *ANY
      Garante que uma coluna possa receber e armazenar litaralmente qualquer tipo de dado sem tentar converter

   A sintaxe será:

*      CREATE TABLE nome_da_tabela (
*         coluna_1 INT NOT NULL,
*         coluna_2 TEXT NOT NULL 
*      ) STRICT;

"""