-- Atalho para reduzir o calculo
WITH notas AS (
   SELECT COALESCE("Turma_3A_1B"."Av_1", 0) + COALESCE("Turma_3A_1B"."Av_2", 0) +
          COALESCE("Turma_3A_1B"."Tr_1", 0) + COALESCE("Turma_3A_1B"."Tr_2", 0)
          AS Total
   FROM Turma_3A_1B)

-- Alunos da Turma 3A
SELECT * FROM Turma_3A;

-- Todas Notas da turma 3A - 1ºBimestre
CREATE VIEW "todas_notas_3A_1B" AS 
SELECT "Turma_3A"."id" AS 'n',
       "Turma_3A"."nome" ,
       "Turma_3A_1B"."Av_1" AS 'Av1',
       "Turma_3A_1B"."Av_2" AS 'Av2',
       "Turma_3A_1B"."Tr_1" AS 'Tr1',
       "Turma_3A_1B"."Tr_2" AS 'Tr2',
       "Total",
      CASE
         WHEN 
         COALESCE("Turma_3A_1B"."Av_1", 0) + COALESCE("Turma_3A_1B"."Av_2", 0) +
         COALESCE("Turma_3A_1B"."Tr_1", 0) + COALESCE("Turma_3A_1B"."Tr_2", 0)
         < 15 THEN 'Recuperacao'     
            ELSE '--'
      END AS Recp,
      CASE 
         WHEN "Turma_3A_1B"."Recuperacao" IS NULL THEN '--'
         ELSE "Turma_3A_1B"."Recuperacao"
      END 
      AS 'AvR',
      CASE
         WHEN 
         "Turma_3A_1B"."Recuperacao" IS NOT NULL
         AND
         (
         COALESCE("Turma_3A_1B"."Av_1", 0) + COALESCE("Turma_3A_1B"."Av_2", 0) +
         COALESCE("Turma_3A_1B"."Tr_1", 0) + COALESCE("Turma_3A_1B"."Tr_2", 0) +
         COALESCE("Turma_3A_1B"."Recuperacao", 0) >= 15
         )
         THEN 15
         ELSE 
         COALESCE("Turma_3A_1B"."Av_1", 0) + COALESCE("Turma_3A_1B"."Av_2", 0) +
         COALESCE("Turma_3A_1B"."Tr_1", 0) + COALESCE("Turma_3A_1B"."Tr_2", 0) +
         COALESCE("Turma_3A_1B"."Recuperacao", 0)
      END
      AS 'TotR'
FROM "Turma_3A"
JOIN "Turma_3A_1B"
ON "Turma_3A"."id" = "Turma_3A_1B"."id_nome";

-- Todas Notas da turma 3A - 2ºBimestre
DROP VIEW "todas_notas_3A_2B";
CREATE VIEW "todas_notas_3A_2B" AS 
SELECT "Turma_3A"."id" AS 'n',
       "Turma_3A"."nome" ,
       "Notas_3A"."Av_1" AS 'Av1',
       "Notas_3A"."Av_2" AS 'Av2',
       "Notas_3A"."Tr_1" AS 'Tr1',
       "Notas_3A"."Tr_2" AS 'Tr2',
       "Total",
      CASE
         WHEN 
         COALESCE("Notas_3A"."Av_1", 0) + COALESCE("Notas_3A"."Av_2", 0) +
         COALESCE("Notas_3A"."Tr_1", 0) + COALESCE("Notas_3A"."Tr_2", 0)
         < 15 THEN 'Recuperacao'     
            ELSE '--'
      END AS Recp,
      CASE 
         WHEN "Notas_3A"."Recuperacao" IS NULL THEN '--'
         ELSE "Notas_3A"."Recuperacao"
      END 
      AS 'AvR',
      CASE
         WHEN 
         "Notas_3A"."Recuperacao" IS NOT NULL
         AND
         (
         COALESCE("Notas_3A"."Av_1", 0) + COALESCE("Notas_3A"."Av_2", 0) +
         COALESCE("Notas_3A"."Tr_1", 0) + COALESCE("Notas_3A"."Tr_2", 0) +
         COALESCE("Notas_3A"."Recuperacao", 0) >= 15
         )
         THEN 15
         ELSE 
         COALESCE("Notas_3A"."Av_1", 0) + COALESCE("Notas_3A"."Av_2", 0) +
         COALESCE("Notas_3A"."Tr_1", 0) + COALESCE("Notas_3A"."Tr_2", 0) +
         COALESCE("Notas_3A"."Recuperacao", 0)
      END
      AS 'TotR'
FROM "Turma_3A"
JOIN "Turma_3A_2B" AS "Notas_3A"
ON "Turma_3A"."id" = "Notas_3A"."id_nome";

