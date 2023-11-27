import threading
import time
import random
import queue
import sys

class Ixfera:
    def __init__(self, n_vagas, permanencia):
        self.n_vagas = n_vagas
        self.permanencia = permanencia
        self.experiencia_em_curso = None
        self.pessoas_na_ixfera = 0
        self.mutex = threading.Lock()
        self.queue_sem = threading.Semaphore()
        self.enter_sem = threading.Semaphore(0)
        self.cond_var = threading.Condition(lock=self.mutex)

    def full(self):
        return self.pessoas_na_ixfera == self.n_vagas

    def iniciar_experiencia(self, faixa_etaria):
        if self.experiencia_em_curso is None:
            self.experiencia_em_curso = faixa_etaria
            print(f"[Ixfera] Iniciando a experiencia {faixa_etaria}.")

    def entrar_na_ixfera(self, pessoa):

        self.pessoas_na_ixfera +=1
        print(f"[Pessoa {pessoa.numero} / {pessoa.faixa_etaria}] Entrou na Ixfera (quantidade = {self.pessoas_na_ixfera}).")
        if (self.experiencia_em_curso == None):
            self.iniciar_experiencia(pessoa.faixa_etaria)

    def sair_da_ixfera(self, pessoa):
        with self.mutex:
            self.pessoas_na_ixfera -= 1
            print(f"[Pessoa {pessoa.numero} / {pessoa.faixa_etaria}] Saiu da Ixfera (quantidade = {self.pessoas_na_ixfera}).")

            if self.pessoas_na_ixfera == 0:
                self.experiencia_em_curso = None
                print(f"[Ixfera] Pausando a experiencia {pessoa.faixa_etaria}.")
                self.enter_sem.release()

    def entrar_na_fila(self, pessoa):
        print(f"[Pessoa {pessoa.numero} / {pessoa.faixa_etaria}] Aguardando na fila.")

    def finalizar_simulacao(self):
        print("[Ixfera] Simulacao finalizada.")

class Pessoa(threading.Thread):
    def __init__(self, numero, faixa_etaria, ixfera: Ixfera, max_intervalo, unid_tempo):
        super().__init__()
        self.numero = numero
        self.faixa_etaria = faixa_etaria
        self.ixfera = ixfera  # botar global
        self.max_intervalo = max_intervalo
        self.unid_tempo = unid_tempo
        self.wait_time = 0

    def run(self):
        time.sleep(random.randint(1, self.max_intervalo) * self.unid_tempo)  # Simula o tempo de chegada

        self.ixfera.entrar_na_fila(self)
        self.ixfera.entrar_na_ixfera(self)

        entrada_ixfera = time.time()
        saida_ixfera = entrada_ixfera + self.ixfera.permanencia * self.unid_tempo
        self.wait_time = saida_ixfera - entrada_ixfera
        time.sleep(self.wait_time)  # Simula o tempo de permanência

        self.ixfera.sair_da_ixfera(self)

def relatorio_estatistico(tempo_medio_espera, taxa_ocupacao):
    print("\nRelatorio Estatistico:")
    print(f"Tempo medio de espera:")
    for faixa_etaria, tempo_medio in tempo_medio_espera.items():
        print(f"Faixa {faixa_etaria}: {tempo_medio:.2f} ms")

    print(f"\nTaxa de ocupacao: {taxa_ocupacao:.2%}")

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Uso correto: python3 ixphere.py <N_PESSOAS> <N_VAGAS> <PERMANENCIA> <MAX_INTERVALO> <SEMENTE> <UNID_TEMPO>")
        sys.exit(1)

    N_PESSOAS, N_VAGAS, PERMANENCIA, MAX_INTERVALO, SEMENTE, UNID_TEMPO = map(int, sys.argv[1:])
    random.seed(SEMENTE)

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

    tempo_total_simulacao = fim_simulacao - inicio_simulacao
    taxa_ocupacao = ixfera.pessoas_na_ixfera / tempo_total_simulacao
    tempo_medio_espera = {'A': 0, 'B': 0, 'C': 0}

    for pessoa in pessoas:
        tempo_medio_espera[pessoa.faixa_etaria] += pessoa.wait_time

    for faixa_etaria in tempo_medio_espera:
        tempo_medio_espera[faixa_etaria] /= (N_PESSOAS // 3)

    relatorio_estatistico(tempo_medio_espera, taxa_ocupacao)
