Trabalho 2 – IxferaTM
INE5410 – Programação Concorrente – UFSC
Profs. Márcio Castro e Giovani Gracioli
1 Introdução
Uma nova atração que está fazendo muito sucesso em Florianópolis, denominada IxferaTM, foi instalada no estacionamento externo do Villa Romana Shopping. A atração é uma cópia descarada, mas obviamente em proporção muito
menor, do SphereTM de Las Vegas nos EUA (https://www.thespherevegas.com). Ao entrar na atração, os turistas
passam por uma experiência incrível, com tela em 360 graus, som de alta qualidade e diversos efeitos sensoriais.
A IxferaTM possui três experiências (A, B e C) desenvolvidas para faixas etárias diferentes:
• Experiência A: somente para crianças de 4 a 11 anos (faixa etária A);
• Experiência B: somente para adolescentes entre 12 e 18 anos (faixa etária B); e
• Experiência C: somente para adultos acima de 19 anos (faixa etária C).
As regras de funcionamento da IxferaTM são:
1. Uma única fila fora da IxferaTM é utilizada para organizar as pessoas em ordem de chegada (pessoas de diferentes
faixas etárias podem estar na fila);
2. Existe somente uma única experiência em curso na IxferaTM (A, B ou C). Devido as experiências estarem
relacionadas às faixas etárias, nunca haverá pessoas de faixas etárias diferentes simultaneamente na atração;
3. Quando a primeira pessoa ingressa na atração, a IxferaTM inicia automaticamente a experiência equivalente à
faixa etária desta pessoa e outras pessoas da mesma faixa etária podem ingressar na atração;
4. Quando a IxferaTM está funcionando para uma experiência x, ele permanence recebendo pessoas da faixa etária
x na ordem de chegada na fila até que uma outra pessoa de faixa etária diferente x
′
seja a primeira da fila.
Quando isso acontecer, x
′ deverá aguardar que todas as pessoas da faixa etária x saiam da atração para x
′ poder
entrar;
5. A experiência é automaticamente pausada quando não há ninguém na IxferaTM e não existem pessoas aguardando
na fila;
6. Existe um número limitado de vagas (N_VAGAS) na atração, portanto, nunca haverá mais do que N_VAGAS pessoas
simultaneamente na atração;
7. Após entrar na atração, cada pessoa permanece nela por PERMANENCIA unidades de tempo.
2 Definição do Trabalho
O trabalho consiste em desenvolver um programa multithread em Python que simula o comportamento da atração
IxferaTM. A sua solução deverá, obrigatoriamente, considerar os seguintes requisitos:
1. A sua solução deverá rodar com Python v3.10.12 ou superior;
2. Cada pessoa deverá ser representada por uma thread na simulação;
3. Mecanismos de sincronização deverão ser empregados para que as regras definidas anteriormente sejam respeitadas (não será permitido fazer uso da técnica de espera ocupada para fins de sincronização);
4. Uma thread especial deverá ser responsável pela criação das threads que representam as pessoas;
5. O número de pessoas das faixas etárias (A, B e C) que chegam na atração deverá ser aproximadamente o mesmo;
1
6. O tempo de chegada das pessoas na atração assim como as suas idades deverão ser escolhidos de maneira aleatória.
Porém, deverá ser respeitado um intervalo máximo de tempo MAX_INTERVALO entre a chegada de quaisquer duas
pessoas. O método random.randint(a, b) deverá obrigatoriamente ser utilizado para esses fins;
7. A simulação acaba quando a última pessoa sai da atração.
Além das threads que representam pessoas e da thread especial que cria as pessoas, é permitido utilizar outras
threads para realizar atividades específicas na sua simulação.
2.1 Parâmetros de Entrada
O seu programa deverá receber todos os parâmetros através da linha de comando, conforme a seguinte sintaxe:
$ python3 ixphere.py <N_PESSOAS> <N_VAGAS> <PERMANENCIA> <MAX_INTERVALO> <SEMENTE> <UNID_TEMPO>,
onde:
• <N_PESSOAS>: é um número inteiro maior do que zero que representa o número total de pessoas que irão ingressar
na atração (cada faixa etária deverá conter aproximadamente 1/3 do total de pessoas);
• <N_VAGAS>: é um número inteiro maior do que zero que representa o número total de vagas (lugares) na atração;
• <PERMANENCIA>: é um número inteiro maior do que zero que representa a quantidade de unidades de tempo que
as pessoas permanecem na atração;
• <MAX_INTERVALO>: é um número inteiro maior do que zero que representa o intervalo máximo (medido em
unidades de tempo da simulação) entre a chegada de duas pessoas quaisquer na fila;
• <SEMENTE>: é um número inteiro maior ou igual à zero que representa a semente a ser utilizada para inicializar
o gerador de números aleatórios;
• <UNID_TEMPO>: é um número inteiro maior do que zero que representa o tempo, em milissegundos, correspondente
a uma unidade de tempo na simulação (quanto maior esse valor, mais lenta será a simulação).
2.2 Saída do Simulador
Durante a execução do programa, deverá ser impresso na tela as seguintes informações (conforme os padrões
definidos abaixo), onde X é um numero sequencial (iniciando em 1) incrementado toda vez que uma pessoa chega, Y
representa a quantidade de pessoas na atração após o ingresso ou saída da pessoa na/da atração e Z é uma das três
experiências/faixas etárias (A, B ou C):
• Quando a simulação iniciar: [Ixfera] Simulacao iniciada.
• Quando uma pessoa for “criada”: [Pessoa X / Z] Aguardando na fila.
• Quando a IxferaTM iniciar uma experiência: [Ixfera] Iniciando a experiencia Z.
• Quando uma pessoa ingressar na IxferaTM: [Pessoa X / Z] Entrou na Ixfera (quantidade = Y).
• Quando uma pessoa sair da IxferaTM: [Pessoa X / Z] Saiu da Ixfera (quantidade = Y).
• Quando a IxferaTM pausar uma experiência: [Ixfera] Pausando a experiencia Z.
• Quando a simulação finalizar: [Ixfera] Simulacao finalizada.
Além das informações anteriores, ao final da execução do programa deverá ser exibido um pequeno relatório
estatístico no seguinte formato, onde X é um número inteiro em ponto flutuante com precisão de 2 casas decimais:
• Tempo médio de espera, em milissegundos, para ingressar na IxferaTM por faixa etária:
Tempo medio de espera:
Faixa A: X
Faixa B: X
Faixa C: X
• Taxa de ocupação da IxferaTM (tempo em que a atração ficou funcionando dividido pelo tempo total de simulação):
Taxa de ocupacao: X
2
Um pequeno exemplo de saída do simulador (6 pessoas) é mostrado abaixo:
[Ixfera] Simulacao iniciada.
[Pessoa 1 / A] Aguardando na fila.
[Ixfera] Iniciando a experiencia A.
[Pessoa 1 / A] Entrou na Ixfera (quantidade = 1).
[Pessoa 2 / A] Aguardando na fila.
[Pessoa 2 / A] Entrou na Ixfera (quantidade = 2).
[Pessoa 3 / B] Aguardando na fila.
[Pessoa 1 / A] Saiu da Ixfera (quantidade = 1).
[Pessoa 4 / C] Aguardando na fila.
[Pessoa 2 / A] Saiu da Ixfera (quantidade = 0).
[Ixfera] Iniciando a experiencia B.
[Pessoa 3 / B] Entrou na Ixfera (quantidade = 1).
[Pessoa 3 / B] Saiu da Ixfera (quantidade = 0).
[Ixfera] Iniciando a experiencia C.
[Pessoa 4 / C] Entrou na Ixfera (quantidade = 1).
[Pessoa 4 / C] Saiu da Ixfera (quantidade = 0).
[Ixfera] Pausando a experiencia C.
[Pessoa 5 / C] Aguardando na fila.
[Ixfera] Iniciando a experiencia C.
[Pessoa 5 / C] Entrou na Ixfera (quantidade = 1).
[Pessoa 6 / B] Aguardando na fila.
[Pessoa 5 / C] Saiu da Ixfera (quantidade = 0).
[Ixfera] Iniciando a experiencia B.
[Pessoa 6 / B] Entrou na Ixfera (quantidade = 1).
[Pessoa 6 / B] Saiu da Ixfera (quantidade = 0).
[Ixfera] Pausando a experiencia B.
[Ixfera] Simulacao finalizada.
Tempo medio de espera:
Faixa A: 1.02
Faixa B: 5.30
Faixa C: 6.14
Taxa de ocupacao: 0.99
3 Grupos, Avaliação e Entrega
O trabalho deverá ser realizado em grupos de 3 alunos. Os alunos serão responsáveis por formar os grupos
com auxilio da ferramenta “Escolha de Grupos - Trabalho 2 (T2)” disponível no Moodle. Os trabalhos serão
apresentados nos dias definidos no cronograma disponível no Moodle.
Pelo menos um dos integrantes de cada grupo deverá submeter um arquivo compactado em formato zip contendo:
(i) o código fonte da solução do trabalho; e (ii) um relatório em PDF (mínimo 2 páginas) explicando a solução adotada.
A data/hora limite para o envio dos trabalhos é 29/11/2023 às 23h55min. Não será permitida a entrega de
trabalhos fora desse prazo: trabalhos não entregues no prazo receberão nota zero.
O professor irá avaliar a corretude e a clareza da solução. Durante a apresentação, o professor irá avaliar o
conhecimento individual dos alunos sobre os conteúdos teóricos e práticos vistos em aula e sobre a
solução adotada no trabalho. A nota atribuída à cada aluno i no trabalho (NotaT rabalhoi) será calculada da
seguinte forma, onde Ai é a nota referente à apresentação do aluno i e S é a nota atribuída à solução do trabalho:
NotaT rabalhoi =
Ai ∗ S
10
(1)
ATENÇÃO: como indicado pela fórmula mostrada acima, a nota atribuída à solução adotada será ponderada pelo desempenho do aluno durante a apresentação do trabalho. Por exemplo, se o professor atribuir
nota 10 para a solução adotada pelo grupo mas o aluno receber nota 5 pela apresentação – devido ao desconhecimento
dos conteúdos teóricos, práticos e/ou da solução do trabalho – a sua nota final do trabalho será 5. A ausência no dia
da apresentação ou recusa de realização da apresentação do trabalho implicará em nota zero na apresentação, fazendo
com que a nota atribuída ao aluno também seja zero.
3