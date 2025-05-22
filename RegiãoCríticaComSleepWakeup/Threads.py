import threading
import time
import random

recursoComp = 0
condicao = threading.Condition()
recursoOcup = False

def regiaoCritica(threadID):
    global recursoComp, recursoOcup

    print(f"Thread - {threadID} tentando entrar na região crítica.")

    with condicao:
        while recursoOcup:
            print(f"Thread - {threadID} esperando (recurso ocupado).")
            condicao.wait()

        recursoOcup = True
        print(f"Thread - {threadID} entrou na região crítica.")

    valor_anterior = recursoComp
    tempo_processamento = random.uniform(0.5, 2.0)
    time.sleep(tempo_processamento)
    recursoComp = valor_anterior + 1

    with condicao:
        recursoOcup = False
        print(f"Thread - {threadID} alterou o recurso para {recursoComp}")
        print(f"Thread - {threadID} saiu da região crítica.\n")
        condicao.notify()

threads = []
for i in range(5):
    t = threading.Thread(target=regiaoCritica, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nValor final do recurso compartilhado: {recursoComp}")
