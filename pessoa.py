import threading
import time
import random
import queue
import sys
from ixphere_class import Ixfera

class Pessoa(threading.Thread):
    def __init__(self, numero, faixa_etaria, ixfera: Ixfera, max_intervalo, unid_tempo):
        super().__init__()
        self.numero = numero
        self.faixa_etaria = faixa_etaria
        self.ixfera = ixfera  # botar global
        self.max_intervalo = max_intervalo
        self.unid_tempo = unid_tempo
        self.show_time = 0
        self.wait_time = 0
        self.entrada_fila = 0

    def run(self):
        time.sleep(random.randint(0, self.max_intervalo) * self.unid_tempo/1000)  # Simula o tempo de chegada

        self.entrada_fila = time.time()
        self.ixfera.entrar_na_fila(self)
        self.ixfera.entrar_na_ixfera(self)

        entrada_ixfera = time.time()
        saida_ixfera = entrada_ixfera + self.ixfera.permanencia * self.unid_tempo
        self.show_time = saida_ixfera - entrada_ixfera
        time.sleep(self.show_time/1000)  # Simula o tempo de permanência

        self.ixfera.sair_da_ixfera(self)
