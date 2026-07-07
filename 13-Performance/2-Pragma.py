"""
-Pragma
   O PRAGMA é um conjunto de comandos especiais do SQLite utilizado para consultar ou modificar configurações interna de dados e do ambiente de execução. Diferentemente dos comandos tradicionais da linguagem SQL, como SELECT, INSERT, UPDATE, DELETE, os comandos PRAGMA não manipual diretamente os dados armazenados nas tabelas. Seu objetivo é controlar o funcionamento do SQLite, fornecer informações sobre a estrutura do banco de dados e ajustar diversos aspectos relacionados ao desempenho, integridade e comportamento da conexão.

   A palavra PRAGMA significa de forma geral, uma diretiva ou instrução especial. NO SQLite, ela representa comandos próprios do sistema de gerenciamneto de banco de dados que permitem acessar funcionalidadesespecíficas que não fazem parte do padrão SQL. Por esse motivo, embora vários BDs posssuam mecanismos semelhantes, os comandos PRAGMA são uma característica específica do SQLite

   OS comandos PRAGMA podem ser utilizados tanto para consultar informações quanto para alterar configurações. Alguns deles retornam dados, funcionando de maneira semelhante a uma consulta SELECT, enquanto outros modificam parÂmetros internos do BD ou da conexão atual. Em muitos casos, as alterações realizadas por um PRAGMA permanecem válidas apenas durante a conexão aberta com o BD. Em outros casos, a configuração é gravada permanentemente no próprie arquivo do banco, permanecendo ativa mesmo após seu fechamento.

-  PRAGMA foreign_keys = ON;
   Já conhecido e utilizado, permite verificar se a chave entrangeira está habilitada ou não, também possibilita alterar esse comportamento.
   Quando o recurso está habilitado, o SQLite valida automaticamente todas as operações que envolvem chaves entrangeiras. Isso significa que um registro não poderá ser inserido com um referência inválida, nem será possível excluir ou alterar um registro que esteja sendo referenciado por outra tabela, exceto quando houver regras específicias como CASCADE, SET NULL, ou SET DEFAULT.

-  PRAGMA journal_mode;
   É utilizado para alterar o modo como o SQLite registra e protege as alterações realizadas no BD; O termo significa Write-Ahead Logging, um mecanismo que melhora o desempenho e a concorrência em comparação com o modo tradional de gravação.

*  PRAGMA journal_mode = DELETE;
   No modo padrão, o SQLite cria um arquivo temporário conhecido como #rollback journal. Antes de modificar o BD, as informações originais são copiadas para esse arquivo. Caso ocorra algum problema durante a transação, o SQLite utiliza esse arrquivo para restaurar o banco ao seu estado anterior. Após a conclusão bem sucedida da operação, o arquivo é removido.

*  PRAGMA journal_mode = WAL;
   No modo WAL, em vez de modificar diretamente o arquivo principal do BD, o SQLite grava inicialmente todas as alterações em um arquivo separado com extensão .wal. Somente posteriormente essas alterações são incorporadas ao BD principal por meio de um processo chamado #checkpoint. Dessa forma, o arquivo principal permanece disponível para leitura em múltiplas operações enquanto novas alterações continuam sendo registradas no arquivo WAL.

   É importante destacar que a configuração é armazenada no próprio BD. Assim, após defnir o modo WAL, esse configuração permanece ativa nas próximas conexões, até que seja alterada novamente para outro modo (DELETE - Padrão).

-  PRAGMA synchronous;
   O comando é utilizado para controlar o nível de sincoronização entre o SQLite e os dispositivo de armazenamento durante a gravação de dados. 

*  PRAGMA synchronous = FULL;
   É o nível de sincronização utilizado por padrão. NEsse modo o BD realiza todas as sincornizações necessárias para garantir que os dados tenham sido efetivamente gravados no dispositivo de armazenamento antes da confirmação da transação. Isso reduz significativamente a possibilidade de perda de dados causada por falhas inesperadas, embora com um pequeno impacto no desempenho das gravações

*  PRAGMA synchronous = NORMAL;
   Realiza apenas as sincrinizações consideradas essenciais, reduzindo número de acesso ao disco e proporcionando um bom equilíbrio entre desempenho e segurança. Esse modo é alplamente utilizado em conjunto com o #PRAGMA journal_mode = WAL; sendo recomendado para a grande parte das aplicações modernas.

*  PRAGMA synchronous = EXTRA;
   O modo oferece o mais alto nível de proteção disponível, além das sincronizações realizadas pelo modo FULL, ele executa verificações adicionais em determinadas operações para reduzir ainda mais a possibilidade de corrupção do BD em situações extremamente raras. Em contrapartida, esse nível aumenta o custo das operações de escrita, por isso é utilizado apenas em aplicações que exigem o máximo possível confiabilidade e integridade dos dados.

-PRAGMA cache_size = XXXX;
   É utilizado para definir o tamanho do cache de páginas utilizadp pelo SQLite durante o acesso ao BD. Esse cache é uma área de mamória RAM onde o SQLite mantém temporariamente as páginas do banco que foram lidas ou modificadas reduzindo a necessidade de acessar o disco repedidamente e melhorando o desempenho das operações.

   O SQLite organiza os dados em blocos chamados páginas. Sempre que uma consulta ou atualização precisa acessar uma informação, o banco carrega a páginas correspondente para a memória. Se essa páginas permanecer no cache, futuras operações poderão reutilizá-la sem a necessidade de uma nova leitura no disco, tornando as consultas e gravações mais rápidas.

*   PRAGMA cache_size = 2000;

   O SQLite passa a utilizar um cache capaz de armazenar até 2.000 páginas de dados. Como o tamanho de cada página depende da configuração do banco de dados (geralmente 4 KB), o espaço efetivamente utilizado pelo cache varia conforme o tamanho definido para as páginas.

   O valor configurado por meio de PRAGMA cache_size é aplicado apenas à conexão atual com o banco de dados. Isso significa que, ao abrir uma nova conexão, será necessário configurar novamente o tamanho do cache, caso a aplicação deseje utilizar um valor diferente do padrão.

-PRAGMA busy_timeout
   É utilizado para definir por quanto tempo o SQLite deve aguardar quando um banco estiver temporariamente bloqueado por outra conexão. Em vez de retornar imediatamente um erro informando que o banco está ocupado, o SQLite continua tentando obter acesso até que o tempo configurado seja atingido.

   O SQLite utiliza mecanismos de bloqueio para garantir a integridade dos dados durante operações de escrita. Quando uma conexão está realizando uma transação que exige acesso exclusivo ao BD, outras conexões podem precisar aguardar até que esse bloqueio seja liberado. Sem um tempo de espera configurado, o SQLite retorna imadiatamente um erro indicando que o banco está ocupado (database is locked).

*   PRAGMA busy_timeout = 5000;

   O SQLite aguardará até 5 segundos para que o bloqueio seja liberado. Caso a outra conexão conclua sua operação dentro desse intervalo, a instrução será executada normalmente.
   É importante observar que busy_timeout não elimina os bloqueios nem permite que duas conexões escrevam no banco de dados ao mesmo tempo. Ele apenas determina quanto tempo uma conexão deve esperar antes de desistir da operação. Caso o bloqueio persista além do tempo configurado, a operação continuará falhando.

   A configuração de busy_timeout é válida apenas para a conexão atual com o banco de dados. Sempre que uma nova conexão for aberta, será necessário configurar novamente esse tempo de espera, caso a aplicação deseje utilizá-lo.

-Pragma temp_store
   O comando PRAGMA temp_store é utilizado para definir onde o SQLite armazenará os objetos temporários criados durante a execução de consultas e outras operações. Esses objetos podem incluir tabelas temporárias, índices temporários, resultados intermediários de ordenações (ORDER BY), agrupamentos (GROUP BY), operações de junção (JOIN) e outras estruturas que o SQLite cria internamente para processar uma consulta.

   *PRAGMA temp_store = MEMORY;
   O SQLite passa a armazenar esses objetos temporários na memória RAM, em vez de gravá-los em arquivos temporários no disco. Como o acesso à memória é muito mais rápido do que ao armazenamento físico, essa configuração pode melhorar o desempenho de consultas que utilizam intensivamente estruturas temporárias.

   *PRAGMA temp_store = FILE;
   O modo FILE armazena os objetos temporários em arquivos no disco.

   *PRAGMA temp_store = DEFAULT;
   O modo DEFAULT faz com que o SQLite utilize a configuração definida no momento em que a biblioteca foi compilada.

   A configuração de temp_store é válida apenas para a conexão atual com o banco de dados, salvo quando a biblioteca SQLite é compilada com configurações específicas que definem um comportamento padrão diferente.

-Pragma analysis_limit
   Sempre que o comando é executado, o SQLite examina os índices existentes no banco de dados para coletar informações sobre a distribuição dos dados. Com base nessas estatísitcas, o otimizador consegue decidir, por exemplo, se é mais vantajoso utilizar um índice, realizar uma varredura completa na tabela, ou escolher entre índices disponíveis.

   *PRAGMA analysis_limit = 1000;

   Nesse caso termos uma análise de aproximadamente 1000 registros por índice durante a execução do comando. 
   Essa configuração é especialmente útil em bancos de dados muito grandes, onde analisar todos os registros de todos os índices pode consumir um tempo considerável. Ao limitar a quantidade de informações analisadas, torna-se possível atualizar as estatísticas com maior frequência, mantendo um bom equilíbrio entre desempenho e qualidade da otimização.

   O valor definido por analysis_limit é aplicado apenas à conexão atual com o banco de dados. Caso uma nova conexão seja aberta, essa configuração deverá ser definida novamente, se desejado.

-Pragma optimize;
   O comando PRAGMA optimize é utilizado para solicitar que o SQLite execute automaticamente algumas tarefas de otimização do banco de dados. Em vez de o desenvolvedor decidir manualmente quando executar comandos como ANALYZE ou outras rotinas de manutenção, o próprio SQLite verifica se existe alguma otimização realmente necessária e a realiza apenas quando isso for considerado útil.

   O comando também aceita um parâmetro numérico que funciona como uma máscara de bits (bitmask). Esse valor controla quais verificações e otimizações poderão ser executadas. Um dos valores mais utilizados é:

   *PRAGMA optimize = 0x10002;

   Entre essas opções está a permissão para que o SQLite considere tabelas e índices que ainda não foram utilizados pela conexão atual, permitindo uma análise mais abrangente durante a otimização. Essa configuração é especialmente útil quando uma aplicação acabou de abrir uma conexão com o banco de dados ou quando deseja realizar uma manutenção mais completa antes de encerrar sua execução.

   O comando PRAGMA optimize não reorganiza fisicamente o banco de dados nem substitui comandos como VACUUM. Seu foco é melhorar a qualidade das estatísticas utilizadas pelo Query Planner, permitindo que o SQLite escolha planos de execução mais eficientes para consultas futuras.

   Em versões mais recentes do SQLite, os próprios desenvolvedores recomendam utilizar PRAGMA optimize em vez de executar o comando ANALYZE manualmente na maioria dos casos. Isso ocorre porque o SQLite consegue determinar quais estatísticas realmente precisam ser atualizadas, evitando análises completas desnecessárias e reduzindo o custo de manutenção do banco de dados.

-Informações

   *PRAGMA pragma_list;
   Lista de comandos Pragma

   *PRAGMA table_list;
   Lista as tabelas

   *PRAGMA function_list;
   Lista as funções

   *PRAGMA page_size;
   Tamanho de cada página

   *PRAGMA page_count;
   Total de páginas





"""