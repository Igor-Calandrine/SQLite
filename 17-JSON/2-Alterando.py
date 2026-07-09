"""
Alterando Dados JSON
   O SQLite oferece diversas funções para modificar documentos JSON armazenados no banco de dados. Todas elas retornam um novo documento JSON contendo as alterações realizadas, já que os valores JSON são imutáveis.
   As principais funções são:

   *json_set()
   Altera o valor de uma chave caso ela já exista ou cria essa chave caso ela ainda não esteja presente no documento.

*     UPDATE "users_config"
*     SET "config" = json_set("config", '$.font', 'helvetica')
*     WHERE "user_id" = 1;

   *json_insert
   A função json_insert() adiciona uma nova chave somente quando lea ainda não existe. Caso o caminho informado já esteja presente do documento, nenhuma alteração é realizada.

*     UPDATE "users_config"
*     SET "config" = json_insert("config", '$.ads', 0)
*     WHERE "user_id" = 1;

   *json_remove()
   A função json_remove() elimina um ou mais elementos de um documento JSON

*     UPDATE "users_config"
*     SET "config" = json_remove("config", '$.ads')
*     WHERE "user_id" = 1;

-Colunas Geradas
   Uma das formas mais eficiente de trabalhar com documentos JSON no SQLite é utilizando colunas geradas. Esse recurso permite criar colunas cujo valor é calculado automaticamente a partir de um documento JSON, facilitando consultas, ordenações e criação de índices.

   Considere a seguinte tabela:

*   CREATE TABLE usuarios (
*      id INTEGER PRIMARY KEY,
*      dados TEXT
*   );

   Suponha que a colunas dados contenha o seguinte documento JSON

   { 
      "nome": "Maria", 
      "idade": 28, 
      "cidade": "São Paulo" ]
   }   

   Para consultar o nome seria necessário:

*   SELECT json_extract(dados, '$.nome') FROM usuarios;

   Podemos criar uma nova tabela para automaticamente extrair os dados e formar um coluna do JSON

*   CREATE TABLE usuarios (
*      id INTEGER PRIMARY KEY,
*      dados TEXT
*      nome TEXT GERERATED ALWAYS AS (json_extract(dados, '$.nome')) VIRTUAL
*   );

   Após o registro for inserido facilmente podemos acessar através de:

*   SELECT nome FROM usuarios;

   Podemos também, como já foi visto, alterar uma tabela

*   ALTER TABLE usuarios
*   ADD COLUMN "nome" TEXT AS (dados ->> '$.nome')
"""