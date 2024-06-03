import hashlib
import threading


def calcular_hash(arquivo):
    with open(arquivo, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def comparar_arquivos(arquivo1, arquivo2):
    hash_arquivo1 = calcular_hash(arquivo1)
    hash_arquivo2 = calcular_hash(arquivo2)

    if hash_arquivo1 == hash_arquivo2:
        print("Os arquivos são idênticos.")
    else:
        print("Os hashes dos arquivos são diferentes. Realizando comparação byte a byte...")

        with open(arquivo1, 'rb') as f1, open(arquivo2, 'rb') as f2:
            byte1 = f1.read(1)
            byte2 = f2.read(1)
            byte_pos = 0

            while byte1 and byte2:
                if byte1 != byte2:
                    print(f"Os arquivos diferem no byte {
                          byte_pos}: {byte1} != {byte2}")
                    return

                byte1 = f1.read(1)
                byte2 = f2.read(1)
                byte_pos += 1

            if byte1 or byte2:
                print("Os arquivos têm tamanhos diferentes.")
            else:
                print("Os arquivos são idênticos.")


# Caminhos dos arquivos de áudio
caminho_arquivo1 = r"C:\Users\dnzar\OneDrive\Desktop\test\BB02_02_06.wav"
caminho_arquivo2 = r"C:\Users\dnzar\OneDrive\Desktop\test\BB02_06.wav"

# Criar thread para realizar a comparação em paralelo
thread_comparacao = threading.Thread(
    target=comparar_arquivos, args=(caminho_arquivo1, caminho_arquivo2))
thread_comparacao.start()
