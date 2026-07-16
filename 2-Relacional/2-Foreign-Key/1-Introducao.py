"""
-Foreign Key
   São como uma ponte que conecta duas tabelas diferentes em um banco de dados, garantindo que essa conexão seja segura e faça sentindo.
   Se a Primary Key é o documento de identidade único de uma linha, a Foreign Key é a coluna que armazena a identidade de outra tabela para criar um relacionamento.

   A principal funçao da Foreign Key vai além da mera organização estrutural: ela é o mecanismo que assegura a integridade referencial dos dados dentro do ecossistema relacional. Ao definir essa restrição, o sistema de gerenciamento de banco de dados (SGBD) passa a impor e fiscalizar regras rígidas de consistência em todas as operações de modificaçao de dados (INSERT, UPDATE e DELETE).

   *Garatia de Existência de Vinculos
      O SGBD impede a inserção ou atualização de registros na tabela dependente (tabela filha) cujo valor na coluna da Foreign Key não possua uma correspondência exata e previamente existente na Primary Key da tabela referenciada (tabela pai). Isso elimina completamente a possibilidade de ocorrência de referências inválidas ou inexistentes no sistema.

   *Prevenção de Registros Órfãos
      O mecanismo restringe operações de exclusão ou alteração na tabela pai se houver registros vinculados na tabela filha. Caso uma tentativa de deleção de um registro vinculado referenciado ocorra, o banco de dados bloqueia a instrução por padrão, impedindo que a tabela dependente fique com dados desconectados e sem rastreabilidade.
   
   *Redução da Redundância de Dados
      No modelo relacional, a ausência de duplicação determina que cada fato ou entidade deve ser armazenada em um único local no banco de dados. Em vez de replicar informações descritivas repetidamente ao longo do sistema, o modelo adota uma arquitetura automatizada, onde tabelas especializadas são referenciadas por meio de chaves.

   Com isso, agora temos em mãos as principais peças de um banco de dados relacional

   Apartir daqui, o banco de dados deixa de ser apenas um amontoado de planilhas isoladas e passa a funcionar como um ecossistema inteligente, onde as informações conversam entre si com total segurança, organização e velocidade. Você acabou de dominar a base de como o mundo organiza seus dados.

-Pragma Foreign_Keys
   Por padrão normativo do SQLite, a verificação de restrições de integridade referencial fica desativada a cada nova conexão por motivos de compatibilidade histórica. É necessário injetar este comando no escopo da dessão para habilitar o motor de validação de chaves estrangeiras.
   Certifique-se de executar o comando de ativação e o de verificação na mesma sessão/janela de execução.

*     PRAGMA foreign_keys = ON;
*     PRAGMA foreign_keys;

Na sintaxe então teremos:

   Na tabela abaixo temos dos dados cadastrais exclusivos de cada cliente. A coluna id é a Primary Key (PK)

*   CREATE TABLE "Clientes" (
*      "id" INTEGER PRIMARY KEY,
*      "nome" TEXT NOT NULL,
*      "email" TEXT NOT NULL
*      ) STRICT;

   Na tabela abaixo armazenamos as compras realizadas. Acoluna id é a PK do pedido, e a colunas cliente_id é a Foreign Key (FK), que aponta diretamente para o id da tabela Clientes. Note que não tem a necessidade de incluir na tabela no características do comprador, já que temos todas com a FK.
   
*   CREATE TABLE "Pedidos" (
*      "id" INTEGER PRIMARY KEY,
*      "produto" TEXTO NOT NULL,
*      "valor" INTEGER,
*      "nome" TEXT,
*      "cliente_id" INTEGER,
*      FOREIGN KEY ("cliente_id") REFERENCES "Clientes" ("id")
*   ) STRICT;

-Cascade
   É um regra de integridadee referencial associada às FK. Ele serve para automatizar ações entre tabelas relacionadas, garantindo que, quando um registro na tabela pai for modificado ou excluído, as alterações sejam refletidas automaticamente nas tabelas filhas.
   
   *Sem o CASCADE, você teria que deletar ou atualizar manualmente os dados em várias tabelas para evitar erros de restrição ou dados órfãos.

   Existem dois cenários principais onde o CASCADE é aplicado

   *ON DELETE CASCADE
      Se um registro na tabela pai for excluído, todos os registros associados a ele na tabela filha serão ecluídos automaticamente.
      Ex: Se você deletar a conta de um usuário, todas as postagens que ele fez serão apagadas junto.

   *ON UPDATE CASCADE
      Se a PK de um registro na tabela pai for alterada, o valor da chave estrangeira correspoondente na tabela filha será atualizado automaticamente.
      Ex: Se o ID de um produto mudar de 10 para 20, todos os pedidos que continham o produto 10 serão atualizados para 20.

   !Cuidado:
      O efeito CASCADE pode ser muito perigoso se as tabelas estiverem muito encadeadas. Deletar um único registro no topo da hierarquia pode apagar milhares de dados associados sem que você perceba. Use com sabedoria!

   Veja o exemplo da sintaxe:

   *   CREATE TABLE "Pedidos" (
*        "id" INTEGER PRIMARY KEY,
*        "produto" TEXTO NOT NULL,
*        "valor" INTEGER,
*        "nome" TEXT,
*        FOREIGN KEY ("cliente_id") REFERENCES "Clientes" ("id")
!          ON DELETE CASCADE
!          ON UPDATE CASCADE
*   ) STRICT;






"""