"""
-Trigger
   As Triggers permitem que uma ação seja executada automaticamente quando ocorre um determinado evento em uma tabela.
   É como que tudo seja feito no back-end, mas muitos sistemas de dados corporativos ainda às utilizam, o que torna algo importante de se conhecer.
   Os eventos possíveis são:
      
      *INSERT
      *UPDATE
      *DELETE

   Sua sintaxe é a seguinte:

*     CREATE TRIGGER nome_trigger
*     BEFORE | AFTER | INSTEAD OF
*     INSERT | UPDATE | DELETE
*     ON tabela
*     BEGIN
*        comandos SQL;
*     END;



   No exemplo abaixo criaremos um logo automaticamente após um novo dado for inserido. Note que temos um ponto e vírgula para o comando e o fim da trigger.

*     CREATE TRIGGER log_usuario
*     AFTER UPDATE OF coluna
*     ON users
*     BEGIN
*        INSERT INTO log(mensagens)
*        VALUES ('Novo usuário cadastrado');
*     END;
   

-Old New
   As palavras OLD e NEW são referências especiais utilizadas dentro de uma Trigger para acessar os valores de um registro antes ou depois de uma operação realizada no banco de dados.
   Elas não são tabelas reais nem variáveis criadas pelo desenvolvedor, são disponibilizadas automaticamente pelo SQLite enquanto a Trigger está sendo executada.

   A referência NEW representa os dados novos do registro, ela é utilizada quando uma linhas está sendo inserida (INSERT) ou após a alteraçao de seus valores (UPDATE). Por meio de NEW, é possível acessar qualquer coluna do registro utilizado a sintaxe NEW.nome_da_coluna. Dessa forma, a Trigger consegue trabalhar com os valores que estão sendo gravados no banco.

   A referência OLD representa os dados antigos do registro, ou seja, os valores existentes antes da operação. Ela está disponível nas operação UPDATE e DELETE, permitindo que a Trigger consulte o estado anterior do registro. Assim como NEW, o acesso aos dados é feita pela sintaxe OLD.nome_da_coluna.

   Durante uma operação de INSERT, apenas NEW está disponível, pois antes da inserção o registro ainda não existe. Em uma operação DELETE, ocorre o contrário, apenas o OLD pode ser utilizado, já que após a exlcusão não existe um novo registro para ser consultado. Já em uma operação de UPDATE, tanto OLD quanto NEW estão disponíveis simultaneamente, permitindo comparar os valores antes e depois da alteração.

   Essa possibilidade de acessar os dois estados de um mesmo registro torna as Triggers bastante úteis para registrar históricos de alterações, gerar auditorias, validar modificações e identificar exatamente quais informações foram alteradas em uma atualização.

   Imagine a seguinte tabela:

*      CREATE TABLE produtos (
*         id INTEGER PRIMARY KEY,
*         nome TEXT,
*         preco REAL
*      );

   Agora uma tabela logo para registrar alterações

*      CREATE TABLE log_precos (
*         id INTEGER PRIMARY KEY,
*         mensagem TEXT
*      );

   Vamos criar uma Trigger para registrar quando o preço de um produto for alterado

*     CREATE TRIGGER trg_alterar_preco
*     AFTER UPDATE OF preco
*     ON produtos
*        BEGIN
*           INSERT INTO log_precos(mensagem)
*           VALUES (
*           'O produto' || OLD.name || 'preco de' || OLD.preco || 'para' || NEW.preco
*           );
*        END;

-When e Update Of
   As cláusulas WHEN e UPDATE OF são recursos do SQLite que permitem controlar com mais precisão quando uma Trigger deve ser executada. Em vez de disparar a Trigger para toda operação de inserção, atualização, ou exclusão, essas cláusulas permitem restringir sua execução a situações específicas,, tornando o código mais eficiente e evitando ações desnecessárias.

   A cláusula WHEN funciona como uma condição lógica para a Trigger. Ela é avaliada no momento em que o evento ocorree, caso a expressão seja verdadeira, os comando definidos no bloco BEGIN...END são executados. Se a condição for falsa, a Trigger simplesmente não é executada. A condição pode utilizar operadores de comparação, operadores lógicos e os valores disponíveis por meio de OLD e NEW, permitindo verificar, por exemplo, se um estoque ficou abaixo de uma determinada quantidade, se um preço foi alterado ou se um determinado campo recebeu um vaor específico.

   Já cláusula UPDATE OF é utilizada exlcusivamente em Triggers de UPDATE e serve para indicar quais colunas devem provocar o disparo da Trigger. Sem essa cláusula, qualquer atualização realizada na tabela executará a Trigger, independentemente da coluna modificada.

   CREATE TRIGGER aviso_estoque
   AFTER UPDATE OF produtos(estoque)
   ON produtos
   WHEN NEW.estoque < 5
      BEGIN
         INSERTO INTO aviso(mensagens)
         VALUES ('O produto' || NEW.nome || 'está com estoque baixo');
      END;

-Drop Trigger
   O comando DROP TRIGGER é utilizado para remover uma Trigger existente do banco de dados SQLite. Após sua exclusão, a Trigger deixa de exxistir e não será mais executada quando ocorrer o evento o qual havia sido criada.

   A sintaxe é simples e consiste em informar o nome da Trigger que será removida. A partir da execução do comando, toda a definição da Trigger é apagada do banco de dados.

   A Remoção de uma Trigger não afeta a estrutura da tabela à qual ela estava associada, nem altera os dados já armazenados. Apenas o comportamento automático definido por ela deixa de existir.

   Em SQLite não existe o comando ALTER TRIGGER para modificar uma já criada. Sem´re que for necessário alterar sua lógica, adionar novas instruções ou corrigir algum erro, o procedimento consiste em remover a Trigger existente utilizando DROP TRIGGER e, em seguida, criar uma nova TRIGGER com a definição desejada.

   Caso exista a possibilidade de a Trigger não estar presente no banco de dados, pode-se utilizar a cláusula IF EXISTS, evitando que o SQLite gere um erro ai tentar excluir um Triggger inexistente.

*     DROP TRIGGER nome_da_trigger;
   
*     DROP TRIGGER IF EXISTS nome_da_trigger;

 ?Pelos meus objetivos de ir ao back-end ainda não acho que devo aprofundar nisso, melhor deixar o básico forte por enquanto e seguir em frente.

"""