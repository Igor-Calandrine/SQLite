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

CREATE TABLE Turma_3A (
   "id" INTEGER PRIMARY KEY,
   "nome" TEXT NOT NULL,
   "1_B" INTEGER CHECK ("1_B" BETWEEN 0 AND 25),
   "2_B" INTEGER CHECK ("2_B" BETWEEN 0 AND 25),
   "3_B" INTEGER CHECK ("3_B" BETWEEN 0 AND 25),
   "4_B" INTEGER CHECK ("4_B" BETWEEN 0 AND 25),
   "Total" INTEGER
      GENERATED ALWAYS AS (
      COALESCE("1_B", 0) + 
      COALESCE("2_B", 0) + 
      COALESCE("3_B", 0) + 
      COALESCE("4_B", 0)
      ) STORED,
   "Resultado" TEXT
      GENERATED ALWAYS AS (
         CASE
            WHEN "Total" < 60 THEN 'Recuperacao'
            WHEN "Total" >= 60 THEN 'Aprovado'
         END
      ) STORED
) STRICT;

DROP TABLE Turma_3A;

CREATE TABLE Turma_3A (
   "id" INTEGER PRIMARY KEY,
   "nome" TEXT NOT NULL
) STRICT;

CREATE TABLE Turma_3A_1B (
   "id_nome" INTEGER PRIMARY KEY,
   "Av_1" INTEGER CHECK ("Av_1" BETWEEN 0 AND 8),
   "Av_2" INTEGER CHECK ("Av_2" BETWEEN 0 AND 7),
   "Tr_1" INTEGER CHECK ("Tr_1" BETWEEN 0 AND 5),
   "Tr_2" INTEGER CHECK ("Tr_2" BETWEEN 0 AND 5),
   "Total" INTEGER CHECK ("Total" BETWEEN 0 AND 25)
      GENERATED ALWAYS AS (COALESCE("Av_1", 0) + COALESCE("Av_2", 0) + COALESCE("Tr_1", 0) + COALESCE("Tr_2", 0)) STORED,
   "Recuperacao" INTEGER,
   FOREIGN KEY ("id_nome") REFERENCES Turma_3A ("id")
) STRICT;

DROP TABLE Turma_3A_1B;

CREATE TABLE Turma_3A_2B (
   "id_nome" INTEGER PRIMARY KEY,
   "Av_1" INTEGER CHECK ("Av_1" BETWEEN 0 AND 8),
   "Av_2" INTEGER CHECK ("Av_2" BETWEEN 0 AND 7),
   "Tr_1" INTEGER CHECK ("Tr_1" BETWEEN 0 AND 5),
   "Tr_2" INTEGER CHECK ("Tr_2" BETWEEN 0 AND 5),
   "Total" INTEGER CHECK ("Total" BETWEEN 0 AND 25)
      GENERATED ALWAYS AS (COALESCE("Av_1", 0) + COALESCE("Av_2", 0) + COALESCE("Tr_1", 0) + COALESCE("Tr_2", 0)) STORED,
   "Recuperacao" INTEGER,
   FOREIGN KEY ("id_nome") REFERENCES Turma_3A ("id")
) STRICT;

CREATE TABLE Turma_3A_3B (
   "id_nome" INTEGER PRIMARY KEY,
   "Av_1" INTEGER CHECK ("Av_1" BETWEEN 0 AND 8),
   "Av_2" INTEGER CHECK ("Av_2" BETWEEN 0 AND 7),
   "Tr_1" INTEGER CHECK ("Tr_1" BETWEEN 0 AND 5),
   "Tr_2" INTEGER CHECK ("Tr_2" BETWEEN 0 AND 5),
   "Total" INTEGER CHECK ("Total" BETWEEN 0 AND 25)
      GENERATED ALWAYS AS (COALESCE("Av_1", 0) + COALESCE("Av_2", 0) + COALESCE("Tr_1", 0) + COALESCE("Tr_2", 0)) STORED,
   "Recuperacao" INTEGER,
   FOREIGN KEY ("id_nome") REFERENCES Turma_3A ("id")
) STRICT;

CREATE TABLE Turma_3A_4B (
   "id_nome" INTEGER PRIMARY KEY,
   "Av_1" INTEGER CHECK ("Av_1" BETWEEN 0 AND 8),
   "Av_2" INTEGER CHECK ("Av_2" BETWEEN 0 AND 7),
   "Tr_1" INTEGER CHECK ("Tr_1" BETWEEN 0 AND 5),
   "Tr_2" INTEGER CHECK ("Tr_2" BETWEEN 0 AND 5),
   "Total" INTEGER CHECK ("Total" BETWEEN 0 AND 25)
      GENERATED ALWAYS AS (COALESCE("Av_1", 0) + COALESCE("Av_2", 0) + COALESCE("Tr_1", 0) + COALESCE("Tr_2", 0)) STORED,
   "Recuperacao" INTEGER,
   FOREIGN KEY ("id_nome") REFERENCES Turma_3A ("id")
) STRICT;









