PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;

CREATE TABLE Users (
   "id" INTEGER PRIMARY KEY,
   "name" TEXT NOT NULL COLLATE NOCASE,
   "password" TEXT NOT NULL,
   "email" TEXT NOT NULL UNIQUE COLLATE NOCASE,
   "created" TEXT  NOT NULL DEFAULT CURRENT_TIMESTAMP
) STRICT;

CREATE TABLE Courses (
   "id" INTEGER PRIMARY KEY,
   "slug" TEXT NOT NULL UNIQUE COLLATE NOCASE,
   "title"  TEXT NOT NULL UNIQUE COLLATE NOCASE,
   "description" TEXT NOT NULL,
   "aulas" INTEGER NOT NULL CHECK ("aulas" > 0),
   "horas" INTEGER NOT NULL CHECK ("horas" > 0),
   "created" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
) STRICT;

CREATE TABLE Lessons (
   "id" INTEGER PRIMARY KEY,
   "course_id" INTEGER NOT NULL,
   "slug" TEXT NOT NULL COLLATE NOCASE,
   "title" TEXT NOT NULL,
   "materia" TEXT NOT NULL,
   "materia_slug" TEXT NOT NULL UNIQUE COLLATE NOCASE,
   FOREIGN KEY ("course_id") REFERENCES Courses ("id"),
   UNIQUE ("course_id", "slug")
) STRICT;

CREATE TABLE Lesson_Video (
   "id" INTEGER PRIMARY KEY,
   "couser_id" INTEGER NOT NULL,
   "lesson_id" INTEGER NOT NULL,
   "video" TEXT NOT NULL,
   "seconds" INTEGER NOT NULL,
   "description" TEXT NOT NULL,
   "lesson_order" INTEGER NOT NULL CHECK ("lesson_order" > 0),
   "free" INTEGER NOT NULL DEFAULT 0 CHECK ("free" IN (0, 1)),
   "created" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY ("couser_id") REFERENCES Courses ("id"),
   FOREIGN KEY ("lesson_id") REFERENCES Lessons ("id")
) STRICT;

CREATE TABLE Lesson_Completed (
   "user_id" INTEGER NOT NULL,
   "course_id" INTEGER NOT NULL,
   "lesson_id" INTEGER NOT NULL,
   "completed" TEXT DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ("user_id", "course_id", "lesson_id"),
   FOREIGN KEY ("user_id") REFERENCES Users ("id")
      ON DELETE CASCADE,
   FOREIGN KEY ("course_id") REFERENCES Courses ("id"),
   FOREIGN KEY ("lesson_id") REFERENCES Lessons ("id")
) STRICT;

CREATE TABLE Certificates (
   "id" TEXT PRIMARY KEY,
   "user_id" INTEGER NOT NULL,
   "course_id" INTEGER NOT NULL,
   "completed" TEXT DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY ("user_id") REFERENCES Users ("id")
      ON DELETE CASCADE,
   FOREIGN KEY ("course_id") REFERENCES Courses ("id"),
   UNIQUE ("user_id", "course_id")
) STRICT;


   