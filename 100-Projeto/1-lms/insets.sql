INSERT INTO "users" ("name", "password_hash", "email", "user_name")
VALUES
('Carlos Silva', hex(randomblob(8)), 'carlos@email.com', 'carlos'),
('João Pereira', hex(randomblob(8)), 'joao@email.com', 'joao'),
('Pedro Alves', hex(randomblob(8)), 'pedro@email.com', 'pedro'),
('Lucas Souza', hex(randomblob(8)), 'lucas@email.com', 'lucas'),
('Mateus Lima', hex(randomblob(8)), 'mateus@email.com', 'mateus'),
('Ana Costa', hex(randomblob(8)), 'ana@email.com', 'ana'),
('Fernanda Rocha', hex(randomblob(8)), 'fernanda@email.com', 'fernanda'),
('Mariana Gomes', hex(randomblob(8)), 'mariana@email.com', 'mariana'),
('Renata Dias', hex(randomblob(8)), 'renata@email.com', 'renata'),
('Beatriz Melo', hex(randomblob(8)), 'beatriz@email.com', 'beatriz');

INSERT INTO "resets" ("token", "user_id", "ip", "expires")
VALUES
(hex(randomblob(8)), 1, '123.1.1.1', strftime('%s', 'now', '+12 hours')),
(hex(randomblob(8)), 4, '123.1.1.2', strftime('%s', 'now', '+12 hours')),
(hex(randomblob(8)), 8, '123.1.1.3', strftime('%s', 'now', '+12 hours'));

INSERT INTO "sessions"
("token", "user_id", "ip", "expires")
VALUES
(hex(randomblob(8)), 1, '123.1.1.1', strftime('%s','now','+30 days')),
(hex(randomblob(8)), 4, '123.1.1.2', strftime('%s','now','+30 days')),
(hex(randomblob(8)), 8, '123.1.1.3', strftime('%s','now','+30 days'));

--- courses
INSERT INTO "courses" ("slug","title","description","lessons","hours")
VALUES
('html-para-iniciantes','HTML para Iniciantes','Aprenda a linguagem de marcação que é a base da web.',40,10),
('css-animacoes','CSS Animações','Domine transições, transforms e keyframes.',35,8),
('javascript-completo','JavaScript Completo','Sintaxe, DOM, ES modules, APIs Web e Async/Await',120,25),
('sqlite-fundamentos','SQLite Fundamentos','Aprenda create table, insert, select e mais.',50,12);

--- lessons
INSERT INTO "lessons"
("course_id","title_slug","title",
"materia","materia_slug","second",
"video","description","order","free")
VALUES
(1,'introducao-ao-html','Introdução ao HTML','Fundamentos','fundamentos',300,'html01.mp4','Visão geral do HTML e configuração do ambiente.',1,1),
(1,'tags-basicas','Tags Básicas','Fundamentos','fundamentos',420,'html02.mp4','Uso das principais tags de estrutura.',2,0),
(1,'atributos-e-semantica','Atributos e Semântica','Fundamentos','fundamentos',360,'html03.mp4','Atributos globais e boas práticas semânticas.',3,0),
(1,'imagens-e-links','Imagens e Links','Multimídia','multimidia',480,'html04.mp4','Inserindo imagens responsivas e links internos/externos.',4,0),
(1,'conclusao','Conclusão','Estrutura','estrutura',540,'html05.mp4','Criando tabelas acessíveis e formulários semânticos.',5,0),

(2,'transicoes-css','Transições CSS','Fundamentos','fundamentos',360,'css01.mp4','Introdução às propriedades de transição.',1,1),
(2,'transforms-2d-e-3d','Transforms 2D e 3D','Fundamentos','fundamentos',420,'css02.mp4','Aplicando transformações de escala, rotação e translação.',2,0),
(2,'keyframes-na-pratica','@keyframes na prática','Animações','animacoes',480,'css03.mp4','Criando animações complexas com keyframes.',3,0),
(2,'propriedades-de-animacao','Propriedades de Animação','Animações','animacoes',450,'css04.mp4','Controlando timing, delay e iteration count.',4,0),
(2,'conclusao','Conclusão','Avançado','avancado',540,'css05.mp4','Disparando animações via Intersection Observer.',5,0),

