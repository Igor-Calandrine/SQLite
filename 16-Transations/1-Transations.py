"""
-Transations
   Elas garantem que um conjunto de operações sejam executados de forma segura e consistente. Em vez de gravar cada comando imediatamente no banco de dados, o SQLite pode agrupar várias operações em uma única unidade de trabalho.

   Uma transação segue o princípio conhecido como ACID, que garante confiabilidade mesmo em caso de falhas.
   Imagine aseguinte operação:

*   UPDATE contas
*   SET saldo = saldo - 200
*   WHERE id = 1;

*   UPDATE contas
*   SET saldo = saldo + 200
*   WHERE id = 2;

   Se ocorrer um erro entre duas instruções, João perderá R$200 e Maria não receberá o dinheiro.
   É exatamente esse tipo de problema que uma transação evita.

-Estrutura
   Uma trasação possui 3 comandos principais:

   BEGIN TRANSATION; (TRANSATION pode ser subtraido)

   --comandos SQL

   COMMIT;


No caso acimas teremos

*   BEGIN TRANSATION;
*     UPDATE contas
*     SET saldo = saldo - 200
*     WHERE id = 1;

*     UPDATE contas
*     SET saldo = saldo + 200
*     WHERE id = 2;
*   COMMIT;

   Somente após o COMMIT as alterações tornam-se permanentes.

-Rollback
   É um comando de retorno, que pode ser utilizado para desfazer todas as alterações feitas e retornar ao estado anterior

*   BEGIN TRANSATION;
*     UPDATE contas
*     SET saldo = saldo - 200
*     WHERE id = 1;

*   ROLLBACK;

- Quando usar
   Sempre que houver mais de uma operação que deve ser tratada como uma única unidade lógica, por exemplo:
      *Transferências bancárias.
      *Cadastro de um pedido com seus itens.
      *Atualização de estoque e registro de venda.
      *Importação de milhares de registros.
      *Migração de dados.
      *Execução de vários INSERT, UPDATE ou DELETE relacionados.

"""