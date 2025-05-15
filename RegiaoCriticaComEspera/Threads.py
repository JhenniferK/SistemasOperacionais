import threading
import time

# Variável compartilhada
contador = 0

# Variável de controle (flag) para a região crítica
regiao_critica_ocupada = False

# Função para simular uma thread acessando a região crítica
def thread_func(nome):
    global contador, regiao_critica_ocupada

    for i in range(5):
        # Espera ocupada
        while regiao_critica_ocupada:
            pass  # Fica esperando até a região ficar livre (busy waiting)

        # Entra na região crítica
        regiao_critica_ocupada = True

        # Início da região crítica
        print(f"{nome} entrou na região crítica")
        valor_atual = contador
        time.sleep(0.1)  # Simula processamento
        contador = valor_atual + 1
        print(f"{nome} saiu da região crítica, contador = {contador}")
        # Fim da região crítica

        regiao_critica_ocupada = False

        # Simula trabalho fora da região crítica
        time.sleep(0.1)

# Criando duas threads
t1 = threading.Thread(target=thread_func, args=("Thread 1",))
t2 = threading.Thread(target=thread_func, args=("Thread 2",))

# Iniciando as threads
t1.start()
t2.start()

# Esperando as duas terminarem
t1.join()
t2.join()

print("Valor final do contador:", contador)