(3,'introducao-ao-javascript','Introdução ao JavaScript','Fundamentos','fundamentos',300,'js01.mp4','História, versões ES e configuração do ambiente.',1,1),
(3,'variaveis-e-tipos','Variáveis e Tipos','Fundamentos','fundamentos',420,'js02.mp4','let, const, tipos primitivos e conversões.',2,0),
(3,'funcoes-e-escopo','Funções e Escopo','Fundamentos','fundamentos',480,'js03.mp4','Declaração, arrow functions e closures.',3,0),
(3,'dom-manipulation','DOM Manipulation','DOM','dom',540,'js04.mp4','Selecionando e alterando elementos HTML.',4,0),
(3,'fetch-api','Fetch API','Async','async',600,'js05.mp4','Requisições assíncronas com fetch e async/await.',5,0),

(4,'introducao-ao-sqlite','Introdução ao SQLite','Fundamentos','fundamentos',300,'sqlite01.mp4','O que é SQLite e onde usar.',1,1),
(4,'criacao-de-tabelas','Criação de Tabelas','DDL','ddl',420,'sqlite02.mp4','Sintaxe CREATE TABLE e tipos de dados.',2,0),
(4,'select-e-where','SELECT e WHERE','DML','dml',480,'sqlite03.mp4','Consultas básicas e filtros.',3,0),
(4,'insert-update-delete','INSERT, UPDATE, DELETE','DML','dml',540,'sqlite04.mp4','Manipulação de dados na prática.',4,0),
(4,'indices-e-otimizacao','Índices e Otimização','Performance','performance',600,'sqlite05.mp4','Criação de índices e análise de desempenho.',5,0);

-- lessons_completed
INSERT INTO "lessons_completed" ("user_id","course_id","lesson_id")
VALUES
(1,1,1),
(1,1,2),
(1,1,3),
(1,2,6),
(1,2,7),
(1,2,8),
(1,2,9),
(2,3,11),
(2,3,12),
(2,3,13),
(2,3,14),
(2,3,15),
(2,4,16),
(2,4,17),
(2,4,18),
(3,1,1),
(3,1,2),
(3,1,3),
(3,1,4),
(3,1,5),
(3,2,6),
(3,2,7),
(4,3,11),
(4,3,12),
(4,3,13),
(4,3,14),
(4,3,15),
(4,4,16),
(4,4,17),
(4,4,18),
(4,4,19),
(5,1,2),
(5,1,3),
(5,1,4),
(5,1,5),
(5,2,6),
(5,2,7),
(5,2,8),
(5,2,9),
(5,2,10),
(6,3,11),
(6,3,12),
(6,3,13),
(6,3,14),
(6,3,15),
(6,4,16),
(6,4,17),
(6,4,18),
(6,4,19),
(7,1,3),
(7,1,4),
(7,1,5),
(7,2,6),
(7,2,7),
(7,2,8),
(7,2,9),
(7,2,10),
(8,3,11),
(8,3,12),
(8,3,13),
(8,3,14),
(8,3,15),
(8,4,16),
(8,4,17),
(8,4,18),
(8,4,19),
(8,4,20),
(9,1,1),
(9,1,2),
(9,1,3),
(9,1,4),
(9,1,5),
(9,2,6),
(9,2,9),
(9,2,10),
(10,3,11),
(10,3,12),
(10,3,13),
(10,3,14),
(10,3,15),
(10,4,16),
(10,4,17),
(10,4,18),
(10,4,19),
(10,4,20);

--- certificates
INSERT INTO "certificates" ("id","user_id","course_id")
VALUES
(hex(randomblob(8)),1,1),
(hex(randomblob(8)),1,2),
(hex(randomblob(8)),2,3),
(hex(randomblob(8)),2,4),
(hex(randomblob(8)),3,1),
(hex(randomblob(8)),3,2),
(hex(randomblob(8)),4,3),
(hex(randomblob(8)),4,4),
(hex(randomblob(8)),5,1),
(hex(randomblob(8)),5,2),
(hex(randomblob(8)),6,3),
(hex(randomblob(8)),6,4),
(hex(randomblob(8)),7,1),
(hex(randomblob(8)),7,2),
(hex(randomblob(8)),8,3),
(hex(randomblob(8)),8,4),
(hex(randomblob(8)),9,1),
(hex(randomblob(8)),9,2),
(hex(randomblob(8)),10,3),
(hex(randomblob(8)),10,4);

SELECT * FROM "certificates";