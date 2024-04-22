# Investigando os efeitos das más práticas de integração contínua em projetos de software industriais

A prática da Integração Contínua (IC) é crucial para a eficiência dos processos de desenvolvimento de software, permitindo a integração frequente de código e a detecção precoce de erros. No entanto, sua má implementação pode resultar em más práticas que comprometem não apenas a eficácia da IC, mas também afetam a qualidade do produto final. Esta pesquisa se concentrou em identificar, compreender e mitigar os efeitos das más práticas de IC em projetos industriais. Ao investigar as más práticas mais comuns, constatamos que problemas como o uso inadequado de _feature branches_, _branches_ divergentes e a falta de controle do ambiente pelos desenvolvedores foram recorrentes. Estas más práticas geraram impactos adversos nos projetos industriais, afetando a estabilidade do código, aumentando o tempo e o custo de desenvolvimento, e diminuindo a produtividade das equipes. Quanto à qualidade do software, descobrimos que uma implementação adequada da IC teve efeitos positivos nos atributos internos de qualidade. Houve um aumento geral na coesão do código após a adoção da IC, indicando uma correlação positiva entre uma IC bem executada e uma melhoria na estrutura do código. No entanto, más práticas não resolvidas impactaram negativamente a qualidade do software ao longo do tempo, refletindo em indicadores de qualidade prejudicados e análise estática do código. Analisando a interação entre a IC e a Revisão de Código (RC), identificamos correlações significativas entre métricas de IC e vários aspectos da RC, como tempo de execução e tempo de revisão. Más práticas de IC, como divergências em _branches_ e testes inadequados, influenciaram adversamente a RC, aumentando a carga de trabalho dos revisores e atrasando a identificação e correção de problemas no código. Esses resultados sublinham a importância de implementar e manter práticas eficientes de IC para alcançar os benefícios desejados. Mitigar as más práticas de IC não apenas melhora a qualidade do produto final, mas também aumenta a satisfação das equipes de desenvolvimento e otimiza os processos de revisão e correção de código.

## Artefatos do primeiro estudo

| Artefato | Descrição |
| -------- | --------- |
| [Ocorrências das más práticas](estudo-1/bad-practices-occurrences.pdf) | Tabela de ocorrências das más práticas de IC |
| [Intervalos de correção de build](estudo-1/broken-build-fix-intervals.csv) | Valores brutos dos intervalos de correção de build |
| [Resumo dos intervalor de correção de build](estudo-1/broken-build-fix-intervals-summary.csv) | Métricas calculadas com base nos valores dos intervalos de correção de build |
| [Respostas do formulário](estudo-1/form-answers.csv) | Respostas do formulário direcionado aos integrantes dos projetos analisados |
| [Formulário](estudo-1/form-bad-practices-of-continuous-integration.pdf) | Perguntas direcionadas aos integrantes dos projetos analisados |
| [Visão ordenada das más práticas de IC](estudo-1/ordered-bad-practices-occurences.pdf) | Tabela com uma visão ordenada pela quantidade de ocorrências das más práticas de IC |
| [Script para coleta dos intervalos de correção de build](estudo-1/pipeline-api-tool.zip) | Código-fonte do script desenvolvido para coletar os valores dos intervalos de correção de build nos projetos analisados |

## Artefatos do segundo estudo

| Artefato  |  Descrição  |
| ------------------- | ------------------- |
|  [S1 - Antes do CI](estudo-2/s1-before-ci.csv) | Valores dos atributos internos de S1 antes da implementação do CI |
|  [S1 - Depois do CI](estudo-2/s1-after-ci.csv) | Valores dos atributos internos de S1 depois da implementação do CI |
|  [S2 - Antes do CI](estudo-2/s2-before-ci.csv) | Valores dos atributos internos de S2 antes da implementação do CI |
|  [S2 - Depois do CI](estudo-2/s2-after-ci.csv) | Valores dos atributos internos de S2 depois da implementação do CI |
|  [S4 - Antes do CI](estudo-2/s4-before-ci.csv) | Valores dos atributos internos de S4 antes da implementação do CI |
|  [S4 - Depois do CI](estudo-2/s4-after-ci.csv) | Valores dos atributos internos de S4 depois da implementação do CI |
|  [S6 - Antes do CI](estudo-2/s6-before-ci.csv) | Valores dos atributos internos de S6 antes da implementação do CI |
|  [S6 - Depois do CI](estudo-2/s6-after-ci.csv) | Valores dos atributos internos de S6 depois da implementação do CI |
|  [S8 - Antes do CI](estudo-2/s8-before-ci.csv) | Valores dos atributos internos de S8 antes da implementação do CI |
|  [S8 - Depois do CI](estudo-2/s8-after-ci.csv) | Valores dos atributos internos de S8 depois da implementação do CI |
|  [Arquivo Principal Python](estudo-2/main.py) | Arquivo principal do script Python para coleta dos indicadores de qualidade |
|  [Arquivo de Cálculo Python](estudo-2/calc.py) | Arquivo responsável pelo cálculo dos valores dos indicadores de qualidade |
|  [Respostas do Questionário](estudo-2/answers.csv) | Valores brutos das respostas dos membros das equipes de desenvolvimento dos sistemas analisados |
|  [Impacto nos Indicadores de Qualidade](estudo-2/quality-indicators-impact.csv) | Resumo da análise do impacto das más práticas de CI nos indicadores de qualidade |
|  [Dificuldade de Resolução](estudo-2/resolution-difficulty.csv) | Resumo da análise da dificuldade em resolver más práticas de CI |
|  [Impacto versus Dificuldade de Resolução](estudo-2/impact-vs-difficulty.csv) | Resumo da análise de priorização de resolução de más práticas de CI com base no impacto e na dificuldade de resolução |

## Artefatos do terceiro estudo

| Artefato                                  | Descrição                                                |
|-------------------------------------------|----------------------------------------------------------|
| [Mining tool](estudo-3/mining-tool.zip)  | Ferramenta utilizada para coletar as métricas de IC e RC |
| [Correlações](estudo-3/correlations.ods) | Dados gerais das correlações encontradas                 |
| [Grupo focal](estudo-3/focus-group.pdf)  | Dados da aplicação do grupo focal                        |
| [Dados gerais](estudo-3/general)         | Arquivos das métricas para todos os projetos             |
| [Dados do projeto 22](estudo-3/22)       | Arquivos das métricas para todos o projeto 22            |
| [Dados do projeto 26](estudo-3/26)       | Arquivos das métricas para todos o projeto 26            |
| [Dados do projeto 36](estudo-3/36)       | Arquivos das métricas para todos o projeto 36            |
| [Dados do projeto 39](estudo-3/39)       | Arquivos das métricas para todos o projeto 39            |
| [Dados do projeto 41](estudo-3/41)       | Arquivos das métricas para todos o projeto 41            |
| [Dados do projeto 54](estudo-3/54)       | Arquivos das métricas para todos o projeto 54            |
| [Dados do projeto 55](estudo-3/55)       | Arquivos das métricas para todos o projeto 55            |
| [Dados do projeto 56](estudo-3/56)       | Arquivos das métricas para todos o projeto 56            |
| [Dados do projeto 78](estudo-3/78)       | Arquivos das métricas para todos o projeto 78            |
| [Dados do projeto 133](estudo-3/133)     | Arquivos das métricas para todos o projeto 133           |
