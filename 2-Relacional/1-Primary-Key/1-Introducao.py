"""
-Rowid
   Por padrão, quase toda tabela criada no SQLite possui uma coluna oculta chamada #rowid. Ela funciona como uma chave primária automática de tipo inteiro de 64 bits assinados.

   Sempre que você insere uma nova linha na tabela, o SQLite atribui automaticamente um número sequencial exlcusivo a essa linhas, a menos que você forneça um valor manualmente.
   Você pode consultar diretamente no seu comando SELECT

*     SELECT rowid, nome FROM Usuarios;

-Chave Primária
   As chaves primárias são a espinhas dorsal do design de qualquer banco de dados relacional, incluindo o SQLite. Elas servem para garantir que cada registro (linhas) em uma tabela seja absolutamente único e identificável

   Para uma coluna (ou conjunto de colunas) ser uma chave primária, ela precisa seguir duas regras estritas:

   *Unicidade
      Não podem existir duas linhas com o mesmo vvalor na chave primária

   *Não nula
      O padrão do SQL determina que chaves primárias não podem ser vazias. No entanto, por questões de compatibilidade históricas, o SQLite permite valores NULL em chaves primárias comuns, a menos que você use o tipo INTEGER PRIMARY KEY

   A sintaxe é a seguinte:

*     CREATE TABLE Funcionarios (
*         id INTEGER PRIMARY KEY,
*         nome TEXT NOT NULL
*         ) STRICT;

   Se você inserir um funcionário sem passar o id, o SQLite vai gerar automaticamente o próximo número inteiro.

   Se você inserir uma chave primeira com um id muito a frente do atual (1, 2, 3, 20) a próxima será o número seguinte ao número maior inserido (21).

   Você pode usar textos, como CPF, email ou um código como chave primária. No caso ainda será criado uma rowid oculto no fundo para organizar a tabela, mas a sua chave de busca oficial e a garatia de unicidade estarão na coluna email.

-Chave Primária Composta
   Às vezes, uma coluna sozinhas não garante a unicidade, mas a combinação de duas ou mais colunas sim.
   Por exemplo, um aluno pode se inscrever em várias cursos, e um curso pode ter várias alunos. Mas o mesmo aluno não pode se inscrever no mesmo curso duas vezes. Ex:

*   CREATE TABLE Inscricoes (
*      id_curso INTEGER,
*      id_aluno INTEGER,
*      data_inscricao TEXT,
*      PRIMARY KEY (id_curso, id_aluno)
*   ) STRICT;



"""