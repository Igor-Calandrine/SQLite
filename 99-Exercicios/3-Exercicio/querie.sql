SELECT * FROM "users";
SELECT * FROM "courses";
SELECT * FROM "lessons";
SELECT * FROM "lessons_completed";
SELECT * FROM "certificates";

-- 1. Selecione todas as aulas do curso de html-para-iniciantes e ordene por lesson-order em ordem crescente

SELECT courses.slug, lessons.title, lessons.lesson_order
FROM courses
JOIN lessons
ON courses.id = lessons.course_id
WHERE courses.id = 
      (SELECT id FROM courses 
      WHERE slug = 'html-para-iniciantes')
ORDER BY lessons.lesson_order ASC;

-- 2. Somar o total de segundos das aulas do curso de css-animacoes

SELECT   courses.slug, 
         SUM(lessons.seconds) AS 'segundos',
         SUM(lessons.seconds)/60 AS 'minutos'
FROM courses
JOIN lessons
ON courses.id = lessons.course_id
WHERE courses.id = 
      (SELECT id FROM courses 
      WHERE slug = 'css-animacoes')
GROUP BY courses.slug
ORDER BY lessons.seconds;

-- 3. Contar o total de aulas e agrupar por curso

SELECT   courses.slug,
         COUNT(lessons.course_id) AS 'total aulas'
FROM courses
JOIN lessons
ON courses.id = lessons.course_id
GROUP BY courses.slug
ORDER BY COUNT(lessons.course_id);

-- 4. Somar o total de segundos das aulas, agrupar por curso e ordenar o total de segundos por ordem decrescente

SELECT   courses.slug, 
         SUM(lessons.seconds)
FROM courses
JOIN lessons
ON courses.id = lessons.course_id
GROUP BY courses.slug
ORDER BY SUM(lessons.seconds) DESC;

-- 5. Utilize a query 4, e filtre apenas os cursos que possuem mais de 2300 segundos de aulas. Continue ordenando

SELECT   courses.slug, 
         SUM(lessons.seconds)
FROM courses
JOIN lessons
ON courses.id = lessons.course_id
GROUP BY courses.slug
HAVING SUM(lessons.seconds) >= 2300
ORDER BY SUM(lessons.seconds) DESC;

-- 6. Utilize a query 4, mostre o título do curso no lugar do course_id

SELECT   courses.id,
         courses.title, 
         SUM(lessons.seconds) AS 'segundos'
FROM courses
JOIN lessons
ON courses.id = lessons.course_id
GROUP BY courses.slug
-- HAVING SUM(lessons.seconds) >= 2300
ORDER BY SUM(lessons.seconds) DESC;

-- 7. Selecione o ID dos certificados de mariana@email.com

SELECT   users.name, users.email, 
         certificates.id
FROM users
JOIN certificates
ON certificates.user_id =
      (SELECT id FROM users
      WHERE email = 'mariana@email.com')
WHERE users.id = 
      (SELECT id FROM users
      WHERE email = 'mariana@email.com');

-- 8. Selecione todas as aulas completas ou não pelo usuário lucas@email.com "ID=4". Mostre o título da aula e se está completa ou não

SELECT   u.id, u.name, u.email, 
         l.title,
         l_c.lesson_id
FROM users AS u
CROSS JOIN lessons AS l
LEFT JOIN lessons_completed AS l_c 
   ON l_c.lesson_id = l.id
   AND l_c.user_id = u.id
WHERE u.id = 
      (SELECT id FROM users
      WHERE email = 'lucas@email.com')
;

SELECT   l.id, l.title, l_c.completed
FROM lessons AS l
LEFT JOIN lessons_completed AS l_c
   ON l.id = l_c.lesson_id
   AND l_c.user_id = 
      (SELECT id FROM users
      WHERE email = 'lucas@email.com')

-- WHERE l_c.user_id = 
--    (SELECT id FROM users
--    WHERE email = 'lucas@email.com')
;
 

-- 9. Selecione todas as aulas anterior/próxima da aula funcoes-e-escopo. Retorne 3 aulas (se existirem): a anterior, a atual e a próxima. Utilize lesson_order para isso.

SELECT id, slug, lesson_order
FROM lessons
WHERE course_id = 3
AND lesson_order 

   BETWEEN (
      SELECT lesson_order
      FROM lessons
      WHERE slug = 'funcoes-e-escopo'
   ) - 1
   AND (
      SELECT lesson_order
      FROM lessons
      WHERE slug = 'funcoes-e-escopo'
   ) + 1  
; 

-- Usando WITH

WITH aula_atual AS (
   SELECT lesson_order
   FROM lessons
   WHERE slug = 'funcoes-e-escopo'
)

SELECT l.id, l.slug, l.lesson_order
FROM lessons l, aula_atual a
WHERE course_id = 3
AND l.lesson_order 
   BETWEEN a.lesson_order - 1
   AND  a.lesson_order + 1  
;       

SELECT lessons2.slug, lessons2.lesson_order
FROM lessons AS lessons1
JOIN lessons AS lessons2
ON lessons1.course_id = lessons2.course_id
WHERE lessons1.slug = 'funcoes-e-escopo'
   AND lessons2.lesson_order 
      BETWEEN lessons1.lesson_order -1
      AND lessons1.lesson_order +1
;



