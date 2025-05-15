import threading
import time

contador = 0
rcOcupada = False

def thread(nome):
    global contador, rcOcupada

    for i in range(5):
        while rcOcupada:
            pass

        rcOcupada = True

        print(f"{nome} entrou na região crítica")
        valorAtual = contador
        time.sleep(2.5) 
        contador = valorAtual + 1
        print(f"{nome} saiu da região crítica, contador = {contador}")

        rcOcupada = False

        time.sleep(2.5)

processoA = threading.Thread(target=thread, args=("Processo A",))
processoB = threading.Thread(target=thread, args=("Processo B",))

processoA.start()
processoB.start()

processoA.join()
processoB.join()

print("Valor final do contador:", contador)