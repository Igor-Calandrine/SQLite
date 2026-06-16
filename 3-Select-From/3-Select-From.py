"""
-Select
   É o comando mais utilizado em toda a linguagem, a sua função é buscar e exibir informações que já estão salva dentro de uma tabela. 
   Para entender de forma simples, o SELECT é equivalente a você abrir uma planilha apenas para olhar o que está escrito nela.

   O SELECT é um comando de pura leitura, ele nunca cria tabelas, nunca apaga dados e nunca altera nada do que está gardado. Ele apenas "imprime" na sua tela o que você pediu para ver.

-From
   É um comando que serve para especificar a tabela de origem de onde as informações serão puxadas. Como um banco de dados pode ter dezenas ou centenas de tabelas diferentes, o SQLite precisa que você aponte para exatamente deseja.

-Asterisco (*)
   Irá indicar apenas "todas as colunas..." 

-Estrutura de Sintaxe
   Para ler os dados de uma tabela, nós iremos escrever a seguinte sintaxe:

*     SELECT * FROM nome_da_tabela;

-Pugins
   Há vários plugins para vizualizar uma tabela, eles serão usados para facilitar o trabalho, o comando será utilizado para os seguintes capítulos com diferentes objetivos.

   Para servir de exemplo, foi inserido o comando que iremos ver no capítulo a frente:

*     INSERT INTO Moradores (id, Nome, idade, altura) VALUES (1, 'Igor', 20, 1.65);

   E depois o comando para vizualizar a tabela, assim temos um exemplo didático e vizual.
"""