CREATE VIEW "lessons_completed_full" AS
SELECT "users"."id", "users"."email", 
       "courses"."title" AS "course", 
       "lessons"."title" AS "lesson",  
       "lessons_completed".*
FROM "lessons_completed"
JOIN "users" 
   ON  "users"."id" = "lessons_completed"."user_id"
JOIN "lessons"
   ON  "lessons"."id" = "lessons_completed"."user_id"
JOIN "courses"
   ON  "courses"."id" = "lessons_completed"."user_id";


CREATE VIEW "certificates_full" AS
SELECT "certificates"."id", "certificates"."user_id",
       "users"."name", 
       "certificates"."course_id",
       "courses"."title", "courses"."hours", "courses"."lessons",
       "certificates"."completed"
FROM "certificates"
JOIN "users" 
   ON  "users"."id" = "certificates"."user_id"
JOIN "courses"
   ON  "courses"."id" = "certificates"."user_id";

CREATE VIEW "lessons_nav" AS
SELECT "current_lessons"."title_slug" AS "current_slug",
       "lessons".*
FROM "lessons" AS "current_lessons"
JOIN "lessons"
   ON "lessons"."course_id" = "current_lessons"."course_id"
   AND "lessons"."order" BETWEEN "current_lessons"."order" - 1 AND "current_lessons"."order" + 1
   ORDER BY "lessons"."order";

-- SELECT DE VIEWS
SELECT * FROM "lessons_completed_full" WHERE "id" = 1;
SELECT * FROM "certificates_full";
SELECT * FROM "lessons_nav" WHERE "course_id" = 1 AND "current_slug" = 'atributos-e-semantica';

-- Encontrar nome por e-amil
SELECT "name" FROM "users" WHERE "email" = 'ana@email.com';

-- Encontrar as lessons de um curso
SELECT * FROM "lessons" WHERE "course_id" = 1 ORDER BY "order";

-- Encontrar as lessons de um curso pelo nome do curso
SELECT * FROM "lessons" WHERE "course_id" = 
   (SELECT "id" FROM "courses" WHERE "slug" = 'javascript-completo')
   ORDER BY "order";

-- Encontrar as lessons que são gratuitas
SELECT * FROM "lessons" WHERE "free" = 1;

-- Encontrar determinado certificado
SELECT * FROM "certificates" WHERE "id" = 'BD3469C7BDA2CB98';

-- Encontrar o tempo total em minutos de um curso
SELECT (SUM("second") / 60) AS "total_minutes" FROM "lessons" WHERE "course_id" = 1;

-- Encontrar o total de lessons completas de um usuário de um determinado curso
SELECT COUNT("lessons"."title"), COUNT("lessons_completed"."completed")
FROM "lessons"
LEFT JOIN "lessons_completed"
   ON "lessons_completed"."lesson_id" = "lessons"."id" AND "lessons_completed"."user_id" = 1
   WHERE "lessons"."course_id" = 1;












