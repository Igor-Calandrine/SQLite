"""
-Tipo de Dados
   O SQLite funciona de forma diferente dos outros banco de dados. Ele usa uma sistema chamado tipagem dinâmica, o que significa que o tipo é um sugestão ao banco, não uma regra rígida. Ele se resume a 6 tipos de armazenamentos.

   *INTEGER
      Armazena números inteiros, positivos ou negativos, sem casas decimais

   *REAL
      Armazena números com casas decimais, usando ponto flutuante

   *TEXT
      Armazena qualquer texto, de qualquer tamanho

   *BLOB
      Armazena dados binários exatamente como foram inseridos, sem nanhuma conversão

   *NULL
      Representa a ausência de valor. Toda coluna pode conter NULL. Você pode restringir a possibilidade com NOT NULL

   *NUMERIC
      Uma coluna esse tipo pode assumir mais de um tipo de dados, ela vai tentar transformar se possível para INTEGER, caso não seja possível, ele será do tipo TEXT. Ex:
       100    -> INTEGER
      '100'   -> INTEGER
      'R$100' -> INTEGER

-Problemas com NUMERIC
   Quando você usa o comportamento dinâmico que o NUMERIC proporciona, você pode causar problemas críticos.

   *Inconsistência crítica
      Se o seu código backend espera receber apenas números para fazer cálculos (como méida de idade), o sistemas vai quebrar ou retornar erros quando encontrar um texto perdido no banco de dados.

   *Comparações Bizarras
      O SQLite compara texto e números de forma diferente, se você fizer uma buscas como:
      WHERE idade > 20
      o texto é condiderado maior que qualquer número

   *Falta de erros no momento certo
      Em outros banco de dados, se o seu aplicativo tentar salvar um texto inválido em uma coluna numérica, o banco rejeita na hora. No SQLite padrão, ele aceita em silêncio. Você só vai descobrir o erro meses depois, quando o relatório falhar.

   Mais adiante falaremos sobre o modo STRICT para resolver esse tipo de problema.
      



"""