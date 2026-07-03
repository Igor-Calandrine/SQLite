SELECT * FROM "users";
SELECT * FROM "courses";
SELECT * FROM "lessons";
SELECT * FROM "lessons_completed";
SELECT * FROM "certificates";

-- Objetivo de treinar o uso de JOIN

-- Abaixo temos uma tabela com o ID de cada Curso, o Titulo de cada lição e o tempo.
SELECT courses.id AS 'ID Curso', lessons.slug AS 'Slug Lesson', lessons.seconds 
FROM courses 
JOIN lessons
ON courses.id = lessons.course_id;

-- Abaixo temos uma tabela com o ID de cada Curso, o Titulo de cada curso e o tempo total.
SELECT courses.id AS 'ID', courses.slug AS 'Slug Curso', SUM(lessons.seconds)
FROM courses 
JOIN lessons
ON courses.id = lessons.course_id
GROUP BY courses.slug
ORDER BY SUM(lessons.seconds);

-- Aqui temos o nome com o id de cada curso finalizado e o nome
SELECT users.id, users.name, lessons_completed.course_id, courses.title
FROM  users
JOIN lessons_completed
ON users.id = lessons_completed.user_id
JOIN courses
ON lessons_completed.course_id = courses.id;

-- Agora acrescentamos o título de cada lição
SELECT users.id, users.name, lessons_completed.course_id, courses.title, lessons.title
FROM  users
JOIN lessons_completed
ON users.id = lessons_completed.user_id
JOIN courses
ON lessons_completed.course_id = courses.id
JOIN lessons
ON lessons_completed.lesson_id = lessons.id;

-- Agora acrescentamos uma ordem por id do nome e id do curso com Alias para abriviações
-- Não gostei disso, piorou muito a leitura -.-
SELECT u.id, u.name, l_c.course_id, c.title, l.title
FROM  users AS u
JOIN lessons_completed AS l_c
ON u.id = l_c.user_id
JOIN courses AS c
ON l_c.course_id = c.id
JOIN lessons AS l
ON l_c.lesson_id = l.id
ORDER BY u.id, l_c.course_id;

-- Agora temos o tempo total do curso e agrupando pelo id do nome juntamente id do curso
SELECT users.id ,users.name, lessons_completed.course_id, courses.title, courses.horas
FROM  users
JOIN lessons_completed
ON users.id = lessons_completed.user_id
JOIN courses
ON lessons_completed.course_id = courses.id
GROUP BY users.id, lessons_completed.course_id
ORDER BY users.id, lessons_completed.course_id ASC;

-- Agora alterando a ordem para o sentido do id do curso
SELECT lessons_completed.course_id, users.id ,users.name, courses.title, courses.horas
FROM  users
JOIN lessons_completed
ON users.id = lessons_completed.user_id
JOIN courses
ON lessons_completed.course_id = courses.id
GROUP BY users.id, lessons_completed.course_id
ORDER BY courses.id ASC;







