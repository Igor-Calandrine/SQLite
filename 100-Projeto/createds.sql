-- Configurações
PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;

PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;

PRAGMA cache_size = 2000;
PRAGMA busy_timeout = 5000;
PRAGMA temp_store = memory;

PRAGMA analysis_limit = 1000;
-- 

CREATE TABLE "users" (
   "id" INTEGER PRIMARY KEY,
   "name" TEXT NOT NULL,
   "password_hash" TEXT NOT NULL,
   "user_name" TEXT NOT NULL COLLATE NOCASE,
   "email" TEXT NOT NULL COLLATE NOCASE,
   "criado" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
   "ultimo_login" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
) STRICT;

CREATE TABLE "resets" (
   "token" TEXT PRIMARY KEY,
   "user_id" INTEGER NOT NULL,
   "ip" TEXT NOT NULL,
   "criado" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
   "expires" INTEGER NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP, '+30 DAY')),
      FOREIGN KEY ("user_id") REFERENCES "usuarios" ("id")
      ON DELETE CASCADE
) WITHOUT ROWID, STRICT;

-- Índice em FOREIGN KEY ON DELETE CASCADE
CREATE INDEX "idx_resets_user_id" ON "resets" ("user_id");

CREATE TABLE "sessions" (
   "token" TEXT PRIMARY KEY,
   "user_id" INT NOT NULL,
   "ip" TEXT NOT NULL,
   "criado" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
   "expires" INT NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP, '+30 DAY')),
      FOREIGN KEY ("user_id") REFERENCES "usuarios" ("id")
      ON DELETE CASCADE
) WITHOUT ROWID, STRICT;

-- Índice em FOREIGN KEY ON DELETE CASCADE
CREATE INDEX "idx_sessions_user_id" ON "sessions" ("user_id");

CREATE TABLE "courses" (
   "id" INTEGER PRIMARY KEY,
   "slug" TEXT NOT NULL COLLATE NOCASE UNIQUE,
   "title" TEXT NOT NULL,
   "description" TEXT NOT NULL,
   "lessons" INT NOT NULL,
   "hours" INT NOT NULL,
   "created" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
) STRICT;

CREATE TABLE "lessons" (
   "id" INTEGER PRIMARY KEY,
   "course_id" INTEGER NOT NULL,
   "title_slug" TEXT NOT NULL COLLATE NOCASE,
   "title" TEXT NOT NULL,
   "materia_slug" TEXT NOT NULL COLLATE NOCASE,
   "materia" TEXT NOT NULL,
   "video" TEXT NOT NULL,
   "description" TEXT NOT NULL,
   "second" INTEGER NOT NULL,
   "order" INTEGER NOT NULL,
   "free" INTEGER NOT NULL DEFAULT 0 CHECK ("free" = 0 OR "free" = 1),
   "created" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY ("course_id") REFERENCES "courses"("id"),
      UNIQUE ("course_id", "title_slug")
) STRICT;

-- Indece criado para otimizar buscas ordenados por "order"
CREATE INDEX "idx_lesson_order" ON "lessons" ("course_id", "order"); 

CREATE TABLE "lessons_completed" (
   "user_id" INTEGER NOT NULL,
   "course_id" INTEGER NOT NULL,
   "lesson_id" INTEGER NOT NULL,
   "completed" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY ("user_id", "course_id", "lesson_id"),
      FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE,
      FOREIGN KEY ("course_id") REFERENCES "courses"("id"),
      FOREIGN KEY ("lesson_id") REFERENCES "lessons"("id")
) WITHOUT ROWID, STRICT;

CREATE TABLE "certificates" (
   "id" TEXT PRIMARY KEY,
   "user_id" INTEGER NOT NULL,
   "course_id" INTEGER NOT NULL,
   "completed" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      UNIQUE ("user_id" ,"course_id"),
      FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE,
      FOREIGN KEY ("course_id") REFERENCES "courses"("id")
) WITHOUT ROWID, STRICT;

DROP TABLE "certificates";






