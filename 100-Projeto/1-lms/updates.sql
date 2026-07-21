UPDATE "users"
SET "email" = 'pedro.new@email.com',
  "ultimo_login" = CURRENT_TIMESTAMP
WHERE "id" = 3;

UPDATE "sessions"
SET "expires" = STRFTIME('%s', 'now', '+40 days') WHERE "token" = '4E71AD08408EB359';

CREATE TRIGGER "set_users_update"
AFTER UPDATE ON "users"
BEGIN
   UPDATE "users" SET "criado" = CURRENT_TIMESTAMP 
   WHERE "id" = NEW."id";
END;

UPDATE "users" SET "email" = 'fernanda2@email.com'
WHERE "id" = 7;

SELECT "id", "email" FROM "USERS";
SELECT * FROM "users";
SELECT * FROM "sessions";