from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def criptografar_mensagem(mensagem, chave):
    iv = os.urandom(16)
    cifra = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
    padder = padding.PKCS7(128).padder()
    mensagem_preenchida = padder.update(mensagem.encode()) + padder.finalize()
    criptografador = cifra.encryptor()
    criptografado = criptografador.update(mensagem_preenchida) + criptografador.finalize()
    return iv, criptografado

def descriptografar_mensagem(iv, criptografado, chave):
    cifra = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
    descriptografador = cifra.decryptor()
    mensagem_preenchida = descriptografador.update(criptografado) + descriptografador.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    mensagem = unpadder.update(mensagem_preenchida) + unpadder.finalize()
    return mensagem.decode()

def main():
    print("CRIPTOGRAFIA SIMÉTRICA - AES\n")

    mensagem = input("Digite a mensagem que deseja criptografar: ")
    chave = os.urandom(32)  

    iv, criptografado = criptografar_mensagem(mensagem, chave)
    print("\nMensagem criptografada (hex):", criptografado.hex())

    descriptografada = descriptografar_mensagem(iv, criptografado, chave)
    print("Mensagem descriptografada:", descriptografada)

if __name__ == "__main__":
    main()
