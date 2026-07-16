"""
-Performance
   A performance no SQL refere-se à capacidade de um banco de dados executar consultas de forma rápida e eficiente, utilizando o mínimo possível de recursos computacionais, como processamento, memória e acesso ao disco. À medida que a quantidade de dados armazenados cresce, a preocupação com o desempenho torna-se essencial para garantir que as aplicações continuem respondendo de maneira satisfatória aos usuários.

   Em banco de dados pequenos, uma consulta pode parecer rápida mesmo que não tenha sido escrita da melhor forma. No entanto, quando uma tabela passa de centenas para milhares ou milhões de registros, consultas mal otimizadas podem levar segundos ou até minutos para serem executadas, comprometendo a experiência do susário e aumentando o consumo de recursos do servidor.

   Imagine a seguinte consulta:

*   SELECT * FROM users WHERE email = 'igoraraujo@email.com'

   Se a tabela possuir apenas 100 registros provavelmente a consulta será executada rapidamente, mesmo sem um índice.

   Entretando, se a mesma tabela crescer para 10 milhões de registros, o banco poderá precisar verificar cada linhas até encontrar o e-mail desejado, tornando a consulta muito lenta.
   Esse é um exemplo de como uma consulta aparentemente simples pode sofrer degradação de desempenho conforme o banco cresce.

-Explain Query Plan
   O EXPLAIN QUERY PLAN é um comando do SQLite utilizado para exibir o plano de execução de uam consulta SQL. Em vez de executar a consulta e retornar seus resultados, ele informa como o banco de dados pretende executá-la, indicando quais tabelas serão ecessadas, se haverá varreduras completas (table scans), utilização de índices, junções e outras operações.

   Esse comando é uma das principais ferramentas para análise e otimização de desempenho, pois permite identificar consultas ineficientes e verificar se os índices criados estão sendo utilizados pelo mecanismo do banco de dados.

   Na sixtaxe basta adicionar da seguinte forma:

*   EXPLAIN QUERY PLAN
*   SELECT * FROM users
*   WHERE email = 'igoraraujo@email.com'

   As duas palavras mais importante que aparecem no plano de execução são:

   *SCAN
      Significa que o SQLite está realizando uma verredura completa da tabela (Full Table Scan).Ocorre caso não exista um índice sobre a coluna pedida no Select realizado
   
   *SEARCH
      Nesse caso o SQLite utiliza o índice para localizar os registros diretamente, evitando percorrer toda a tabela. Essa abordagem reduz significativamente o tempo necessário para executar a consulta.

-Indices
   Os índices são um dos principais recusos utilizados pelso bancos de dados para melhorar o desempenho das conultas. Eles permitem que o SQLite localize registros de forma muito mais rápida, reduzindo a quantidadde de dados que precisam ser analisados durante a execução de uma consulta.

   Sem índices, o banco de dados frequentemente precisa percorrer todas as linhas de uma tabela para encontrar os registros desejados. À medida que a quantidade de dados aumenta, esse processo torna-se cada vez mais lento. Com índices adequados, o SQLite pode acessar diretamente os registros procurados, tornando as conultas muito mais eficientes.

   -Funcionamento de Indices
      Sem um índice, para encontrar um assunto específico seria necessário em um livro ler página por página até localizar a informação desejada.

      Com um índice, basta consultar a lista de tópicos, descobrir a página correspondente e ir diretamente ao conteúdo. Da mesma forma, o SQLite utiliza índices para localizar registors sem precisar analisar toda a tabela.

      Internamente, os índices do SQLite são armazenados principalmente em estruturas do tipo B-tree (Balanced Tree), que organizam os dados de forma ordenada e permitem buscas muito mais rápidas.

   -Indices tem Custos
      Embora os índices acelerem as consultas de leitura, eles também possuem um custo. Sempre que um registro é inserido, atualizado ou removido, o SQLite precisa atualizar todos os índices relacionados à tabela.

      Por isso:
*      INSERT, UPDATE, DELETE podem ficar um pouco mais lentos

      Além idsso, cada índice ocupa espaço adicional em disco. Dessa forma, criar índices em excesso pode aumentar o consumo de armazenamennto e reduzir o desempenho das operações de escrita.
      Um índice é recomendado quando:

      * A coluna é utilizada frequentemente em cláusulas WHERE
      *Participa de relacionamentos JOIN
      *Acoluna é utilizada em ORDER BY, GROUP BY

-Criando um Índice
   Uma das principais formas de otimizar consultas em um banco de dados é a criação de índices. A sintaxe é a seguinte:

*     CREATE INDEX nome_do_indice
*     ON nome_da_tabela(coluna);

   Para apagar basta:

*      DROP INDEX nome_do_indice;
   
   Supondo o exemplo acima de busca por email sem índice, agora iremos criar:

*      CREATE INDEX email_id
*      ON users(email);

   Uma característica importante é que sua criação ocorre internamente no banco de dados. Quando um índice é criado, o SQLite não adiciona uma nova coluna à tabela, nem altera sua estrutura visível. Em vez disso, ele cria uma estrutura auxiliar separada, utilizada exclusivamente para otimizar a localização dos registros.

   

   
"""