-- Todas Notas da turma 3A - 3ºBimestre
CREATE VIEW "todas_notas_3A_3B" AS 
SELECT "Turma_3A"."id" AS 'n',
       "Turma_3A"."nome" ,
       "Notas_3A"."Av_1" AS 'Av1',
       "Notas_3A"."Av_2" AS 'Av2',
       "Notas_3A"."Tr_1" AS 'Tr1',
       "Notas_3A"."Tr_2" AS 'Tr2',
       "Total",
      CASE
         WHEN 
         COALESCE("Notas_3A"."Av_1", 0) + COALESCE("Notas_3A"."Av_2", 0) +
         COALESCE("Notas_3A"."Tr_1", 0) + COALESCE("Notas_3A"."Tr_2", 0)
         < 15 THEN 'Recuperacao'     
            ELSE '--'
      END AS Recp,
      CASE 
         WHEN "Notas_3A"."Recuperacao" IS NULL THEN '--'
         ELSE "Notas_3A"."Recuperacao"
      END 
      AS 'AvR',
      CASE
         WHEN 
         "Notas_3A"."Recuperacao" IS NOT NULL
         AND
         (
         COALESCE("Notas_3A"."Av_1", 0) + COALESCE("Notas_3A"."Av_2", 0) +
         COALESCE("Notas_3A"."Tr_1", 0) + COALESCE("Notas_3A"."Tr_2", 0) +
         COALESCE("Notas_3A"."Recuperacao", 0) >= 15
         )
         THEN 15
         ELSE 
         COALESCE("Notas_3A"."Av_1", 0) + COALESCE("Notas_3A"."Av_2", 0) +
         COALESCE("Notas_3A"."Tr_1", 0) + COALESCE("Notas_3A"."Tr_2", 0) +
         COALESCE("Notas_3A"."Recuperacao", 0)
      END
      AS 'TotR'
FROM "Turma_3A"
JOIN "Turma_3A_3B" AS "Notas_3A"
ON "Turma_3A"."id" = "Notas_3A"."id_nome";

-- Todas Notas da turma 3A - 4ºBimestre
CREATE VIEW "todas_notas_3A_4B" AS 
SELECT "Turma_3A"."id" AS 'n',
       "Turma_3A"."nome" ,
       "Notas_3A"."Av_1" AS 'Av1',
       "Notas_3A"."Av_2" AS 'Av2',
       "Notas_3A"."Tr_1" AS 'Tr1',
       "Notas_3A"."Tr_2" AS 'Tr2',
       "Total",
      CASE
         WHEN 
         COALESCE("Notas_3A"."Av_1", 0) + COALESCE("Notas_3A"."Av_2", 0) +
         COALESCE("Notas_3A"."Tr_1", 0) + COALESCE("Notas_3A"."Tr_2", 0)
         < 15 THEN 'Recuperacao'     
            ELSE '--'
      END AS Recp,
      CASE 
         WHEN "Notas_3A"."Recuperacao" IS NULL THEN '--'
         ELSE "Notas_3A"."Recuperacao"
      END 
      AS 'AvR',
      CASE
         WHEN 
         "Notas_3A"."Recuperacao" IS NOT NULL
         AND
         (
         COALESCE("Notas_3A"."Av_1", 0) + COALESCE("Notas_3A"."Av_2", 0) +
         COALESCE("Notas_3A"."Tr_1", 0) + COALESCE("Notas_3A"."Tr_2", 0) +
         COALESCE("Notas_3A"."Recuperacao", 0) >= 15
         )
         THEN 15
         ELSE 
         COALESCE("Notas_3A"."Av_1", 0) + COALESCE("Notas_3A"."Av_2", 0) +
         COALESCE("Notas_3A"."Tr_1", 0) + COALESCE("Notas_3A"."Tr_2", 0) +
         COALESCE("Notas_3A"."Recuperacao", 0)
      END
      AS 'TotR'
FROM "Turma_3A"
JOIN "Turma_3A_4B" AS "Notas_3A"
ON "Turma_3A"."id" = "Notas_3A"."id_nome";

-- Apenas alunos de recuperação 1º Bimestre
CREATE VIEW "alunos_rec_3A_1B" AS
SELECT "id" AS 'n', 
       "nome",
       COALESCE("Rec_Notas"."Av_1", 0) + COALESCE("Rec_Notas"."Av_2", 0) +
       COALESCE("Rec_Notas"."Tr_1", 0) + COALESCE("Rec_Notas"."Tr_2", 0)
       AS Total,
       CASE
            WHEN 
            COALESCE("Rec_Notas"."Av_1", 0) + COALESCE("Rec_Notas"."Av_2", 0) +
            COALESCE("Rec_Notas"."Tr_1", 0) + COALESCE("Rec_Notas"."Tr_2", 0)
            < 15 THEN 'Recuperacao'     
               ELSE '--'
       END AS Recp
FROM "Turma_3A"
JOIN "Turma_3A_1B" AS "Rec_Notas"
ON "Turma_3A"."id" = "Rec_Notas"."id_nome"
WHERE Recp = 'Recuperacao';

-- Apenas alunos de recuperação 2º Bimestre
CREATE VIEW "alunos_rec_3A_2B" AS
SELECT "id" AS 'n', 
       "nome",
       COALESCE("Rec_Notas"."Av_1", 0) + COALESCE("Rec_Notas"."Av_2", 0) +
       COALESCE("Rec_Notas"."Tr_1", 0) + COALESCE("Rec_Notas"."Tr_2", 0)
       AS Total,
       CASE
            WHEN 
            COALESCE("Rec_Notas"."Av_1", 0) + COALESCE("Rec_Notas"."Av_2", 0) +
            COALESCE("Rec_Notas"."Tr_1", 0) + COALESCE("Rec_Notas"."Tr_2", 0)
            < 15 THEN 'Recuperacao'     
               ELSE '--'
       END AS Recp
