"""
-Insert
   O INSERT é o comando responsável por "alimentar" o banco de dados, para entender como ele funciona nos bastidores, pense na tabela como uma planilha e no comando como uma instrução para adicionar uma nova linha.

   Quando você executa um comando se inserção, o SQLite faz uma checagem em 3 etapas:
      
      *Mapeamento
         Ele olha para as colunas que vocÇe escolheu e encaixa os valores na ordem correspondente
      *Validação de Tipos
         Ele verifica se você está colocando o tipo de dado correto
      *Verificação de Regras (Constraints)
         Ele garante que nanhuma regra da tabela seja quebrada

-Into
   O INTO é a palavras de transição que indica o destino dos dados
   No comando INSERT INTO, você está literalmente dizendo ao banco de dados, "Insira [estes dados] para dentro da [tabela X].

-Values
   É o comando que define o que está entrando na tabela. Para usar VALUES sem errar, existem 2 regras básicas sobre como o SQLite enxerga esses dados.

   *Casamento de posições
      O SQLite funciona por ordem posicional, o primeiro valor dentro dos parênteses do VALUES vai para a primeira coluna listada no INSERT INTO, o segundo valor para a segunda coluna, e assim por diante.

   *O tipo de dado
      A forma se escreve o dado dis que tipo de informação ele é: texto com aspas, números sem aspas, decimais usando ponto, ausência de dado com NULL

   Uma característica muito importante de VALUES é a capacidade de inserir vários registros de uma vez só, separando os blocos de parênteses por vírgulas. Isso é muito mais rápido para o banco de dados do que executar várias comandos separados.
   Ex:

*     INSERT INTO "usuarios" (nome, idade) VALUES
*     ("Igor", 20),
*     ("Bianca, 19),
*     ("Yuri, 18);

   
-Insert or Ignore
   Se você tentar inserir um dado que viola uma regra dde unicdade (como um ID, e-mail), o SQLite normalmente trava a execuçao e joga um erro. Se você usar o IGNORE, ele simplesmente pula aquela inserção e continua o script sem dar erro.

*     INSERT OR IGNORE INTO "usuarios" (id, nome) VALUES 
*     (1, "Igor")



-Insert or Replace
   Se o registro não existir, ele insere, se já existir ele deleta o registro antigo e insere o novo por cima.

*     INSERT OR REPLACE INTO "usuarios" (id, nome) VALUES 
*     (1, "Igor Araújo")
"""