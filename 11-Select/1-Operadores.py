"""
-Operadores
   Alguns operadoradores já conhecidos através de outros estudos, estão presentes e pode ser usados de diferças formas, como em uso de Datas e Textos:

*      = -------- Igual
*      != ou <> - Diferente
*      < -------- Menor
*      > -------- Maior
*      <= ------- Menor ou Igual
*      >= ------- Maior ou Igual

-Is/Is Not
   Quando um campo possui o valor NULL, comparações utilizando = ou != não retornam o resultaado esperado, pois o valor nulo representa a ausência de informaçao. Nesses casos, deve-se utilizar os operadores IS e IS NOT. 
   O uso correto de IS e IS NOT torna as consultas mais precisas e evita erros de interpretação dos dados armazenados no banco. Por isso, esses operadores são fundamentais para o tratamento adquado de valores nulos em banco de dados SQLite.
   Como exemplo temos:

*     SELECT * FROM clientes WHERE telefone IS NOT NULL;

   Os operadores também podem ser utilizados para comparar valores booleanos ou expressões específicas, embora seu uso seja mais comum em verificações envolvendo NULL.

-Like/Not Like
   O operador LIKE é utilizado para realizar buscas por padrões em campos do tipo texto. Ele permite localizar registros que contenham determinadas palavras, letras ou sequências de caracteres, sendo muito útil em pesquisas flexíveis dentro de um banco de dados, e quando usamos NOT LIKE estaremos exlcuindo um determiando padrão das pesquisas.
   O funcionamento do LIKE baseia-se no uso de caracteres curinga (wildcards), que representam partes variáveis de uma string. Os principais curingas são:

*   % -> representa zero, um ou vários caracteres
*   _ -> representa exatamente um único caractere.

   Por exemplo, queremos encontrar todos os clientes cujo nome começa com a letra "A", pode-se utilizar a seguinte consulta:

*     SELECT * FROM clientes WHERE nome LIKE 'A%';

   Podemos buscar todos os clientes que terminam seu nome com a letra "A"

*     SELECT * FROM clientes WHERE nome LIKE '%a'; 

   Podemos buscar todos os clientes que tenham um determinado sobrenome

*     SELECT * FROM clientes WHERE nome LIKE '%Silva%'; 

      Podemos buscar todos os clientes que tenham apenas 2 caracteres após seu sua letra inicial

*     SELECT * FROM clientes WHERE nome LIKE 'A__'; 

-Betwenn/Not Betwenn
   Os operadores BETWEEN e IN são recursos muito utilizados no SQLite para simplificar consultas e tornar o código mais legível. Eles permitem realizar filtragens de dados de forma prática, evitando a necessidade de múltiplas comparações em uma mesma condição.

   O operador BETWEEN é utilizado para verificar se um valor está dentro de um intervalo específico. Esse intervalo inclui os valores inicial e final informados na consulta. É frequentemente empregado em pesquisas por datas, preços, idade ou qualquer outro dado numérico. Ex:

*     SELECT * FROM produtos WHERE preco BETWEEN  50 and 100;

-In/Not In
   O operador é utilizado para verificar se um valor pertence a uma lista de opções previamente definidas. Ele substitui várias comparações utilizando o operador OR, tornando a consulta mais simples e fácil de entender. Ex:

*     SELECT * FROM clientes WHERE cidade IN ('Belém', 'Manaus', 'São Luíz');




 

"""