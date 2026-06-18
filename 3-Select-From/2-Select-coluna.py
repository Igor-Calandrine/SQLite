"""
-Especificando uma coluna
   Em banco de dados reais, as tabelas podem ter dezenas de colunas, trazer tudo isso gasta memória e deixa a consulta lenta.
   Para resolver isso, nós especificamos as colunas separando seus nomes por vírgula logo após a palavras SELECT:

*     SELECT coluna1, coluna2 FROM  nome_da_tabela

-Limit
   O LIMIT é uma cláusala deo SQL que serve exatamente para o que o nome diz: limitar a quantidade de linhas que o banco de dados vai te devolver no resultado de uma consulta com o SELECT.
   Se você tem uma tabela com 1 milhão de usuários, mas só precisa olhar para os 5 primeiros na tela, o LIMIT impede que o banco gaste memória desnecessária trazendo o resto e deixando o sistema lento.
   Ele é sempre colocado no final do seu comando SELECT como no exemplo abaixo:

*     SELECT coluna1, coluna2 FROM nome_da_tabela LIMIT quantidade_de_linhas


"""