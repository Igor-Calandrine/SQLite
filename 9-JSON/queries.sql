-- Prática de select em um JSON
SELECT json_valid(
'{
    "username": "joaosilva",
    "nome": "João",
    "sobrenome": "Silva",
    "email": "joao.silva@email.com",
    "password": "Senha@123"
  }'
);

SELECT json(
'{
    "username": "joaosilva",
    "nome": "João",
    "sobrenome": "Silva",
    "email": "joao.silva@email.com",
    "password": "Senha@123"
  }'
);

SELECT json_extract('{
    "username": "joaosilva",
    "nome": "João",
    "sobrenome": "Silva",
    "email": "joao.silva@email.com",
    "password": "Senha@123"
  }',
  '$.username');

SELECT json_extract('{
   "username": "joaosilva",
   "nome": "João",
   "sobrenome": "Silva",
   "email": "joao.silva@email.com",
   "password": "Senha@123"
}',
'$.email');


INSERT INTO usuarios(dados) VALUES (
'{
    "username": "joaosilva",
    "nome": "João",
    "sobrenome": "Silva",
    "email": "joao.silva@email.com",
    "password": "Senha@123"
  }'
);

-- Aqui podemos obervar a importância do uso de json()
INSERT INTO usuarios(dados) VALUES (json(
'{
    "username": "joaosilva",
    "nome": "João",
    "sobrenome": "Silva",
    "email": "joao.silva@email.com",
    "password": "Senha@123"
  }'
));

-- Vamos alterar o valor de algumas chave
UPDATE usuarios
SET dados = json_set(dados, 
   '$.nome', 'Carlos',
   '$.username', 'carlito')
WHERE id = 1;

UPDATE usuarios
SET dados = json_set(dados,
   '$.sobrenome', 'Livia',
   '$.email', 'livia.santos@email.com')
WHERE id = 2;

UPDATE usuarios
SET dados = json_remove(dados,
   '$.password')
WHERE id = 3;

-- Vamos agora criar uma coluna nova para inserir o nome do usuário e sem seguida adicionar o nome pelo JSON
ALTER TABLE usuarios
ADD COLUMN nome TEXT;

UPDATE usuarios
SET nome = json_extract(dados, '$.nome')
;

-- Agora temos uma coluna sendo gerada automaticamente com as informações JSON de dados
ALTER TABLE usuarios
ADD COLUMN sobrenome TEXT
   GENERATED ALWAYS AS (dados ->> '$.sobrenome') VIRTUAL;

ALTER TABLE usuarios
ADD COLUMN email TEXT
   GENERATED ALWAYS AS (dados ->> '$.email') VIRTUAL;

   
SELECT * FROM usuarios;
DROP TABLE usuarios;