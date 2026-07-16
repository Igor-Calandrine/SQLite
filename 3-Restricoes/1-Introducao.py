"""
-Not Null
   Como já vimos, a restrição NOT NULL é uma das regras mais fundamentais e utilizadas no design de banco de dados. A funçao dela é muito clara e direta:
      *Garantir que um campo nunca fique vazio (sem dados)

   Com ela podemos garantir:
      *Integridade de dados
         Garante que informações essenciais sempre existam, como o nome de um usuário
      *Evita erros de programação
         Lidar com valores NULL no código da sua aplicação (Node.js, Python, Java, etc) costuma gerar bugs clássicos. Forçar o dado a existir direto no banco reduz essa chance.
      *Melhoria em consultas
         Facilita a lógica de busca, não precisa-se ficar checando o tempo todo se o campo IS NULL ou IS NOT NULL.

-Unique
   A restrição UNIQUE é impedir que existam dados duplicados, então podemos dizer que sua função é garantir que:
      *Os valores de determinada coluna sejam diferentes entre si em toda a tabela

   Com ela podemos garantir:
      *Identificação Exclusiva
         É idela para campos que servem como identificadores secundários no sistema, como CPF, email, número de passaporte ou nome de usuário
      *Regras de Negócio
         Garante que a lógica do seu sustema não seja quebrada por duplicidade, como email duplicado

-Collate
   A Cláusula COLLATE é utilizada para definir a regra de colação (ou ordenação) de uma coluna ou de uma consulta específica. Em termos simples, ela diz ao banco de dados como ele deve comprar e ordenar strings de texto.

   Por padrão, os computadores comparam textos diferentes rigidamente maiúsculas de minúsculas e acentos com base em seus valores binários. O COLLATE permite que você mude esse comportamento para deixar as buscas e ordenações mais inteligentes.

   No SQLite teremos 3 regras de colação embutidas que você pode usar:

   *BINARY (PADRÃO)
      Compara os textos byte a byte usando a codifiação Memcmp(). Isso significa que COLLATE BINARY, diferencia maiusculas de minúsculas.

   *NOCASE
      Ignora a diferença entre maiúsculas e minúsculas, assim "Ana", "ana, "ANA" serão tratadas como textos idênticos em buscas e ordenações.
      Obs: NOCASE só funciona para os 26 caracteres do alfabeto inglês, ele não remove acentos automaticamente.

   *RTRIM
      Funciona exatamente como o BINARY, mas ignora espaços em branco que estejam no final da string

-Default
   A restrição DEFAULT é uma ferramenta indispensável para preencher "espaços em branco", ela permite que você defina um valor padrão para uma coluna.
   Isso significa que, se você ou o seu sistema inserirem um novo registro na tabeka e esquecerem (ouoptarem por não) passar um valor para aquela coluna específica, o SQLite usará automaticamente o valor que você configurou no DEFAULT, em vez de deixar o campo vazio ou gerar um erro.
   Ao utilizar DEFAULT garantimos:
   
   *Praticidade no Cadastro
      Economizamos código na hora do INSERT. Se a grande maioria dos seus usuários começa com o status "Ativo", você não precisa enviar isso manualmente toda vez.
   
   *Consistência de Dados
      Garante que campos importantes tenham um valor inicial válido desde o "segundo zero" da criação do registro

   *Segurança com NOT NULL
      É o parceiro perfeito para a restrição NOT NULL, pois evita que a inserção falhe caso o dado não seja enviado.

   Temos uma função especial amplamente utilizada para obter a data e a hora exatas do momento atual, ela é a CURRENTE_TIMESTAMP que utilizada com DEFAULT teremos os dados inseridos de forma automática, registrando assim o momento de uma vendo por exemplo.
   O SQLite sempre gera esse valor no fuso horário UTC que é o horário "zero" de Greenwich. Isso significa que no Brasil parecerá 3 horas adiantado. Para resolver isso e converter para o horário local em ums SELECT utiliza-se:

*     SELECT datetime(CURRENT_TIMESTAMP, 'localtime');

   Não é recomendado converter o horário na criação de dados, caso o sistema cresça a passe a oferecer serviços internacionais, os registros estarão configurados para o local e assim criando dados de forma errônea.

-Check
   A restrição CHECK no SQLite é como um "segurança" personalizado para as colunas da sua tabela. Enquanto o NOT NULL garante que o campo não fique vazio e o UNIQUE impede duplicatas, o CHECK permite que você crie as suas próprias regras de validação usando expressões lógicas.

   Se alguém inserir ou atualizar um dado que não cumpra a regra estabelecida no CHECK, o SQLite bloqueia imediatamente e protege a integridade do banco.
   Ao utilizar CHECK garantimos:
   
   *Validação Direta no Banco
      Impede que dados absurdos ou corrompidos entrem no sistema.
      Ex: idade negativa, preços baixo de zero

   *Consistência Absoluta
      Mesmo que a validação falhe no código do seu aplicativo (front-end ou back-end), o banco de dados continua sendo a última e mais segura linhas de defesa

   *Flexibilidade
      Você pode criar regras que combinem mais de uma coluna ou usem operadores matemáticos e de texto

   No exemplo abaixo temos todos os comandos acima

*   CREATE TABLE Funcionarios (
*      "id" INTEGER PRIMARY KEY,
*      "nome" TEXT NOT NULL COLLATE NOCASE,
*      "idade" INTEGER NOT NULL CHECK("idade" >= 18),
*      "email" TEXT NOT NULL UNIQUE COLLATE NOCASE,
*      "salario REAL NOT NULL CHECK("salario" > 0),
*      "endereço" TEXT DEFALUT 'Brasil',
*      "registro" TEXT DEFAULT CURRENT_TIMESTAMP,
*      "departamento" TEXT NOT NULL CHECK("departamento" IN ('Vendas', 'TI', 'RH'))
*      ) STRICT;



"""