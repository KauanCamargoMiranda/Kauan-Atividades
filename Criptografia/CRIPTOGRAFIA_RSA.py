import hashlib

def gerar_hash_sha256(mensagem):
    mensagem_bytes = mensagem.encode()
    hash_obj = hashlib.sha256(mensagem_bytes)
    hash_hex = hash_obj.hexdigest()
    return hash_hex

if __name__ == "__main__":
    texto = "Kauan123"
    print("Texto original:", texto)

    hash_gerado = gerar_hash_sha256(texto)
    print("Hash SHA-256 gerado:", hash_gerado)
