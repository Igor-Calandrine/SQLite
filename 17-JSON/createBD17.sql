PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;

CREATE TABLE usuarios (
   id INTEGER PRIMARY KEY,
   dados TEXT NOT NULL
) STRICT;

INSERT INTO usuarios(dados) VALUES (
'{
    "username": "joaosilva",
    "nome": "João",
    "sobrenome": "Silva",
    "email": "joao.silva@email.com",
    "password": "Senha@123"
  }'
),
(
'{
    "username": "mariasantos",
    "nome": "Maria",
    "sobrenome": "Santos",
    "email": "maria.santos@email.com",
    "password": "Senha@456"
  }'
),
(
'{
    "username": "pedrooliveira",
    "nome": "Pedro",
    "sobrenome": "Oliveira",
    "email": "pedro.oliveira@email.com",
    "password": "Senha@789"
  }'
);

