"""
-Upsert
   o UPSERT é um recurso do SQLite que permite realizar uma operação de INSERT ou UPDATE em uma única instrução SQL. Seu objetivo é evitar erros de chave duplicada e seimplificar a lógica da aplicação.

   Em vez de verificar primeiro se um registro existe para depois decidir entre um INSERT ou um UDATE, o próprio SQLite faz essa verificação automaticamente. Tendo conflito ou não, ele insere um novo registro.

   O UPSET foi introduzido em 2018 e segue uma sintaxe semelhante à utilizada pelo PostgreSQL.
   Sua sintaxe é:

*   INSERT INTO tabela (...)
*   VALUES (...)
*   ON CONFLICT (coluna caso seja desejada)
*   DO ...

   O trecho ON CONLICT informa ao SQLite o que fazer caso existe uma violação de unicidade.

   *DO NOTHING
      A ação mais simples consiste em ignorar o conflito 

   *DO UPDATE
      A segunda possibilidade consiste em atualizar o registro existente mesmo tendo uma conflito. Esse é o comportamento normalmente associado ao termo UPSERT

- Excluded
   Quando ocorre um conflito, o SQLite cria uma tabela especial chamada EXCLUDED. Ela contém exatamente os valores que estavam sendo inseridos, não e um tabela física, portanto ela existe apenas durante a execução daquela instrução SQL.

   Durante o DO UPDATE, é possível acessar os valores novos descartados utilizando:

   *excluded.coluna

-Diferença entre USERT e INSERT OR REPLACE
   Embora sejam utilizados para lidar com conflitos de inserção do SQQLite, eles funcionam de maneiras bastante diferentes. À primeira vista, ambos parecem resolver o mesmo problema, evitar erros quando um registro com a mesma chave primária ou valor único já existe, porém o comportamento interno de cada um é distinto e pode gerar consequências importantes para a integridade dos dados.

   O UPSERT, utilizando a cláusula ON CONFLICT, tenta inserir um novo registro normalmente. Se não houver conflito, o registro é inserido. Caso ocorra uma violação de uma restrição PRIMARY KEY ou UNIQUE, o SQLite executa a ação definida pelo desenvolvedor, como DO NOTHING ou DO UPDATE. Quando a opção DO UPDATE é utilizada, o banco simplesmente modifica os valores da linha existente, preservando sua identidade. O rowid, a chave primária e todos os relacionamentos permanecem inalterados, tornando essa abordagem segura e previsível.

   Já o INSERT OR REPLACE não realiza uma atualização da linha existente. Quando ocorre um conflito, o SQLite primeiro remove o registro antigo e, em seguida, insere um novo registro com os valores informados. Na prática, trata-se de uma operação de DELETE seguido de INSERT, e não de um UPDATE. Embora o resultado visual seja semelhante, internamente o banco considera que um registro foi apagado e outro foi criado

   Essa diferença pode causar diversos efeitos colaterais. Como o registro original é excluído, seu rowid pode mudar, principalmente quando a chave primária não é um INTEGER PRIMARY KEY. Além disso, triggers de DELETE e INSERT podem ser executadas, o que não acontece em um UPSERT com DO UPDATE. Se houver tabelas relacionadas por chaves estrangeiras (FOREIGN KEY), a exclusão do registro pode provocar erros de integridade ou acionar ações como CASCADE, SET NULL ou RESTRICT, dependendo da configuração da tabela.

   Outro ponto importante é o desempenho. O UPSERT geralmente é mais eficiente porque modifica apenas os campos necessários da linha existente, evitando a exclusão e a recriação completa do registro. Já o INSERT OR REPLACE exige que o SQLite remova a linha antiga, atualize índices e grave um novo registro, realizando mais trabalho internamente.

   Por esses motivos, o UPSERT é considerado a abordagem moderna e recomendada para a maioria dos cenários. Ele preserva a identidade do registro, mantém os relacionamentos intactos, evita efeitos colaterais com triggers e chaves estrangeiras e torna a intenção da consulta mais clara. O INSERT OR REPLACE continua disponível e pode ser útil em situações específicas nas quais realmente se deseja substituir completamente um registro, mas deve ser utilizado com cautela, pois seu comportamento é muito diferente de uma simples atualização.
"""