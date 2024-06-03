import threading
import time  # Importando a biblioteca time

# Definindo a função que será executada em cada thread


def contar_letras(palavra, intervalo):
    # Aguardando por um determinado período de tempo
    time.sleep(intervalo)

    qtd_letras = len(palavra)
    print(f"A palavra '{palavra}' tem {qtd_letras} letras.")


# Criando as threads
thread1 = threading.Thread(target=contar_letras, args=("Python", 3))
thread2 = threading.Thread(target=contar_letras, args=("OpenAI", 2))

# Iniciando a execução das threads
thread1.start()
thread2.start()

# Aguardando a finalização das threads
thread1.join()
thread2.join()

print("Execução das threads finalizada.")
