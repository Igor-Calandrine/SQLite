"""
-JSON
   Apenas para revisar antes de começar, JSON é um formato de texto utilizado para armazenar e trocar dados estruturados:
   *Objetos
   {
      "nome": "Igor,
      "idade": 30,
      "cidade": "Belém"
   }

   *Array
   {
      "cursos: [
         "HTML",
         "CSS",
         "JavaScript"
      ]
   }

   O SQLite não possui um tipo de dado JSON, diferentemente de alguns bancos de dados.

   !Não existe
   CREATE TABLE usuarios (dados JSON);

-json_valid()
   A função json_valid() é utilizada para verificar se um texto armazenado no banco de dados representa um documento JSON válido. Como o SQLite não possui um tipo de dado específico para JSON e armazena esses documentos como TEXT, essa função é importante para garantir que os ados estejam corretamente formatados antes de serem utilizados pelas demais funções da extensão JSON.

   Afunção é especialmente útil antes de inserir ou atualozar informações em uma tabela. Dessa forma, é possível impedir que documentos malformados sejam armazenados no banco de dados.

   Onde json é o texto que será analisado. A função retorna 1 quando o conteúdo é válido e 0 quando há erros de sentaxe ou não segue o padrão JSON.

   Ex:

*   SELECT json_valid('{"nome":"Igor","idade":30}')
   Resultado: 1

*   SELECT json_valid('{nome:"Igor","idade":30}')
   Resultado: 0

   Podemos realizar uma consulta para retornar registros cuja seu registro JSON é inválido.

*   SELECT * FROM usuarios
*   WHERE json_valid(dados) = 0

-josn()
   A função é utilizada para interpretar um valor como um documento JSON. Sua principal finalidade é validar o conteúdo informado e retroná-lo em uma representação JSON padronizada. Caso o valor fornecido não seja um JSON válido, a função interrompe a execução da consulta e retorna um erro. 

   Afunção também normaliza sua repreeentação, isso significa que espaços em branco, quebras de linha e indentação são removidos, retornando um JSON compacto, mas mantendo exatamente os mesmos dados.
   Sua sintaxe é:

*   SELECT json('{"nome": "Igor","idade": 30}');

-json_extract()
   A função é utilizada para extrair valores específicos de um documento JSON. Ela permite acessar informações armazenadas em objetos e arrays utilizando um caminho, sem a necessidade de converter o JSON para uma tabela ou processá-lo em uma plicação externa.

   -Objetos
   Por exemplo considere o JSON do ínicio onde temos objetos, na sintaxe teríamos:

*  SELECT json_extract('{"nome":"Igor", "idade":30}', '$.nome')
   Resultado: Igor

*  SELECT json_extract('{"nome":"Igor", "idade":30}', '$.idade')
   Resultado: 30

   Caso tenhamos um objeto dentro de outro objeto, basta passar o caminho, como o exemplo:
   $.usuario.nome

   -Arrays
   Para acessar um elemento de uma Array podemos utilizar seus índices.
   Por exemplo considere o JSON do ínicio onde temos uma lista, na sintaxe teríamos:

*  SELECT json_extract('{"cursos":["HTML", "CSS", "JavaScript"]}', '$.cursos[1]');
   Resultado: CSS

   -Conultando
   Através das funções acima é possível consultar apenas um requerido dado

*  SELECT json_extract("dados", '$.idade') FROM usuarios;

-Operadores -> e ->>
   Esses operadores foram introduzidos para tornar as consultas mais curtas e legíveis, sendo uma alternativa prática à utilização de json_extract() em situações simples.

   *->
   Extrai um valor do documento JSON e o retorna com um valor JSON. Isso significa que objetos e arrays continuam sendo retornados em formato JSON e, quando o resultado é uma string, ela permanece representada como uma string JSON.

*  SELECT '{"cursos":["HTML", "CSS", "JavaScript"]}' -> '$.cursos[1]';

*  SELECT '{"usuario":["nome": "Maria, "idade": 25]}' -> '$.usuario';

   *->>
   O Operador também extrai um valor do documento JSON, porém retorna o resultado convertido para um valor SQL. Isso significa que as aspas das strings são removidas e os valores podem ser utilizados diretamente em comparações, filtros e operações do banco de dados.

*  SELECT '{"nome":"Igor", "idade":30}', '$.nome' ->> '$.idade';
   Nesse caso, o valor é retornado como um número SQL

   ?Na prática, quando o objetivo é obter um valor simples, como um nome, idade ou preço, o operador ->> costuma ser a opção mais conveniente. Já quando se deseja obter um objeto JSON completo ou um array para continuar manipulando sua estrutura, o operador -> é a escolha mais adequada.

"""