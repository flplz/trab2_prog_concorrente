import sys
import time
import random
from ixphere_class import Ixfera
from pessoa import Pessoa
from relatorio import relatorio_estatistico


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Uso correto: python3 ixphere.py <N_PESSOAS> <N_VAGAS> <PERMANENCIA> <MAX_INTERVALO> <SEMENTE> <UNID_TEMPO>")
        sys.exit(1)

    N_PESSOAS, N_VAGAS, PERMANENCIA, MAX_INTERVALO, SEMENTE, UNID_TEMPO = map(int, sys.argv[1:])
    random.seed(SEMENTE)

    arg_rules = [
        ('<N_PESSOAS>', 1),
        ('<N_VAGAS>', 1),
        ('<PERMANENCIA>', 1),
        ('<MAX_INTERVALO>', 1),
        ('<SEMENTE>', 0),
        ('<UNID_TEMPO>', 1),
    ]

    for i, arg in enumerate(sys.argv[1:]):
        if int(arg) < arg_rules[i][1]:
            print(f"{arg_rules[i][0]} precisa ser maior ou igual a {arg_rules[i][1]}.")
            sys.exit()

    ixfera = Ixfera(N_VAGAS, PERMANENCIA)

    pessoas = []
    for i in range(1, N_PESSOAS + 1):
        faixa_etaria = random.randint(0, 2)
        faixa_etaria = 'A' if faixa_etaria == 0 else 'B' if faixa_etaria == 1 else 'C'
        pessoa = Pessoa(i, faixa_etaria, ixfera, MAX_INTERVALO, UNID_TEMPO)
        pessoas.append(pessoa)

    inicio_simulacao = time.time()

    for pessoa in pessoas:
        pessoa.start()

    for pessoa in pessoas:
        pessoa.join()

    fim_simulacao = time.time()

    ixfera.finalizar_simulacao()

    # Calcula taxa de ocupacao
    tempo_total_simulacao = fim_simulacao - inicio_simulacao
    taxa_ocupacao = ixfera.tempo_atracao / tempo_total_simulacao

    tempo_medio_espera = {'A': 0., 'B': 0., 'C': 0.}

    # Calcula tempo medio de espera
    for pessoa in pessoas:
        tempo_medio_espera[pessoa.faixa_etaria] += pessoa.wait_time * pessoa.unid_tempo

    for faixa_etaria in tempo_medio_espera:
        n_pessoas = len([p for p in pessoas if p.faixa_etaria == faixa_etaria])
        if n_pessoas > 0: tempo_medio_espera[faixa_etaria] /= n_pessoas

    relatorio_estatistico(tempo_medio_espera, taxa_ocupacao)
