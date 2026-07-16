"""
-View
   Uma VIEW é um obketo do SQLite que representa uma consulta SQL armazenada no banco de dados. Diferentemente de uma tabela, uma View não armaezena os dados propriamente ditos, ela apenas guarda a definição de uma consulta. Sempre que a View é consultada, o SQLite executa a consulta associada e apresenta o resultado como se fosse uma tabela comum.

   O principal objetivo de um View é simplificar consultas complexas e facilitar o acesso aos dados. Em vez de escrever repedidamente uma consulta com diversos JOIN, filtros e cálculos, o desenvolvedor pode criar uma View contendo essa lógica e consultá-la posteriormente de forma simples. Isso torna o código mais organizado, reduz a repetição de consultas e facilita a manutenção do sistema.

   Como uma View é baseada em uma consulta, ela sempre apresenta os dados mais recentes das tabelas utilizadas. Sempre que os dados das tabelas originais forem inseridos, alterados ou removidos, essas mudanças serão refletidas automaticamente nos resultados da View, pois ela não mantém uma cópia dos dados.

   Sua sintaxe é:

*     CREATE VIEW nome_da_view AS
*     SELECT coluna1, coluna2, ...
*     FROM tabela
*     WHERE condicao;

Agora em vez de consultar a tabela diretamente pode-se utilizar a VIEW

*     SELECT * FROM nome_da_view

-Segurança
   Além de simplificar consultas, elas também podem contribuir para a segurana das informações. Em muitos sistemas, é comum conceder acesso apenas à VIEW em vez das tabelas originais, permitindo que usuários visualizem apenas as colunas ou registros necessários, sem acesso direto a dados confidenciais.

   Assim como outros objetos de BD, as VIEWS possuem um nome próprio, ficam armazenadas no catálogo do banco e podem ser consultadas repeddidamente por qualquer aplicação que tenha acesso a elas. Caso seja necessário alterar sua definição, deve-se remover utilizando DROP VIEW e recriar com a nova consulta.
"""
