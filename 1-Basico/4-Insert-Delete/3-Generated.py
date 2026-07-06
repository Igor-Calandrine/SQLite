"""
-Generated Columns
   São um recurso do SQLite que permite criar colunas cujos valores são calculados automaticamente a partir de uma expressão baseada em outras colunas da mesma tabela. Em vez de armazenar um valor informado pelo usuário ou pela aplicação, a coluna gerada tem seu conteúdo definido por uma expressão especificada no momento da criação da tabela.

   O principal objetivo das Colunas Geradas é evitar a duplicação de informações e garantir que determinados valores permaneçam sempre consistentes com os dados que lhes dão origem. Como o valor é calculado automaticamente pelo SQLite, não há risco de inconsistências causadas por atualizações manuais incorretas.

   A expressão utilizada para definir uma Coluna Gerada pode realizar operações aritiméticas, concatenações de textos, chamadas de funções determinísticas do SQLite e outras expressões válidas. Entretanto, ela deve depender apenas de colunas da própria linhas e não pode utilizar subconsultas, funções não determinísticas ou referências a outras tabelas.

   O SQLite oferece dois tipos de Colunas Geradas:

   *VIRTUAL
      Não ocupada espaço físico para armazenar seus valores, pois eles são calculados toda vez que a colunas é consultada

   *STORED
      Tem seus valores calculados no momento da inserção ou atualização da linha e armazenados fisicamente na tabela, permitindo consultas mais rápidas ao custo de utilizar espaço em disco.

   Esse recurso é especialmente útil para representar informações derivadas, como o nome completo obtido pela concatenação do nome e sobrenome, o valor total de um produto calculado a partir da quantidade e do preço unitário, a idade aproximada calculada a partir da data de nascimento ou qualquer outro dado que possa ser obtido diretamente de outras colunas da mesma linha.
   Sua sintaxe é:

*   nome_coluna TIPO GENERATED ALWAYS AS expressão VIRTUAL

*   nome_coluna TIPO GENERATED ALWAYS AS expressão STORED
"""   