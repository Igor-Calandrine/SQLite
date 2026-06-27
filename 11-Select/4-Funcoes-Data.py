"""
-Funções Principais Data/Hora
   O SQLite possui um conjunto de funções específicas para manipular datas e horários, permitindo obter a data atual, calcular intervalos de tempo, extrair partes de uma data e formatar datas de acordo com diferentes necessidades. Essas funções são amplamente utilizadas em sistemas que registram evento, controlam prazos, armazenam datas de cadastro e realizam consultas baseadas no tempo.
   As funções mais utilizadas são:
   
   *DATE()
   Retorna apena a data no formato AAAA-MM-DD. Também pode ser utilizada para realizar operações, como adicionar ou subtrair dias.

   *TIME()
   Retorna apenas o horário no formato HH:MM:SS. Ela pode obter a hora atual do sistema ou extrair a parte correspondente ao horário de uma data e hora completas.

   *DATETIME()
   Retorna uma data e um horário completos no formato AAAA-MM-DD HH:MM:SS. Ela é bastante utilizada para registrar datas de cadastros, pedidos, acessos ao sistema e outras informações que necessitam armazenar tanto a data quanto o horário.

   *STRFTIME()
   É uma função para a minupulação de datas e horários. Ela permite formatar datas utilizando códigos específicos, possibilitando extrair apenas determinadas partes da data ou exibi-la em diferentes formatos.

   Entre os códigos de formataçao utilizados pela função temos:
      %Y - ano com 4 dígitos
      %m - mês
      %d - dia
      %H - hora
      %m - minutos
      %s - segundos


"""