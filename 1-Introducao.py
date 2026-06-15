"""
-Banco de Dados
   Um banco de dados é uma coleção organizada de informações armazenadas eletronicamente, projetada para que os dados possam ser facilmente acessados, gerenciados e atualizados.

   É composto por tabelas, que organizam os dados em linhas e colunas, parecido com uma planilha. Cada linhas representa um regostro, e cada coluna representa um atributo desse registro, como nome, e-mail ou telefone. Essas tabelas podem se relacionar entre si, o que permite representar situações complexas do mundo real, como um cliente que fez vários pedidos, cada pedido com vários produtos.

   Para interagir com um banco de dados, usamos um sistema chamado:
      -SGDB, Sistema Gerenciados de Banco de dados
   Como exemplo, podemos citar:
      *MySQL
      *SQLite
      *PostgreSQL
      *MongoDB
      *Oracle

   É ele quem cuida de salvar, buscar, proteger e organizar tudo. Alinguagem mais comum para conversar com esses sistema é o:
      -SQL, Structured Query Language
   Que permite fazer perguntas e receber a resposta instantaneamente.

   Banco de dados estão por toda parte:
      *Quando você faz login em uma rede social
      *Consulta seu saldo bancário
      *Busca um produto num e-comerce
   Há um banco de dados trabalhando nos bastidores, recuperando exatamente as informações certas para você

-SQLite
   No universo dos banco de dados, existem diversas opções disponíveis, cada uma com suas particularidades e casos de uso. Diante de tantas escolhas, o SQLite se destaca como um ponto de partida ideal para quem está começando, e como uma ferramenta poderosa para desenvolvedores experientes em situações específicas.

   O SQLite é um banco de dados relacional de código aberto que funciona de forma completamente diferente dos seus concorrentes, enquanto sistemas como MySQL ou PstgreSQL operam como servidores independentes - exigindo instalação, configuração e manutenção contínua - o SQLite é uma biblioteca que roda diretamente dentro da sua aplicação. 
      *Todo o banco de dados fica armazenado em um único arquivo no disco, sem necessidade de nenhum servidor externo

   Como não há servidores para configurar, usuários para criar, portas de rede para liberar ou serviços para inicar, essa ausência de fricção permite que o aprendiz foque no que realmente importa:
      *Entender como os dados se organizam
      *Escrever consultas SQL
      *Modelar um banco de dados

   Além disso, utiliza-se a mesma linguagem SQL padrão usada nos demais sistemas, isso significa que tudo o que você aprende no SQLite, se aplica diretamente ao MySQL, ao PstgreSQL e a outros.

-Quando não escolher o SQLite
   Há de se reconhecer que existem limitações, ele não é adeuando para:
      *Aplicações com muitos usuários escrevendo dados simultaneamente, como grandes sistemas Web ou APIs de alta concorrência
   Para esses cenários, bancos de dados como PostgreSQL ou MySQL são mais indicados

-Banco de Dados Persistem
   Quem vem do mundo da programação tradicional, carrega um hábito muito natural que auando quer mudar algo, reescrever o código e roda de novo. O programa recomeça do zero, limpo, sem memória do que existia antes. No banco de dados, as coisas funcionam de forma completamente diferente.

      *Um banco de dados é persistente

   Isso significa que tudo o que você cria dentro dele continua existindo mesmo depois que você fecha o programa, desliga o computador ou passa dias sem mexer no projeto. Os dados ficam gravados no disco e permanecem lá até que você explicitamente mande apagá-los ou modificá-los.

   Se você criou uma tabela e quer alterar uma coluna, não basta reescrever o comando e executar de novo:
   
      *O SQLite vai te informar que a tabela já existe e ignorar o comando.

   Isso acontece porque o banco não interpreta seu arquivo de comandos como um script que define como o mundo deve ser, mas sim como uma série de instruções que modificam um estado já existente.
   Essa característica, que no início pode parecer uam complicação, é na verdade o que torna os bancos de dados tão poderosos e confiáveis. Um sistema bancário, um aplicativo de saúde ou um loja online não podem simplesmente "recomeçar do zero" a cada atualização. Os dados precisam sobreviver a atualizações de código, reiniciaçlizações de servidor e mudanças de atrutura. A persistêncoa é uma garantia, não um obstáculo.




   
   

   





"""