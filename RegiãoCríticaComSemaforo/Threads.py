import threading
import time
import random

semaforo =  threading.Semaphore(1)
recursoComp = 0

def regiaoCritica(threadID):
    global recursoComp

    print(f"Thread - {threadID} tentando entrar na região crítica.")

    semaforo.acquire()

    print(f"Thread - {threadID} entrou na região crítica.")

    valorAnterior = recursoComp
    tempoProcessamento = random.uniform(0.5, 2.0)
    time.sleep(tempoProcessamento)
    recursoComp = valorAnterior+1

    print(f"Thread - {threadID} alterou o recurso para {recursoComp}.")

    semaforo.release()

    print(f"Thread - {threadID} saiu da região crítica.")

threads = []
for i in range(5):
    t = threading.Thread(target=regiaoCritica, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nValor final do recurso compartilhado: {recursoComp}")