import threading
import time

contador = 0
rcOcupada = False

def thread_func(nome):
    global contador, rcOcupada

    for i in range(5):
        while rcOcupada:
            pass

        rcOcupada = True

        print(f"{nome} entrou na região crítica")
        valorAtual = contador
        time.sleep(0.1) 
        contador = valorAtual + 1
        print(f"{nome} saiu da região crítica, contador = {contador}")

        rcOcupada = False

        time.sleep(0.1)

t1 = threading.Thread(target=thread_func, args=("Thread 1",))
t2 = threading.Thread(target=thread_func, args=("Thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Valor final do contador:", contador)