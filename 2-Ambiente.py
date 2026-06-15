"""
-Criando
   Antes de começar a escrever comandos SQL, é importante entender como o ambiente de trabalho funciona  no VSCode. Diferente de linguagens de programação onde você simplesmente aperta um botão e o código roda, no SQLite existe uma seoeração clara entre onde você escreve e onde os dados vivem.

   *.sql
      É o arquivo onde você escreve todos os seus comandos, criação de tabelas, inserção de dados, consultas e tudo mais. Pense nele como um bloco de notas inteligente, onde você planeja organizar o que quer fazer com o banco de dados.

   *.db
      É o banco de dados em si, onde tudo o que você executar ficará salvo de forma permanente.

   O primeiro passo é criar o arquivo .sql no seu projeto, e em seguida é necessário criar o banco de dados corretamente, e aqui temos um ponto importante.
      !O arquivo .db não pode ser criado manualmente clicando em "Novo Arquivo" no VSCode
   Pois isso geraria um arquivo de texto comum que o SQLite não reconheceria, ele precisa ser criado pelo próprio SQLite, através do comando:

*     Ctrl + Shift + P -> SQLite: Open Database -> Create new database   

-Executando
   É importante entender que o arquivo .sql sozinho não faz nada, ele é apenas texto. O banco de dados não lê, não processa e não reage ao que está escrito lá enquanto você não mandar executar.

   Executar, ou dar "Run", é o ato de enviar os comandos escritos no arquivo .sql para o banco de dados processar. É nesse momento que o SQLite lê cada instrução de cima para baixo e realmente realiza as ações como: criar tabelas, inserir dados, apagar registros. Antes disso, tudo não passa de texto numa tela. O comando para executar no VSCode será:
   
*     Ctrl + Shift + P -> SQLite: Run Query   
"""