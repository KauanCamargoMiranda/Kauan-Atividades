import hashlib


def gerar_hash_sha256(mensagem):
    return hashlib.sha256(mensagem.encode()).hexdigest()

def comparar_hashes(hash1, hash2):
    return hash1 == hash2

if __name__ == "__main__":
    print("Função Hash")
    
    msg1 = input("Digite a primeira mensagem: ")
    msg2 = input("Digite a segunda mensagem: ")

    hash1 = gerar_hash_sha256(msg1)
    hash2 = gerar_hash_sha256(msg2)

    print("\nHash 1:", hash1)
    print("Hash 2:", hash2)

    if comparar_hashes(hash1, hash2):
        print("\n Os hashes são IGUAIS. As mensagens são idênticas.")
    else:
        print("\n Os hashes são DIFERENTES. As mensagens são diferentes.")