FROM "Turma_3A"
JOIN "Turma_3A_2B" AS "Rec_Notas"
ON "Turma_3A"."id" = "Rec_Notas"."id_nome"
WHERE Recp = 'Recuperacao';

-- Apenas alunos de recuperação 3º Bimestre
CREATE VIEW "alunos_rec_3A_3B" AS
SELECT "id" AS 'n', 
       "nome",
       COALESCE("Rec_Notas"."Av_1", 0) + COALESCE("Rec_Notas"."Av_2", 0) +
       COALESCE("Rec_Notas"."Tr_1", 0) + COALESCE("Rec_Notas"."Tr_2", 0)
       AS Total,
       CASE
            WHEN 
            COALESCE("Rec_Notas"."Av_1", 0) + COALESCE("Rec_Notas"."Av_2", 0) +
            COALESCE("Rec_Notas"."Tr_1", 0) + COALESCE("Rec_Notas"."Tr_2", 0)
            < 15 THEN 'Recuperacao'     
               ELSE '--'
       END AS Recp
FROM "Turma_3A"
JOIN "Turma_3A_3B" AS "Rec_Notas"
ON "Turma_3A"."id" = "Rec_Notas"."id_nome"
WHERE Recp = 'Recuperacao';

-- Apenas alunos de recuperação 4º Bimestre
CREATE VIEW "alunos_rec_3A_4B" AS
SELECT "id" AS 'n', 
       "nome",
       COALESCE("Rec_Notas"."Av_1", 0) + COALESCE("Rec_Notas"."Av_2", 0) +
       COALESCE("Rec_Notas"."Tr_1", 0) + COALESCE("Rec_Notas"."Tr_2", 0)
       AS Total,
       CASE
            WHEN 
            COALESCE("Rec_Notas"."Av_1", 0) + COALESCE("Rec_Notas"."Av_2", 0) +
            COALESCE("Rec_Notas"."Tr_1", 0) + COALESCE("Rec_Notas"."Tr_2", 0)
            < 15 THEN 'Recuperacao'     
               ELSE '--'
       END AS Recp
FROM "Turma_3A"
JOIN "Turma_3A_4B" AS "Rec_Notas"
ON "Turma_3A"."id" = "Rec_Notas"."id_nome"
WHERE Recp = 'Recuperacao';

CREATE VIEW resultado_final_anual AS
SELECT "id" AS 'n',
       "nome",
       "Notas1B"."Total" AS "1B",
       "Notas2B"."Total" AS "2B",
       "Notas3B"."Total" AS "3B",
       "Notas4B"."Total" AS "4B",
       COALESCE("Notas1B"."Total", 0) + COALESCE("Notas2B"."Total", 0) + COALESCE("Notas3B"."Total", 0) + COALESCE("Notas4B"."Total", 0) AS "Total",
       CASE
         WHEN COALESCE("Notas1B"."Total", 0) + COALESCE("Notas2B"."Total", 0) + COALESCE("Notas3B"."Total", 0) + COALESCE("Notas4B"."Total", 0) >= 60
         THEN 'Aprovado'
         ELSE 'Recuperacao'
       END AS "Resultado"

FROM "Turma_3A" 
-- 1º Bimestre
JOIN "Turma_3A_1B" AS "Notas1B"
ON "Turma_3A"."id" = "Notas1B"."id_nome" 
-- 2º Bimestre
JOIN "Turma_3A_2B" AS "Notas2B"
ON "Turma_3A"."id" = "Notas2B"."id_nome"
-- 3º Bimestre
JOIN "Turma_3A_3B" AS "Notas3B"
ON "Turma_3A"."id" = "Notas3B"."id_nome"
-- 4º Bimestre
JOIN "Turma_3A_4B" AS "Notas4B"
ON "Turma_3A"."id" = "Notas4B"."id_nome"; 



-- Média da Turma
SELECT AVG("Av_1") AS 'Av1M',
       AVG("Av_2") AS 'Av2M'
FROM "Turma_3A_1B";

-- Todas as notas da Turma 3A por Bimesre
SELECT * FROM "todas_notas_3A_1B";
SELECT * FROM "todas_notas_3A_2B";
SELECT * FROM "todas_notas_3A_3B";
SELECT * FROM "todas_notas_3A_4B";

-- Todos de recuperação Bimestral
SELECT * FROM "alunos_rec_3A_1B";
SELECT * FROM "alunos_rec_3A_2B";
SELECT * FROM "alunos_rec_3A_3B";
SELECT * FROM "alunos_rec_3A_4B";

-- Resultado Final Antes da Recuperação Final
SELECT * FROM resultado_final_anual;

-- Todos de recuperação Final
SELECT * FROM resultado_final_anual
WHERE "Total" < 60;







