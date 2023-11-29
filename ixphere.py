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

    if N_PESSOAS < 1:
        print("<N_PESSOAS> precisa ser maior que 0.")
        sys.exit()
    if N_VAGAS < 1:
        print("<N_VAGAS> precisa ser maior que 0.")
        sys.exit()
    if PERMANENCIA < 1:
        print("<PERMANENCIA> precisa ser maior que 0.")
        sys.exit()
    if MAX_INTERVALO < 1:
        print("<PERMANENCIA> precisa ser maior a 0.")
        sys.exit()
    if SEMENTE < 0:
        print("<PERMANENCIA> precisa ser maior ou igual a 0.")
        sys.exit()
    if UNID_TEMPO < 1:
        print("<UNID_TEMPO> precisa ser  maior que 0.")
        sys.exit()

    ixfera = Ixfera(N_VAGAS, PERMANENCIA)

    pessoas = []
    for i in range(1, N_PESSOAS + 1):
        faixa_etaria = 'A' if i % 3 == 1 else 'B' if i % 3 == 2 else 'C'
        pessoa = Pessoa(i, faixa_etaria, ixfera, MAX_INTERVALO, UNID_TEMPO)
        pessoas.append(pessoa)

    inicio_simulacao = time.time()

    for pessoa in pessoas:
        pessoa.start()

    for pessoa in pessoas:
        pessoa.join()

    fim_simulacao = time.time()

    ixfera.finalizar_simulacao()
    tempo_total_simulacao = fim_simulacao - inicio_simulacao
    taxa_ocupacao = ixfera.pessoas_na_ixfera / tempo_total_simulacao
    tempo_medio_espera = {'A': 0, 'B': 0, 'C': 0}

    for pessoa in pessoas:
        tempo_medio_espera[pessoa.faixa_etaria] += pessoa.wait_time

    for faixa_etaria in tempo_medio_espera:
        tempo_medio_espera[faixa_etaria] /= (N_PESSOAS // 3)

    relatorio_estatistico(tempo_medio_espera, taxa_ocupacao)
