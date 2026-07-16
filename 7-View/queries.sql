-- BD Cursos
SELECT * FROM "users";
SELECT * FROM "courses";
SELECT * FROM "lessons";
SELECT * FROM "lessons_completed";
SELECT * FROM "certificates";

CREATE VIEW view_usuers_retricted AS
SELECT name, email
FROM users;

SELECT * FROM view_usuers_retricted;

DROP VIEW view_usuers_retricted;

