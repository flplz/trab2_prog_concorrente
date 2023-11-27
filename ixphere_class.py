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